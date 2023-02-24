import pickle
from flask import Flask, render_template, request

app = Flask(__name__) 
model = pickle.load(open('model.pkl','rb'))
@app.route('/')
def index():

    return render_template("home.html")
@app.route('/predict',methods=['GET','POST'])
def predict():
    new_var = float(request.form.get('temperature'))
    prediction = model.predict([[new_var]])
    output = round(prediction[0],2)
    return render_template("home.html",text=f"The predicted revenue is {output}")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')