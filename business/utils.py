import africastalking
import requests

africastalking.initialize('sandbox', 'atsk_3441882cc226354f7f3594da6b40ff14cc126eb1a747302af123aaa12d4d6c5c798489c2')
sms = africastalking.SMS

# Send SMS with SSL verification disabled (for testing only)
def send_sms_alert():
    response = sms.send('message', ['+254710248170'], verify=False)
    return response

# Alternative way by using requests directly




send_sms_alert()