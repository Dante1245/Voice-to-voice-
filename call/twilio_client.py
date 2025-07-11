from twilio.rest import Client
ACCOUNT_SID = 'your_account_sid'
AUTH_TOKEN = 'your_auth_token'
FROM_NUMBER = '+1234567890'
TO_NUMBER = '+0987654321'
client = Client(ACCOUNT_SID, AUTH_TOKEN)

def start_call():
    call = client.calls.create(
        twiml='<Response><Start><Stream url="wss://yourserver.com/media"/></Start></Response>',
        to=TO_NUMBER, from_=FROM_NUMBER)
    print(f"Call started, SID: {call.sid}")
    return call.sid
