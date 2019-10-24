from twilio.rest import Client

def send_msg(event=None, context=None):

    # get your sid and auth token from twilio
    twilio_sid = ''
    auth_token = ''

    whatsapp_client = Client(twilio_sid, auth_token)

    # keep adding contacts to this dict to send
    # them the message
    contact_directory = {'testuser':'+1234567890'}

    for key, value in contact_directory.items():
        msg_from_dir = whatsapp_client.messages.create(
                body = 'Test from Twilio',
                from_= 'whatsapp:+1',
                to='whatsapp:' + value,

            )

        print(msg_from_dir.sid)

send_msg()