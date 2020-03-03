from flask import Flask, send_file, redirect, url_for, request, jsonify
# To make the start endpoint faster, moving imports to main app
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

app = Flask(__name__)


@app.route('/')
def home_page():
    return '''
    <h1> Model Training Container </h1>
    <p> Go to <container-url>/start to train your model</p>
    <p> And go to <container-url>/download to download the currently trained model</p>
    <p> And go to <container-url>/predict to predict based on currently trained model
        prediction Input :  {"data":[ [25], [23], [10], [9], [3],[25], [23], [10], [9], [3] ] }
        Request Type : POST
        Content Type : application/json
    </p>
    '''


@app.route('/hello')
def hello_page():
    return '''
    <h1>Model Training Container </h1>
    <p> Go to <container-url>/start to train your model</p>
    <p> And go to <container-url>/download to download the currently trained model</p>
    <p> And go to <container-url>/predict to predict based on currently trained model</p>
    '''


@app.route('/predict', methods=['POST'])
def predict_model():
    data = request.get_json()
    if data != None:

        y_predict_new = model.predict(data['data'])
        try:
            predict = pd.DataFrame(y_predict_new)
            return jsonify({'prediction': str(predict.apply(np.round))})
        except Exception as ex:
            print(ex)
            return jsonify({'trace': str(ex)})
    else:
        return '''
            <h1>Model Prediction Container </h1>
            <p> Go to <container-url>/start to train your model</p>
            <p> And go to <container-url>/download to download the currently trained model</p>
            '''


@app.route('/download')
def downloadModel():
    return send_file('azdevopsdemo.pkl', as_attachment=True)


@app.route('/start')
def modelGenerator():
    # Run the Training Script
    modelTrainScript = open('SampleModelGeneratorScriptCopy.py')
    exec(modelTrainScript.read())
    modelTrainScript.close()
    # Run the upload script
    modelUploadScript = open('modelUpload.py')
    exec(modelUploadScript.read())
    modelUploadScript.close()
    return redirect(url_for('downloadModel'))


if __name__ == '__main__':
    model = None
    pkl_file = open('azdevopsdemo.pkl', 'rb')
    model = pickle.load(pkl_file)
    pkl_file.close()
    app.run(host='0.0.0.0', port=8080)
