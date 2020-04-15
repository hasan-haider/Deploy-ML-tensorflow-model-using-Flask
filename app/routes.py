import os

from flask import render_template, request
from werkzeug.utils import redirect
from app import app,APP_ROOT

from app.process import predict_img


@app.route('/')
def home():
    return render_template('index.html',title='Home')

@app.route('/about')
def about():
    return render_template('about.html',title='About',name='Passed by variable')

@app.route("/predict")
def predict():
    return render_template("predict.html",title="Predict")

@app.route("/upload",methods=["GET","POST"])
def upload():
    target = os.path.join(APP_ROOT, 'temp/')
    if request.method == 'POST':
        file = request.files['img'] # 'img' is the id passed in input file form field
        filename = file.filename
        # filename = filename(filename)
        file.save("".join([target, filename])) #saving file in temp folder
        print("upload Completed") #printing on terminal

        return redirect('/prediction/{}'.format(filename))

@app.route("/prediction/<filename>",methods=["GET","POST"])
def prediction(filename):
    #imported process.py
    x=predict_img(filename) #imported from process file
    return render_template('output.html',results=x)
