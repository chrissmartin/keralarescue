import os
import sys
import json
from datetime import datetime

import requests
from flask import Flask ,render_template, redirect, url_for, session, request, logging

app = Flask(__name__)

@app.route('/accept/<string:timeindex>',methods=['GET','POST'])
def accept(timeindex):
    url = 'https://byw1s98hik.execute-api.ap-south-1.amazonaws.com/dev/webapp/accepted'
    data = {'TimeIndex':timeindex}
    headers = {'content-type': 'application/json'}
    r=requests.post(url, data=json.dumps(data), headers=headers)
    data = r.json()
    print(data)
    return redirect(url_for('home'))


@app.route('/kerala', methods=['GET','POST']) #landing page
def home1():
    if request.method == 'POST':
        keyword1 = request.form['data']
        url = 'https://byw1s98hik.execute-api.ap-south-1.amazonaws.com/dev/webapp/district'
        data = {'keyword':keyword1}
        headers = {'content-type': 'application/json'}
        r=requests.post(url, data=json.dumps(data), headers=headers)
        data = r.json()
        request_no = data['Count']
        return render_template("index.html",requestnumber = request_no, data = data, district = keyword1)

        
    r = requests.get('https://byw1s98hik.execute-api.ap-south-1.amazonaws.com/dev/androidapp/get')
    data = r.json() 
    request_no = data['Count']
    return render_template("index.html",requestnumber = request_no, data = data)

@app.route('/', methods=['GET','POST']) #landing page
def home():
    if request.method == 'POST':
        keyword1 = request.form['data']
        url = 'https://byw1s98hik.execute-api.ap-south-1.amazonaws.com/dev/webapp/district'
        data = {'keyword':keyword1}
        headers = {'content-type': 'application/json'}
        r=requests.post(url, data=json.dumps(data), headers=headers)
        data = r.json()
        request_no = data['Count']
        return render_template("index.html",requestnumber = request_no, data = data, district = keyword1)   
    r = requests.get('https://byw1s98hik.execute-api.ap-south-1.amazonaws.com/dev/androidapp/get')
    data = r.json()
    request_no = data['Count']
    return render_template("index.html",requestnumber = request_no, data = data)

@app.context_processor
def date_processor():
    def change_epoch(epoch):
        ts = int(epoch)
        ts = ts/1000
       
        return datetime.fromtimestamp(ts).strftime('%Y-%m-%d %I:%M %p')
    return dict(change_epoch=change_epoch)
    
if __name__=='__main__':

	app.run(threaded=True,host="0.0.0.0",port=80) #Debugger is set to 1 for testing and overriding the default port to http port
