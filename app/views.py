from app import app

@app.route('/')
@app.route('/index')
def index():
    return 'true'

@app.route('/wake')
def wake():
    return 'true'
