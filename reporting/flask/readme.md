https://flask-restful.readthedocs.io/en/latest/


https://flask.palletsprojects.com/en/2.2.x/quickstart/
https://code.visualstudio.com/docs/python/tutorial-flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

So what did that code do?
First we imported the Flask class. An instance of this class will be our WSGI application.
Next we create an instance of this class. The first argument is the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.

We then use the route() decorator to tell Flask what URL should trigger our function.

The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.

Save it as hello.py or something similar. Make sure to not call your application flask.py because this would conflict with Flask itself.

To run the application, use the flask command or python -m flask. You need to tell the Flask where your application is with the -app option.

$ flask --app hello run
 * Serving Flask app 'hello'
 * Running on http://127.0.0.1:5000 (Press CTRL+C to quit)

 A general utility script for Flask applications.

  Provides commands from Flask, extensions, and the application. Loads the
  application defined in the FLASK_APP environment variable, or from a wsgi.py
  file. Setting the FLASK_ENV environment variable to 'development' will
  enable debug mode.


    $ export FLASK_APP=hello.py
    $ export FLASK_ENV=development
    $ flask run
If you want to use a different filename than app.py, such as program.py, define an environment variable named FLASK_APP and set its value to your chosen file. Flask's development server then uses the value of FLASK_APP instead of the default file app.py. For more information, see Flask command line interface.

    if you call the app.py then you can just type 'flask run'

Options:
  --version  Show the flask version
  --help     Show this message and exit.

Commands:
  routes  Show the routes for the app.
  run     Run a development server.


https://code.visualstudio.com/docs/python/tutorial-flask

