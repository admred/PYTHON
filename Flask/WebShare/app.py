#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from base64 import  *

from flask import Flask,request,abort,render_template,send_file,flash
from werkzeug.utils import secure_filename

app=Flask(__name__)

PATH="/tmp/files/"

@app.route('/',methods=['GET','POST'])
def index():
    if not os.path.exists(PATH):
        os.mkdir(PATH,mode=511)
        
    if request.method == 'POST':
        if "upload" in request.files:
            f=request.files['upload']
            fname=secure_filename(f.filename)
            f.save(os.path.join(PATH,fname))
    
    

    files=[ f for f in os.listdir(PATH) if f not in ['.','..']  ]

    return render_template('index.html',files=files )


@app.route('/<filename>')
def sendfile(filename):

    f=open(os.path.join(PATH,filename) ,"rb")
    
    return send_file(f,mimetype="") 
    

