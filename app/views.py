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

@app.route('/count-captures')
def countCaptures():
    return str(system.countCaptures())

@app.route('/capture/<n>')
def capture(n):
    return send_file('/home/pi/HAS-captures/'+system.getCapture(int(n)), mimetype='image/jpeg')
