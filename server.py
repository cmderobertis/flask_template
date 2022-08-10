from flask import Flask, render_template, session, request, redirect, url_for
from database_name import ClassName, And, Any, Other, Table, Classes, You, Have

app = Flask(__name__)
app.secret_key = 'I suppose changing this is not absolutely necessary, but do it anyway.'


@app.route('/')
def index():
    friends = ClassName.get_all()
    if friends[0]:
        print("First item:", friends[0])
    return render_template('index.html', friends=friends, page_title='My Flask App')


if __name__ == '__main__':
    app.run(debug=True)
