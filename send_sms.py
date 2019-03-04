import os
from twilio.rest import Client

account_sid = os.getenv["TWILIO_ACCOUNT_SID"]
auth_token = os.getenv["TWILIO_AUTH_TOKEN"]
#look up os.environ variables, forgot what that means

client = Client(account_sid, auth_token)

client.messages.create(
	to=os.environ["MY_PHONE_NUMBER"],
	from="+14159806136",
	body="Hi Diffles I wrote this script with Twilio to text you"
)
