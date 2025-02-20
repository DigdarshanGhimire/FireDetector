from flask import Flask
from flask import render_template, send_from_directory, request
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




app = Flask(__name__)

app.secret_key = 'mechaction1234'

@app.route('/', methods= ['GET'])
def home():
    with open('data.json') as f:
        text = f.read()
        
    data = json.loads(text)
    return render_template('index.html',data=data)


@app.route('/api/fetch/data', methods=["POST"])
def fetch():
    data = request.get_json()
    temperature = data.get("temperature")
    humidity = data.get("humidity")
    gasValue = data.get("gasValue")
    data = json.dumps(data)
    try:
        with open('data.json','w') as f:
            f.write(data)
    except:
        pass
    
    if temperature>45 or humidity<20 or gasValue>1931:
        response = send_push_notification("Fire detected!", "Fire has been detected. Take immediate action")
        return {"message":"The threshold was exceeded"}
    
    return {"message":"The data was fetched successfully"}
    

@app.route('/OneSignalSDKWorker.js')
def serve_file():
    return send_from_directory('.', 'OneSignalSDKWorker.js')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


if __name__ == "__main__":
    app.run(debug=True)