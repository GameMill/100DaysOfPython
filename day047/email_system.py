import smtplib
import os
import json

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSysten:
    ROOT = os.path.dirname(os.path.abspath(__file__))+"/"

    def __init__(self):
        self.load_api_key()
    
    def load_api_key(self):
        with open(f"{self.ROOT}email.key") as email_file:
            self.EMAIL_DATA = json.load(fp=email_file)

    def send(self,amazon_product):
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Amazon Price Alert!"
        msg['From'] = self.EMAIL_DATA["Username"]
        msg['To'] = self.EMAIL_DATA["ToEmail"]

        text = f"Your {amazon_product[0]} is only {amazon_product[1]}"
        html = f"""\
<html>
    <head></head>
    <body>
        <p>
            Hi!<br>
            {amazon_product[0]} <br>
            is only &pound;{amazon_product[1]}
        </p>
    </body>
</html>
        """
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)
        
        with smtplib.SMTP(self.EMAIL_DATA["Host"]) as smtp:
            smtp.starttls()
            smtp.login(self.EMAIL_DATA["Username"],self.EMAIL_DATA["Password"])
            smtp.sendmail(from_addr=self.EMAIL_DATA["Username"],to_addrs=self.EMAIL_DATA["ToEmail"],
            msg=msg.as_string())