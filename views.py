# -*- coding: utf-8 -*-
from flask import render_template, url_for, redirect, request 
from myapp import app 
@app.route('/')
def index():
    return render_template('index.html')


