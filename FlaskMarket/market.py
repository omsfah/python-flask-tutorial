from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/about/<username>')
def about_page(username):
    return f'<h1> about {username} </h1>' #tillater å sende data fra url til python + håndtere den i programmet

if __name__ == '__main__':
    app.run(debug=True) #tillater å kjøre "direkte" med debug mode (ved filendringer trenger man ikke restarte appen)
