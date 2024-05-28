import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time

# Track the number of emails sent
emails_sent_today = 0
DAILY_LIMIT = 500  # Set this to your email provider's daily limit

def send_email():
    global emails_sent_today

    if emails_sent_today >= DAILY_LIMIT:
        print("Daily email limit reached.")
        return

    # Define email parameters
    from_addr = 'kariukid238@gmail.com'
    recipients = ['janetndirangu52@example.com', 'kariukidaniel854@example.com', 'tradetribe3@example.com' , 'fakebanks254@example.com', 'joaephkanyoro001@example.com']
    subject = 'Daily Report'
    body = '''
    Dear Trader,

As we navigate the ever-changing landscape of the forex market, it's crucial to stay informed and inspired. Your dedication to mastering the art of trading is commendable, and I'm here to support you every step of the way.

Remember, success in trading comes from continuous learning, adaptability, and a resilient mindset. Embrace the challenges and setbacks as opportunities for growth, and never lose sight of your long-term goals.

To enhance your trading journey further, I invite you to connect with me on Twitter and subscribe to my YouTube channel. On Twitter, I share daily insights, market updates, and trading tips that can help you make informed decisions in real-time. My YouTube channel offers in-depth tutorials, analysis, and interviews with industry experts to expand your knowledge and refine your trading strategies.

Let's empower each other to thrive in the forex market. Follow me on Twitter (https://x.com/Aj_Aq9) and subscribe to my YouTube channel (www.youtube.com/@Aj.-) today!

Wishing you profitable trades and continued success.

Best regards,
[TradeTribe]
'''

    for to_addr in recipients:
        if emails_sent_today >= DAILY_LIMIT:
            print("Daily email limit reached.")
            return

        # Create a multipart message
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = subject

        # Attach the body with the msg instance
        msg.attach(MIMEText(body, 'plain'))

        # Create the report (For example purposes, using a DataFrame)
        data = {'Date': pd.date_range(start='1/1/2023', periods=5),
                'Value': [100, 200, 300, 400, 500]}
        df = pd.DataFrame(data)

        # Save the report to a file
        file_path = 'report.csv'
        df.to_csv(file_path, index=False)

        # Open the file to be sent
        attachment = open(file_path, 'rb')

        # Instance of MIMEBase and named as part
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename=report.csv')

        # Attach the instance 'part' to instance 'msg'
        msg.attach(part)

        # SMTP server setup
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_user = 'kariukid238@gmail.com'
        smtp_password = '@guvapya73A.'

        # Create SMTP session
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)

        # Convert the Multipart msg into a string
        text = msg.as_string()

        # Sending the mail
        server.sendmail(from_addr, to_addr, text)
        emails_sent_today += 1
        print(f"Email sent successfully to {to_addr}. Emails sent today: {emails_sent_today}")

    server.quit()

# Schedule the send_email function to run daily
schedule.every().day.at("08:00").do(send_email)

# Reset the email count at midnight
def reset_email_count():
    global emails_sent_today
    emails_sent_today = 0

schedule.every().day.at("00:00").do(reset_email_count)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
