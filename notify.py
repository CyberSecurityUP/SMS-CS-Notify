import sys
import json
from twilio.rest import Client

def send_twilio_sms_notification(title, external_ip, internal_ip, hostname, username, twilio_account_sid, twilio_auth_token, twilio_phone_number, recipient_phone_number):

    client = Client(twilio_account_sid, twilio_auth_token)

    message_body = (
        f"{title}\n"
        "New Beacon notification\n"
        f"New Beacon from: {external_ip}\n"
        f"Internal IP: {internal_ip}\n"
        f"Host name: {hostname}\n"
        f"User name: {username}"
    )

    try:
        message = client.messages.create(
            body=message_body,
            from_=twilio_phone_number,
            to=recipient_phone_number
        )
    except Exception as e:
        print(f"Error sending SMS: {e}")
    
if __name__ == "__main__":
    twilio_account_sid = "SID"
    twilio_auth_token = "TOKEN"
    twilio_phone_number = "TWILIO PHONE"
    recipient_phone_number = "YOUR PHONE OR TEAM PHONE"
    if len(sys.argv) < 6:
        print("Usage: python notify.py <title> <external_ip> <internal_ip> <hostname> <username>")
        sys.exit(1)

    title = sys.argv[1]
    external_ip = sys.argv[2].split(':')[1].strip()
    internal_ip = sys.argv[3].split(':')[1].strip()
    hostname = sys.argv[4].split(':')[1].strip()
    username = sys.argv[5].split(':')[1].strip()

    send_twilio_sms_notification(title, external_ip, internal_ip, hostname, username, twilio_account_sid, twilio_auth_token, twilio_phone_number, recipient_phone_number)
