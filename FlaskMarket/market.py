from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1> Hello world, changed again</h1>'

@app.route('/about/<username>')
def about_page(username):
    return f'<h1> about {username} </h1>'

app.run(debug=True) #tillater å kjøre "direkte" med debug mode (ved filendringer trenger man ikke restarte appen)
