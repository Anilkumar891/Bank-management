import smtplib
from email.mime.text import MIMEText
from config.config import EMAIL_CONFIG

class EmailAlert:
    def send_alert(self, subject, message):
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = EMAIL_CONFIG["username"]
        msg["To"] = EMAIL_CONFIG["username"]

        with smtplib.SMTP(EMAIL_CONFIG["smtp_server"], EMAIL_CONFIG["port"]) as server:
            server.starttls()
            server.login(EMAIL_CONFIG["username"], EMAIL_CONFIG["password"])
            server.send_message(msg)
            print("Email alert sent.")
