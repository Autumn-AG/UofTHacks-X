import cohere
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("explor.html")


@app.route("/experience")
def experience():
    co = cohere.Client('5VacVLUOm6X42oCEuu9vZ7AOtMFL6A9f0Hxy3A6J')
    a = request.args.get("activity")
    b = request.args.get("location")
    response1 = co.generate(
        model='command-xlarge-nightly',
        prompt='How to start ' + a + ' as a hobby?:',
        max_tokens=600,
        temperature=0.8)
    response2 = co.generate(
        model='command-xlarge-nightly',
        prompt='Locations on google maps to do (' + a + 'in' + b + ') as a list:',
        max_tokens=400,
        temperature=0.8)
    return render_template("op.html", activity=response1.generations[0].text,
                           location=response2.generations[0].text)


if __name__ == "__main__":
    app.debug = True
    app.run()
