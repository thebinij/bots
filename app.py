from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        text = request.form.get("textbox")
        return render_template("index.html", output=on_message(text), user_text=text)


def on_message(message):
    return (f'Hello There! {message}')


if __name__ == "__main__":
    app.run()
