from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func 

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    

class Teaching_Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    qualification = db.Column(db.String(100))
    academic_rank = db.Column(db.String(50))
    department = db.Column(db.String(50))
    phone = db.Column(db.String(20), unique=True)

class Non_Teaching_Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    qualification = db.Column(db.String(100))
    assigned_duty = db.Column(db.String(50))
    phone = db.Column(db.String(20), unique=True)

class Programmes_Fees(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    programme = db.Column(db.String(50), unique=True)
    fees = db.Column(db.Integer)
    graduation = db.Column(db.String(5))

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_title = db.Column(db.String(50), unique=True)
    event_description = db.Column(db.String(5000))
    image_filename = db.Column(db.String(50))

class Downloads(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_name = db.Column(db.String(50))
    file_name = db.Column(db.String(50))
    #title_name = db.Column(db.String(50), nullable=False)

class IQAC(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    category = db.Column(db.String(50))
    designation = db.Column(db.String(50))

class UG_Programmes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    programme = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    marital_status = db.Column(db.String(10), nullable=False)
    parent_name = db.Column(db.String(50), nullable=False)
    parent_relation = db.Column(db.String(50), nullable=False)
    parent_occupation = db.Column(db.String(50), nullable=False)
    parent_income = db.Column(db.Integer, nullable=False)
    permanent_address = db.Column(db.String(100), nullable=False)
    p_pinode = db.Column(db.String(10), nullable=False)
    p_contact = db.Column(db.String(50), nullable=False)
    residential_address = db.Column(db.String(100), nullable=True)
    r_pincode = db.Column(db.String(10), nullable=True)
    r_contact = db.Column(db.String(50), nullable=True)

class PG_Programmes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    programme = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    phone = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    dob = db.Column(db.Date, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    marital_status = db.Column(db.String(10), nullable=False)
    parent_name = db.Column(db.String(50), nullable=False)
    parent_relation = db.Column(db.String(50), nullable=False)
    parent_occupation = db.Column(db.String(50), nullable=False)
    parent_income = db.Column(db.Integer, nullable=False)
    permanent_address = db.Column(db.String(100), nullable=False)
    p_pinode = db.Column(db.String(10), nullable=False)
    p_contact = db.Column(db.String(50), nullable=False)
    residential_address = db.Column(db.String(100), nullable=True)
    r_pincode = db.Column(db.String(10), nullable=True)
    r_contact = db.Column(db.String(50), nullable=True)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(5000), nullable=False)