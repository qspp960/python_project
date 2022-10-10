from twilio.rest import Client
import smtplib

TWILIO_SID = 'ACf2af7b4d134c67131bc7a5f521c4ef5c'
TWILIO_AUTH_TOKEN = 'e01daad4091470193cadb8ab92d81884'

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_="+19805750448",
            to="+1040156267",
        )

    def send_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP('EMAIL_PROVIDER_SMTP_ADDRESS') as connection:
            connection.starttls()
            connection.login('euihyun960@gmail.com,' 'MY_PASSWORD')
            for email in emails:
                connection.sendmail(
                    from_addr='euihyun960@gmail.com',
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )


