from app import app, system
from flask import send_file, make_response, request, current_app
from datetime import timedelta
from functools import update_wrapper

def crossdomain(origin=None, methods=None, headers=None,
                max_age=21600, attach_to_all=True,
                automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers
            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            h['Access-Control-Allow-Credentials'] = 'true'
            h['Access-Control-Allow-Headers'] = \
                "Origin, X-Requested-With, Content-Type, Accept, Authorization"
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator

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
