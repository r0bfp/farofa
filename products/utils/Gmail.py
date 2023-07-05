import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Gmail:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password


    def send(self, to: str, subject: str, body_as_html: str) -> None:
        body_as_html = MIMEText(body_as_html, 'html')

        message = MIMEMultipart('alternative')

        message['Subject'] = subject
        message['From'] = self.username
        message['To'] = to

        message.set_payload(body_as_html)

        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(self.username, self.password)  
        server.sendmail(self.username, to, message.as_string())
        server.close()
