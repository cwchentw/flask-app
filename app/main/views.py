import os
from flask import render_template, send_from_directory
from . import main

@main.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico')

@main.route('/')
def index():
    return render_template('index.html')
