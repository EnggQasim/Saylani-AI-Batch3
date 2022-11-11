# Flask App deployment
# Create Flask App
    * app.py
```
from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
filename='static/finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/model",  methods=['post'])
def model():
    result = np.int64(request.form['height'])
    result = loaded_model.predict([[result]])[0]
    return f"<h1>Dear Customers your predicted weight is <span style='color:red'>{result}</span></h1>"
   

if __name__ == '__main__':
    app.run(debug=True)
```

* Create **Procfile** file
<pre>       appname:app_instance variable(in app.py)</pre>

* `pip freeze > requirement.txt`
* git command
```
git init
git commit -m "message"
heroku login
heroku git:remote -a HeroKuAppName
git push heroku master 
```
`web: gunicorn app:app`
* Create Heroku Account
    * Heroku cli download and install
        * Install git
        *  `heroku login`
