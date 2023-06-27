from flask import Flask, redirect, url_for
import datetime

app = Flask(__name__)


@app.route("/")
def home():
    age = get_age()
    return f"<p>Rod Stewart is {age} years old</p>"


def get_age() -> str:
    birthday = datetime.datetime(1945, 1, 10)
    today = datetime.date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
    return str(age)


if __name__ == "__main__":
    app.run()
