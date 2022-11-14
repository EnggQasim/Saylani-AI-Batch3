# Flask App with Postgress DB (Signup and Login)
## Create Virtual Evornment
* `python -m venv <cust_name>`
    * Windows OS
        * `.\<cus_name>\Scripts\activate`
    * Lunux
        * `source <cust_name>/bin/activate`
* install packages in **<cust_name>**
    * `pip install flask numpy pandas gunicorn sqlalchemy flask-sqlalchemy psycopg2`

* **Create app.py**
```
from flask import Flask, render_template, url_for, request, jsonify,redirect,flash
from flask_sqlalchemy import SQLAlchemy
import psycopg2
app = Flask(__name__)

#conectivity with PostGress
app.config['SECRET_KEY'] = 'thisissecret'
# our database uri
hostname = "ec2-35-170-21-76.compute-1.amazonaws.com"
username = "qrbjotiddjbmqh"
password = "e4cc25f86d04ff58512826b37f1f460f984c71ea33f19bee6ed4d126e85b6c3f"
dbname = "d2fr0p812tjnco"
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://qrbjotiddjbmqh:e4cc25f86d04ff58512826b37f1f460f984c71ea33f19bee6ed4d126e85b6c3f@ec2-35-170-21-76.compute-1.amazonaws.com:5432/d2fr0p812tjnco"


# ://[username]:[password]@[host name]/[db name]

app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{username}:{password}@{hostname}:5432/{dbname}"
print(f"postgresql://{username}:{password}@{hostname}:5432/{dbname}")


db = SQLAlchemy(app)

# Create A Model For Table
class BlogPosts(db.Model):
    __tablename__ = 'blogposts'
    id = db.Column(db.Integer, primary_key=True)
    blog_title = db.Column(db.String(1000))
    blog_description = db.Column(db.String(6000))






@app.route("/")
def index():
    posts = BlogPosts.query.all()
    return render_template("index.html",posts=posts)
    

@app.route("/user_signup", methods=['post'])    
def signup():
    name = request.form['user_name']
    email = request.form['email']
    password = request.form['psw']

    return f'Dear {name} Welcome in our AI class<br>Your email {email}'

@app.route('/posts',methods=['GET','POST'])
def add_posts():
    if request.method == 'POST':
        blog_title  = request.form['blog_title']
        blog_description  = request.form['blog_description']
        blog_post = BlogPosts(blog_title=blog_title,blog_description=blog_description)
        db.session.add(blog_post)
        db.session.commit()
        flash("Post Added")
    return redirect(url_for('index'))



if __name__ == '__main__':
    with app.app_context():
        db.create_all() # <--- create db object.
    app.run(debug=True)
```

### Create templates/index.html
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.4.1/dist/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>

</head>
<body>
<div class="container-fluid">
    <form action="{{ url_for('signup') }}" method="post">
        <div class="form-group">
          <label for="exampleInputEmail1">User Name</label>
          <input type="text" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="User name" name="user_name">
          <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
        </div>
        <div class="form-group">
            <label for="exampleInputEmail1">Email address</label>
            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email" name="email">
            <small id="emailHelp" class="form-text text-muted">We'll never share your email with anyone else.</small>
          </div>
        <div class="form-group">
          <label for="exampleInputPassword1">Password</label>
          <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password" name="psw">
        </div>
        
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>   


      <div>
        PSQL Flask
    </div>
    <div>
        <form action="{{url_for('add_posts')}}" method="POST">
            <input type="text" name="blog_title" placeholder="Blog Title">
            <textarea name="blog_description"></textarea>
            <button type="submit">Submit</button>
        </form>
    </div>

    <hr/>
    <div>
        {% for p in posts %}
        <ul>
            <li>{{p.blog_title}}</li>
            <li>{{p.blog_description}}</li>
        </ul>
        {% endfor %}
    </div>
</div>

    
</body>
</html>
```