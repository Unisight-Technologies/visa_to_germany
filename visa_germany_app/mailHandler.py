from django.core.mail import send_mail
import environ
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

env = environ.Env()
# reading .env file
environ.Env.read_env()

def sendMailToUser(name, send_to):
	subject = "Thanks for contacting us"
	message = "Hello "+name+"! \n\nWe have successfully received your message.\n\nWe will get back to you as soon as possible.\n\nRegards\n- Visa To Germany."
	msg = Mail(
		from_email='unisighttechnologies@gmail.com',
		to_emails=send_to,
		subject=subject,
		html_content=message
	)

	try:
		sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
		response = sg.send(msg)

	except Exception as e:
		print(e)


def sendMailToVisaToCanada(name, email, phone, subject, message):
	message = "A new message has been received on our website:\n\nName: "+name+"\nEmail Id: "+email+"\nPhone: "+phone+"\nSubject: "+subject+"\nMessage: "+message+"\n\n\nRegards"
	subject = "A message has been received on Visa to Germany."
	msg = Mail(
		from_email='unisighttechnologies@gmail.com',
		to_emails='info@visatogermany.com',
		subject=subject,
		html_content=message
	)

	try:
		sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
		response = sg.send(msg)
	except Exception as e:
		print(e)
