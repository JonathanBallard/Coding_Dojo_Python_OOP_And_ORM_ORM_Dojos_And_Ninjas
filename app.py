# @prefix !!flasksqlalchemy
# @description 



from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy			# instead of mysqlconnection
from sqlalchemy.sql import func                         # ADDED THIS LINE FOR DEFAULT TIMESTAMP
from flask_migrate import Migrate			# this is new
app = Flask(__name__)
# configurations to tell our app about the database we'll be connecting to
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dojos_and_ninjas.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# an instance of the ORM
db = SQLAlchemy(app)
# a tool for allowing migrations/creation of tables
migrate = Migrate(app, db)




#### ADDING THIS CLASS ####
# the db.Model in parentheses tells SQLAlchemy that this class represents a table in our database



class Dojo(db.Model):	
    # __tablename__ = "users"    # optional		
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    city = db.Column(db.String(45))
    state = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())    # notice the extra import statement above
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())


class Ninja(db.Model):	
    # __tablename__ = "users"    # optional		
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(45))
    last_name = db.Column(db.String(45))
    dojo = db.Column(db.String(45))
    created_at = db.Column(db.DateTime, server_default=func.now())    # notice the extra import statement above
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())






# routes go here...

@app.route('/')
def index():

    list_of_ninjas = Ninja.query.all()
    list_of_dojos = Dojo.query.all()



    return render_template('index.html', ninjaList = list_of_ninjas, dojoList = list_of_dojos)


@app.route('/create_ninja', methods=['POST'])
def create_ninja():

    first_name = request.form['fname']
    last_name = request.form['lname']
    dojo = request.form['dojo']

    new_ninja = Ninja(first_name=first_name, last_name = last_name, dojo=dojo)
    db.session.add(new_ninja)
    db.session.commit()

    

    return redirect("/")


@app.route('/create_dojo', methods=['POST'])
def create_dojo():

    name = request.form['name']
    city = request.form['city']
    state = request.form['state']

    new_dojo = Dojo(name=name, city=city, state=state)
    db.session.add(new_dojo)
    db.session.commit()

    


    return redirect("/")








if __name__ == "__main__":
    app.run(debug=True)




















