import africastalking
import requests

# Initialize the SDK with your username and API key
africastalking.initialize('boowafrica', 'e4844127b4905d49e31a88625ceabee80aaea03d6135a520835ecbd5c5b7a78e')
sms = africastalking.SMS

def send_sms_alert():
    recipients = ['+254710248170']  # List of phone numbers
    message = 'Hello, World!'       # The message content

    try:
        response = sms.send(message, recipients)
        return response
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return None

# Example usage
response = send_sms_alert()
print(response)


# Alternative way by using requests directly




send_sms_alert()