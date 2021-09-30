'''
    WebShare

    Copyright (C) 2021 Luciano A.

    WebShare is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    WebShare program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with WebShare.  If not, see <https://www.gnu.org/licenses/>.
'''
""" 
    TLDR; i need to share files over LAN
"""

import os
import sys
from flask import Flask,request,abort,render_template,send_file

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        f=request.files['file']
        f.save(f.filename)

    files=[ f.decode('utf-8') for f in os.listdir('.') ]
    for f in ['templates','app.py','app.pyc']:
        files.remove(f)

    return render_template('index.html',files=files )


@app.route('/<filename>')
def sendfile(filename):
    return send_file(open(filename,'rb'),mimetype="")
    

app.run(host='0.0.0.0')

