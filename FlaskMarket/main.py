import pandas as pd
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def home_page():
    if request.method == 'POST':
        if request.form.get('refresh-button') == '1':
            print("entering refresh routine")
            datatmp=pd.read_csv('data.csv')
            datatmp2=datatmp.to_html()
            print(datatmp2)
            pass
    return render_template('home.html')

@app.route('/upload', methods = ['POST'])  
def upload():  
    if 'file' in request.files:
        file = request.files['file']
        if  file and allowed_file(file.filename):
            file.save("data.csv")
        return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True) #tillater å kjøre "direkte" med debug mode (ved filendringer trenger man ikke restarte appen)
