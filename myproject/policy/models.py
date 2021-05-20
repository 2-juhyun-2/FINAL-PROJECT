from policy import db
from datetime import datetime

class User(db.Model):
	""" Create user table"""
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(150), unique=True, nullable=False)
	password = db.Column(db.String(200), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	
	

	# def __init__(self, username, password):
	# 	self.username = username
	# 	self.password = password

