from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/englishToFrench', methods=['POST'])
def english_to_french():
    textToTranslate = request.args.get('textToTranslate')
    french_text= translator.english_to_french(textToTranslate)
    return french_text

@app.route('/frenchToEnglish', methods=['POST'])
def french_to_english():
    textToTranslate = request.args.get('textToTranslate')
    french_text= translator.french_to_english(textToTranslate)
    return french_text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
