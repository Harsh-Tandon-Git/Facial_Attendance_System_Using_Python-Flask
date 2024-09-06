from flask import Flask, render_template, request, send_file
import os
import csv
from datetime import datetime

app = Flask(__name__)
 
# Initialize attendance list
attendance = []

@app.route('/')
def index():
    return render_template('index.html', attendance=attendance)

@app.route('/add_faces', methods=['POST'])
def add_faces():
    print(request.form)
    name = request.form['name']
    os.system('python Add_faces.py ' + name)
    return "Face added successfully!"

@app.route('/recognise_faces', methods=['POST'])
def recognise_faces():
    os.system('python recognise_faces.py')
    return "Attendance recorded successfully!"

@app.route('/download_attendance', methods=['POST'])
def download_attendance():
    if os.path.exists("attendance.csv"):
        # Send the file as a response for download
        return send_file("attendance.csv", as_attachment=True)
    else:
        return "Attendance file not found"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5001")
