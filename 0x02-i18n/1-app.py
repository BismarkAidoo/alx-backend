#!/usr/bin/env python3
"""Module containing Flask app with Babel integration"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Class that defines Babel instance attributes"""

    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def root():
    """Function defining route to html template"""

    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()