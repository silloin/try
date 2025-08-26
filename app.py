from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    year = request.form['Year']
    rainfall = request.form['average_rain_fall_mm_per_year']
    pesticides = request.form['pesticides_tonnes']
    temp = request.form['avg_temp']
    area = request.form['Area']
    item = request.form['Item']

    # Dummy prediction logic (replace with your model)
    prediction = float(rainfall) * 0.1 + float(pesticides) * 0.2 + float(temp) * 0.3

    # Pass prediction to result.html
    return render_template('result.html', prediction=f"{prediction:.2f} hg/ha")
@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
