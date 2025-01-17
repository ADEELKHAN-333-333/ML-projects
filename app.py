from flask import Flask, render_template, request
import pandas as pd
import pickle
import numpy as np



app = Flask(__name__)
model=pickle.load(open('LinearRegressionModel.pkl','rb'))

car = pd.read_csv('Notebook/data/Cleaned_Car_data.csv')

@app.route('/predict', methods=['POST'])  # Fixed method to 'methods'
def predict():
    company = request.form.get('company')
    car_model = request.form.get('car_model')
    year = request.form.get('year')
    fuel_type = request.form.get('fuel_type')
    driven = request.form.get('kilo_driven')
    prediction=model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                              data=np.array([car_model,company,year,driven,fuel_type]).reshape(1, 5)))
    print(prediction)

    return str(np.round( prediction[0],2))

@app.route('/')
def home():
    companies = sorted(car['company'].unique())
    
    # Create a dictionary to group car models by company
    car_models_by_company = {}
    for company in companies:
        models = sorted(car[car['company'] == company]['name'].unique())
        car_models_by_company[company] = models
    
    year = sorted(car['year'].unique())
    fuel_type = sorted(car['fuel_type'].unique())

    return render_template('index.html', companies=companies, car_models_by_company=car_models_by_company, year=year, fuel_type=fuel_type)

if __name__ == '__main__':
    app.run(debug=True)
