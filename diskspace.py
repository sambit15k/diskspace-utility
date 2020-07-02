# The following script is is monitor space on / dir
# Author/Maintainer: Sambit Kumar Nayak
# Date: 02nd June 2020
# + hostname will add the hostname automatically into the subject

import socket
import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
threshold = 85
partition = "/"
hostname = socket.gethostname()

def report_via_email(s):
        print(s)
        msg = MIMEMultipart()
        msg["Subject"] = "Low disk space warning on " + hostname
        sender = "youremailaddress@gmail.com"
        recipient = ["youremailaddress@gmail.com"]
        msg["From"] = sender
        msg["To"] = ', '.join(recipient)
        part = MIMEText(s,'html')
        msg.attach(part)
        with smtplib.SMTP("yoursmtpprovider #for example smtp.elasticemail.com", 2525) as server:
                server.ehlo()
                server.starttls()
                server.login("youremailaddress@gmail.com","your smtp password")
                server.sendmail(sender,recipient,msg.as_string())
def check_once():
        df = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE)
        s = ""
        for line in df.stdout:
                s+=str(line.decode('utf-8'))+'<br>'
                splitline = line.decode().split()
        df = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE)
        for line in df.stdout:
                splitline = line.decode().split()
                if splitline[5] == partition:
                        if int(splitline[4][:-1]) > threshold:
                                report_via_email(s)
check_once()