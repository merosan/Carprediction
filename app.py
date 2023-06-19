from flask import Flask, request
from flask_cors import CORS
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
import pickle
import os

app = Flask(__name__)
CORS(app)

@app.route("/api/predict/", methods=['GET'])

def predict():
    hour = int(request.args['hour'])
    temperature = float(request.args['temperature'])
    weekday = int(request.args['weekday'])
    richtung = int(request.args['richtung'])

    df = pd.read_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'merged_data.csv'), sep=',', encoding='utf-8')

    gradientboost_model = GradientBoostingRegressor()
    model_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gradient_boost_regression.pkl")
    with open(model_filename, 'rb') as f:
        gradientboost_model = pickle.load(f)


    prediction = gradientboost_model.predict([[hour, temperature, weekday, richtung, df['Month'].iloc[0], df['Year'].iloc[0], df['Day'].iloc[0], df['holiday'].iloc[0],df['Niederschlag'].iloc[0], df['Luftfeuchtigkeit (%Hr)'].iloc[0], df['Luftdruck (hPa)'].iloc[0]]])
    return str(round(prediction[0]))

@app.route('/')
def hello_world():
    print(request.args)
    return 'Hello World!'