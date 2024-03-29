from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
BOT_TOKEN = '6449907754:AAGG9xeTWA12a828byAc7YPnr12dPnC5c4A'
TELEGRAM_API_BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

def send_to_telegram(message):
    data = {
        'chat_id': '1113780746',  # Replace with your Telegram chat ID
        'text': message
    }
    response = requests.post(TELEGRAM_API_BASE_URL + 'sendMessage', data=data)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        form_data = request.form
        # Process the form data and create the message you want to send to Telegram
        message = f"Form Inputs:\nName: {form_data['name']}\nEmail: {form_data['email']}\nMobile Number:{form_data['number']}\nSubject: {form_data['subject']}\nMessage: {form_data['message']}"
        send_to_telegram(message)
        

    return render_template('Home.html')
@app.route('/about')
def about():
    return render_template('aboutme.html')
@app.route('/project1')
def project_1():
    return render_template('project.html')
@app.route('/project 2')
def project_2():
    return render_template('project 2-details.html')
@app.route('/project 6')
def project_6():
    return render_template('project 6-details.html')

if __name__ == '__main__':
    app.run(debug = True)