from datetime import datetime
from flask_login import UserMixin
from marshmallow_sqlalchemy import ModelSchema
from base import db, login_manager


@login_manager.user_loader
def load_user(admin_id):
    return Admin.query.get(int(admin_id))


# the model configuration of the database

class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    country = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    logged_in = db.Column(db.Boolean, default=False)
    auth_key= db.Column(db.String(),  unique=True)


class Satisfaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    agent = db.relationship('Agent', backref='ratings', lazy=True)
    apartment = db.relationship('Apartment', backref='comfort', lazy=True)
    rating = db.Column(db.Integer())
    sales = db.Column(db.Integer(), default=0)


class Agent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    country = db.Column(db.String(), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    dob = db.Column(db.String(), nullable=False)
    amount_earned = db.Column(db.Integer(), default=0)
    buildings_sold = db.Column(db.Integer(), default=0)
    date_employed = db.Column(db.String(), nullable=False)
    ssn = db.Column(db.Integer(), nullable=False)
    client = db.relationship('Client', backref='real_estate', lazy=True)
    clientSatisfaction = db.Column(db.Integer, db.ForeignKey('satisfaction.id'))
    sacked = db.Column(db.Boolean, default=False)


class Apartment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(), nullable=False)
    apartment_name = db.Column(db.String(), nullable=False)
    apartment_no = db.Column(db.Integer(), nullable=False)
    client = db.relationship('Client', backref='housing', lazy=True)
    sold_by = db.Column(db.String())
    purchased_by = db.Column(db.String())
    clientSatisfaction = db.Column(db.Integer, db.ForeignKey('satisfaction.id'))
    sold = db.Column(db.Boolean, nullable=False, default=False)


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    country = db.Column(db.String(), nullable=False)
    dob = db.Column(db.String(), nullable=False)
    phone_no = db.Column(db.Integer(), nullable=False)
    criminal_record = db.Column(db.Boolean, default=False)
    ssn = db.Column(db.Integer(), nullable=False)
    date_registered = db.Column(db.DateTime, nullable=False, default=datetime.now)
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.id'))
    apartment_id = db.Column(db.Integer, db.ForeignKey('apartment.id'))


# the schema configuration to convert the data in each table to json readable format
class AdminSchema(ModelSchema):
    class Meta:
        model = Admin


admin_schema = AdminSchema()
admins_schema = AdminSchema(many=True)


class AgentSchema(ModelSchema):
    class Meta:
        model = Agent


agent_schema = AgentSchema()
agents_schema = AgentSchema(many=True)


class ApartmentSchema(ModelSchema):
    class Meta:
        model = Apartment


apartment_schema = ApartmentSchema
apartments_schema = ApartmentSchema(many=True)


class ClientSchema(ModelSchema):
    class Meta:
        model = Client


client_schema = ClientSchema()
clients_schema = ClientSchema(many=True)
