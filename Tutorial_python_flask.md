## Flask Tutorial part 1

(venv)$ `pip3 install flask`

> To install flask into the virtual environment

```python
from flask import Flask
app = Flask(__name__)
```

> 'app' is the instance of a Flask class. \_\_name\_\_ is just the name of the module.

```python
@app.route("/")
def hello():
    return 'Hello world!'
```

> routes are what we type in browser's address to go to different pages of a web browser. @ indicates a python decorator. A decorator adds additional funcitionality to the existing function. "/" indicates homepage or index.html of a website.

(venv)$ `export FLASK_APP=app.py`

> This will create an environment variable for the flask app in Mac or Linux. for windows, use `set` instead of `export`.

(venv)$ `flask run`

> This will run flask application. the app running on ip address: 127.0.0.1 and port 5000. we can use 'localhost' instead of ip address in the browser also.

(venv)$ `export FLASK_DEBUG=1`

> This will run in flask in debug mode which enables not to restart flask application after every changes and it does automatically, just we need to reload in the browser. Another way to run flask application without setting enviroment variable is given below.

```python
if __name__ == '__main__':
    app.run(debug=True)
```

> This condition is only true if we run this file directly. If we import it anywhere and run, the above if condition will not execute. we can run the program as

(venv)$ `python3 app.py`

> This is more user friendly than setting environment variable everytime we want to run.

```python
@app.route("/about")
def hello():
    return 'about page'
```

> This will create a about page of the website.

```python
@app.route("/")
@app.route("/home")
def home():
    return 'home page'
```

> both two routes handled by a same function

---

sources: [Corey Schafer Flask tutorial part 1](https://youtu.be/MwZwr5Tvyxo?si=dDDSeIZTt5IV7Hl0 "video tutorial")

## Flask Tutorial part 2

```python
from flask import Flask, render_template, url_for
# render_template is used to render a webpage.
# url_for is used to generate a url for specific function dynamically
app = Flask(__name__)

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)
# in the above line html file will get 'posts' on the left, right one indicates the above list of dictionary.

@app.route("/about")
def about():
    return render_template('about.html', title='About')
# 'title' is variable which can be accessed by the html file

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes

- Flask uses jingia 2 to render the template
- Create a templates directory inside the project directory to store template files
- Create a static folder inside the project directory to store static files like css, js etc.

* A quick note on `url_for` is [tutorial point](https://www.tutorialspoint.com/flask/flask_url_building.htm "web content").

sources: [Corey Schafer Flask tutorial part 2](https://youtu.be/QnDWIZuWYW0?si=0sZW2bPp3dES2Urt "video tutorial")
