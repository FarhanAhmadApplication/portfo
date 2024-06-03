# TO START YOUR SERVER YOU SHOULD WRITE
# set FLASK_APP=server.py
# TO RUN YOUR SERVER IN DEBUG MODE AS OFF YOU SHOULD WRITE
# flask run
# TO RUN YOUR SERVER IN DEBUG MODE AS ON YOU SHOULD WRITE
# flask --app server.py run --debug
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')


@app.route('/works.html')
def show_works():
    return render_template('works.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'{email, subject, message}\n')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
   if request.method == 'POST':
       try:
           data = request.form.to_dict()
           write_to_csv(data)
           return redirect('/thankyou.html')
       except:
           return 'did not save to database'
   else:
       return 'something went wrong, Try again!'

