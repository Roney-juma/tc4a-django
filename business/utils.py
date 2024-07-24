import africastalking
 
# Initialize the Africastalking SDK
africastalking.initialize(
    'bloowafrica', 'e4844127b4905d49e31a88625ceabee80aaea03d6135a520835ecbd5c5b7a78e')
sms = africastalking.SMS
 
 
def send_sms_alert():
    try:
        response = sms.send(
            "Hello, this is a test message from Africastalking!", ["+254794299622"], 'BLOOW')
        print("Response:", response)
        return response
    except Exception as e:
        print("Error sending message:", e)
        return None
 
 
# Call the function
send_sms_alert()