from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the trained spam classifier
model = joblib.load(r'D:\Downloads\spam_classifier_pipeline.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    email_text = ""
    if request.method == 'POST':
        email_text = request.form['email_text']
        if email_text.strip() != "":
            prediction = model.predict([email_text])[0]
            result = 'Spam' if prediction == 1 else 'Ham'
    return render_template('index.html', result=result, email_text=email_text)

if __name__ == '__main__':
    app.run(debug=True)
