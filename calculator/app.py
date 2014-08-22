# encoding=utf-8

from flask import Flask, render_template
from logic import Calculator, ValueTooLowException, ValueTooHighException

app = Flask(__name__)


@app.route("/calc/<a>*<b>")
def multiply(a, b):
    c = Calculator()

    try:
        result = c.mul(int(a), int(b))
    except ValueTooLowException as e:
        return e.message, 403
    except ValueTooHighException as e:
        return e.message, 403
    return str(result)


@app.route("/calc/<a>/<b>")
def divide(a, b):
    c = Calculator()

    try:
        result = c.div(int(a), int(b))
    except ValueTooLowException as e:
        return e.message, 403
    except ValueTooHighException as e:
        return e.message, 403
    except ZeroDivisionError:
        return 'cannot divide by 0', 403
    return str(result)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010, debug=True)
