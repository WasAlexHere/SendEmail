import smtplib
import os
import imghdr
from email.message import EmailMessage

def send_mail():
    server =smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('', '')

    message = EmailMessage()
    message['Subject'] = 'Script caught unstable behavior on local machine'
    message['From'] = ''
    message['To'] = ''
    message.set_content('The python script caught unstable behavior of test on local machine!''\n'
                        'You can find Failures.txt, SRStat.txt and a screenshot in attached''\n''\n'
                        'Do not reply to this email!')
    #files = ['design','failures','srstat','screen']
    #for file in files:
    #   with open(file,'rb') as f:
    with open('shibuya_1_big.jpg','rb') as image:
        file_data = image.read()
        file_type = imghdr.what(image.name) #закоментировать для документов
        file_name = image.name

    message.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
    #message.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    server.send_message(message)

send_mail()