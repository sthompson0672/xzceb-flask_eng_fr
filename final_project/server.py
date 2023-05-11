from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/englishToFrench', methods=['POST'])
def english_to_french():
    english_text = request.form['english_text']
    if not english_text:
        return "Please provide English text"
    translated_text = translator.english_to_french(english_text)
    return translated_text

@app.route('/frenchToEnglish', methods=['POST'])
def french_to_english():
    french_text = request.form['french_text']
    if not french_text:
        return "Please provide French text"
    translated_text = translator.french_to_english(french_text)
    return translated_text

if __name__ == '__main__':
    app.run()
