from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True) #tillater å kjøre "direkte" med debug mode (ved filendringer trenger man ikke restarte appen)
