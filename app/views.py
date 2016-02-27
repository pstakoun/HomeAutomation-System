from app import app, system

@app.route('/')
@app.route('/index')
def index():
    return ''

@app.route('/start')
def start():
    system.start()
    print(str(system.isRunning()), file=sys.stderr)
    return str(system.isRunning())

@app.route('/stop')
def stop():
    system.stop()
    print(str(system.isRunning()), file=sys.stderr)
    return str(system.isRunning())
