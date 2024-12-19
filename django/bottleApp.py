from bottle import Bottle, run, template

app = Bottle()

@app.route("/")
def home():
    return template('''
<h1> Welcome to my world!</h1>
''')


run(app, host='localhost', port=5678)
