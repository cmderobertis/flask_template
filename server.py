from flask import Flask, render_template, session, request, redirect, url_for
from database_name import SomeClass

app = Flask(__name__)
app.secret_key = 'there is a fire in the building'


@app.route('/')
def index():
    friends = SomeClass.get_all()
    return render_template('index.html', friends=friends)


if __name__ == '__main__':
    app.run(debug=True)
