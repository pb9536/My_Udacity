from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa9e89d50c1ffd9310294a3eed7bf6b01"
# Your Auth Token from twilio.com/console
auth_token  = "5d13d272aadce9b376d6a3aa7bf2cc24"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919985197278", 
    from_="+15753668089",
    body="Hello from Python!")

print(message.sid)
