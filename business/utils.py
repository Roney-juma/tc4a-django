import africastalking
 
# Initialize the Africastalking SDK
africastalking.initialize(
    'bloowafrica', 'e4844127b4905d49e31a88625ceabee80aaea03d6135a520835ecbd5c5b7a78e')
sms = africastalking.SMS
 
 
def send_sms_alert(message,phone_number):
    try:
        response = sms.send(
            message, [phone_number], 'BLOOW')
        print("Response:", response)
        return response
    except Exception as e:
        print("Error sending message:", e)
        return None
