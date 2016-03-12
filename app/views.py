from app import app, system
from flask import send_file

@app.route('/')
@app.route('/index')
def index():
    return ''

@app.route('/start')
def start():
    system.start()
    return str(system.isRunning())

@app.route('/stop')
def stop():
    system.stop()
    return str(system.isRunning())

@app.route('/isRunning')
def isRunning():
    return str(system.isRunning())

@app.route('/captures')
def captures():
    return str(system.captures)

@app.route('/count-captures')
@crossdomain(origin='*')
def countCaptures():
    return str(system.countCaptures())

@app.route('/capture/<n>')
@crossdomain(origin='*')
def capture(n):
    return send_file('/home/pi/HAS-captures/'+system.getCapture(int(n)), mimetype='image/jpeg')

@app.route('/capture/<n>/date')
@crossdomain(origin='*')
def captureDate(n):
    fileName = system.getCapture(int(n))
    return fileName[:4]+'-'+fileName[4:6]+'-'+fileName[6:8]+' '+fileName[8:10]+':'+fileName[10:12]+':'+fileName[12:14]
