from twilio.rest import Client


account_sid = '12347qwertyujhvc'
auth_token = 'dfghjkldtfghbnm '
twilio_phone_number = '+1223456789098765'
client = Client(account_sid, auth_token)

def send_sms(to_number, message_body):
    try:
        message = client.messages.create(
            body=message_body,
            
            from_=twilio_phone_number,
            
            to=to_number
        )
        print(f'SMS sent successfully. SID: {message.sid}')
    except Exception as e:
        print(f'Failed to send SMS: {e}')


to_number = input('Enter the recipient phone number: ')
message_body = input('Enter the message body: ')

send_sms(to_number, message_body)
