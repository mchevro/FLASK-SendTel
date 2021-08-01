from flask import Flask, render_template, request 
import requests, datetime

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        get_ip = request.environ['REMOTE_ADDR']
        get_datetime = datetime.datetime.now().strftime("%Y-%m-%d %X")
        get_message = request.form['message'] 
        requests.get(f"https://api.telegram.org/[API_BOT]/sendMessage?chat_id=-579314817&text=REQUEST LAGU%E2%9D%97%0aIP : {get_ip}%0aWaktu : {get_datetime}%0aPesan : {get_message}")
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')