import os
from twilio.rest import Client

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

client.messages.create(
	to=os.environ["MY_PHONE_NUMBER"],
	from_="+14159806136",
	body="If you're receiving this message, my twilio app works!"
)
