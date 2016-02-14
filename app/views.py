from app import app, system

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
