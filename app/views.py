from app import app

running = False

@app.route('/')
@app.route('/index')
def index():
    return ''

@app.route('/start')
def start():
    running = True
    return str(running)

@app.route('/stop')
def stop():
    running = False
    return str(running)
