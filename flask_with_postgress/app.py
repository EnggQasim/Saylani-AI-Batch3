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