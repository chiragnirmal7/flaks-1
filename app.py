from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/templates', methods=['POST'])
def predict():
    area = [int(x) for x in request.form.values()]
    age = [int(y) for y in request.form.values()]
    price = [int(z) for z in request.form.values()]

    area1= [np.array(area)]
    age1 = [np.array(age)]
    price1 = [np.array(price)]
    prediction = model.predict(area1, age1, price1)
    
    output = round(prediction[0], 2)
    
    return render_template('index.html', prediction_text='The Price Will be $ {}'.formate(output))


if __name__ =="__main__":
    app.run(debug=True)