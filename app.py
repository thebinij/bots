from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from waitress import serve

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        text = request.form.get("textbox")
        return render_template("index.html", output=on_message(text), user_text=text)


@app.route('/api', methods=['GET', 'POST'])
def api():
    if request.method == "GET":
        return jsonify({'data': 'It is now working'})
    if request.method == "POST":
        username = request.json['name']
        return jsonify({"reponse": f"Hello {username}"})


def on_message(message):
    return (f'Hello There! {message}')


mode = 'dev'

if __name__ == "__main__":
    if mode == 'dev':
        app.run(host="0.0.0.0", port=5201, debug=True)
    else:
        serve(app, host="0.0.0.0", port=8080)
