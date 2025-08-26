from flask import Flask, render_template, request, send_from_directory, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    year = request.form['Year']
    rainfall = request.form['average_rain_fall_mm_per_year']
    pesticides = request.form['pesticides_tonnes']
    temp = request.form['avg_temp']
    area = request.form['Area']
    item = request.form['Item']

    prediction = float(rainfall) * 0.1 + float(pesticides) * 0.2 + float(temp) * 0.3

    return render_template('result.html', prediction=f"{prediction:.2f} hg/ha")

@app.route('/about')
def about():
    return render_template('about.html')

# ✅ Route to download PDF
@app.route('/download_pdf')
def download_pdf():
    return send_from_directory('static', 'stp.pdf', as_attachment=True)

# ✅ Route to view PDF
@app.route('/view_pdf')
def view_pdf():
    return redirect(url_for('static', filename='stp.pdf'))

if __name__ == '__main__':
    app.run(debug=True)
