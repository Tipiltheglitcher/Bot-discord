from flask import Flask, render_template
import logging

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.info("Le script a été lancé")
    from waitress import serve
    serve(app, host='0.0.0.0', port=8080)
