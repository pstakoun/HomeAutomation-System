from app import app, system

@app.route('/')
@app.route('/index')
def index():
    return ''

@app.route('/start')
def start():
    system.start()
    app.logger.info(system.isRunning())
    return str(system.isRunning())

@app.route('/stop')
def stop():
    system.stop()
    app.logger.info(system.isRunning())
    return str(system.isRunning())
