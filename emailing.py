import smtplib
import imghdr
from email.message import EmailMessage

password = ''
SENDER = ''
RECEIVER = ''


def send_email(img_path):
    print('Send email start')
    email_msg = EmailMessage()
    email_msg['Subject'] = 'New customer showed up!'
    email_msg.set_content('Hello')

    with open(img_path, 'rb') as file:
        content = file.read()

    email_msg.add_attachment(content, maintype='image', subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP('smtp.gmail.com', port=587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, password)
    gmail.sendmail(SENDER, RECEIVER, email_msg.as_string())
    gmail.quit()
    print('Send email start')

if __name__ == '__main__':
    send_email(img_path='images/images1.png')
