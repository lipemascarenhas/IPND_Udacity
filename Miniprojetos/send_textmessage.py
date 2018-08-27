from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC3dff99a7bfce84512631d2148d8a652b"
# Your Auth Token from twilio.com/console
auth_token  = "9819cd48e01580d3069db3aa022bd7bf"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5519992803485",
    from_="+13013272097 ",
    body="Carol! Corra para as colinas antes que seja tarde e o hamburguer esfrie!!!!")

print(message.sid)
