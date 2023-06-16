#!/usr/bin/env python3
""" App """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """ Return a template """
    return render_template('0-index.html')
