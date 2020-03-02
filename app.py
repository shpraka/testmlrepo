# import pandas as pd
import numpy as np
import pickle
import sys
# from sklearn.model_selection import train_test_split
# API definition
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    return jsonify({'this will be predict return': "predicting"})
    # data = request.get_json()
    # y_predict_new = model.predict(data['data'])
    # try:
    #     predict = pd.DataFrame(y_predict_new)
    #     return jsonify({'prediction': str(predict.apply(np.round))})
    # except Exception  as ex:
    #     print(ex)
    #     return jsonify({'trace': "tracing"})

@app.route('/hello', methods=['GET'])
def hell0():
	return jsonify({'trace': "tracing", "message" : "your change is deployed"})
	
if __name__ == '__main__':
    model = None;
    port = 8080
    
    # pkl_file = open('azdevopsdemo.pkl', 'rb')
    # model = pickle.load(pkl_file)
    # pkl_file.close()
    
    app.run(host='0.0.0.0',port=port, debug=True)