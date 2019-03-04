import os
from twilio.rest import Client

account_sid = os.getenv["TWILIO_ACCOUNT_SID"]
auth_token = os.getenv["TWILIO_AUTH_TOKEN"]


client = Client(account_sid, auth_token)

client.messages.create(
	to=os.environ["MY_PHONE_NUMBER"],
	from_="+14159806136",
	body="Hi Diffles I wrote this script with Twilio to text you"
)
