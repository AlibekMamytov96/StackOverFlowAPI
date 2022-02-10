from twilio.rest import Client
from django.conf import settings


account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN
twilio_sender = settings.TWILIO_SENDER_PHONE


def send_activation_sms(phone_number, code):
    client = Client(account_sid, auth_token)
    print(code)
    print('asdasdasd')
    message = f'Your activation code is {code}'
    client.messages.create(
        body=message,
        from_=twilio_sender,
        to=phone_number
    )

