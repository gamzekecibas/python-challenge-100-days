from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import requests

app = Flask(__name__)

USERNAME = "YOUR_USERNAME"
TOKEN = "YOUR_TOKEN"
GRAPH_ID = "exam-prep-tracker"

PIXELA_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_study_time', methods=['POST'])
def add_study_time():
    date = request.form['date']
    minutes = request.form['minutes']

    headers = {
        "X-USER-TOKEN": TOKEN
    }

    pixel_data = {
        "date": datetime.strptime(date, '%Y-%m-%d').strftime('%Y%m%d'),
        "quantity": minutes
    }

    response = requests.post(url=PIXELA_ENDPOINT, json=pixel_data, headers=headers)

    if response.status_code == 200:
        return redirect(url_for('index'))
    else:
        return "Error adding study time", 400

if __name__ == '__main__':
    app.run(debug=True)