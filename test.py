import requests
import json

ONESIGNAL_APP_ID = "26191724-825a-462b-b4c4-8a6be7ef71a0"  # Replace with your OneSignal App ID
ONESIGNAL_API_KEY = "os_v2_app_eymrojecljdcxngerjv6p33ruaqokgbq3k4uryf74hetjr52etsotlc57dy26yxlcxiwgda5uydqts3zdiqqr6raemknwiem7rjwfka"  # Replace with your OneSignal REST API Key

def send_push_notification(title, message, user_id=None):
    url = "https://api.onesignal.com/notifications"
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": f"Key {ONESIGNAL_API_KEY}",
    }

    payload = {
        "app_id": ONESIGNAL_APP_ID,
        "headings": {"en": title},
        "contents": {"en": message},
        "included_segments": ["All"],
        "target_channel":"push"
    }


    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()



