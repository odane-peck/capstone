from . import db
from time import time
from datetime import date
from flask import json, jsonify
class Users(db.Model):
	
	
	person_id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(80))
	last_name = db.Column(db.String(80))
	username = db.Column(db.String(80), unique=True)
	password = db.Column(db.String(80))
	gender = db.Column(db.String(10))
	age = db.Column(db.Integer)
	height = db.Column(db.String(80))
	profile_photo = db.Column(db.String(80))
	date_created = db.Column(db.String(30))
	bio = db.Column(db.String(250))
	country = db.Column(db.String(80))
	origin = db.Column(db.String(80))
	professional = db.Column(db.String(80))
	school = db.Column(db.String(80))
	userrel = db.Column(db.String(80))
	userrelty = db.Column(db.String(80))
	
	honesty = db.Column(db.String(80))
	firendly = db.Column(db.String(80))
	loyalty = db.Column(db.String(80))
	integrity = db.Column(db.String(80))
	respectful = db.Column(db.String(80))
	compassionate = db.Column(db.String(80))
	fair = db.Column(db.String(80))
	forgiving = db.Column(db.String(80))
	courageous = db.Column(db.String(80))
	generous = db.Column(db.String(80))
	polite = db.Column(db.String(80))
	kind = db.Column(db.String(80))
	loving = db.Column(db.String(80))
	optimistic = db.Column(db.String(80))
	reliable = db.Column(db.String(80))
	conscious = db.Column(db.String(80))
	
	f = db.Column(db.String(80))
	c = db.Column(db.String(80))
	r1 =db.Column(db.String(80))
	a = db.Column(db.String(80))

	seeking_honesty = db.Column(db.String(80))
	seeking_firendly = db.Column(db.String(80))
	seeking_loyalty = db.Column(db.String(80))
	seeking_integrity = db.Column(db.String(80))
	seeking_respectful = db.Column(db.String(80))
	seeking_compassionate = db.Column(db.String(80))
	seeking_fair = db.Column(db.String(80))
	seeking_forgiving = db.Column(db.String(80))
	seeking_courageous = db.Column(db.String(80))
	seeking_generous = db.Column(db.String(80))
	seeking_polite = db.Column(db.String(80))
	seeking_kind = db.Column(db.String(80))
	seeking_loving = db.Column(db.String(80))
	seeking_optimistic = db.Column(db.String(80))
	seeking_reliable = db.Column(db.String(80))
	seeking_conscious = db.Column(db.String(80))

	traveling = db.Column(db.String(80))
	food = db.Column(db.String(80))
	sports = db.Column(db.String(80))
	movies = db.Column(db.String(80))
	exercsing = db.Column(db.String(80))
	shopping = db.Column(db.String(80))
	music = db.Column(db.String(80))
	singing= db.Column(db.String(80))
	dancing = db.Column(db.String(80))
	reading = db.Column(db.String(80))
	fashion = db.Column(db.String(80))
	pets = db.Column(db.String(80))

	def _init_(self, first_name, last_name, username, password, age, height, gender, 
	profile_photo, school, professional, origin, country, honesty, userrel,friendly,
	loyalty, integrity, respectful, compassionate, fair, forgiving, courageous, generous, 
	kind, loving, optimistic, reliable, fashion, sporst, conscious, exercsing, dancing, f, c, r1, a, 
	movies, food, reading, excercising, shopping, music, singing, pets, traveling):
		
		self.person_id = int(Users.returnID())
		self.first_name = first_name
		self.last_name  = last_name
		self.username = username
		self.password = password
		self.age = age
		self.gender = gender
		self.profile_photo = profile_photo
		self.date_created = Users.timeinfo()
		self.bio = bio
	
	@staticmethod
	def returnID():
		new_id = long(time())
		return new_id
	
	@staticmethod
	def timeinfo():
		"""Forats the date and time"""
		d = date.today();
		return "{0:%A}, {0:%B} {0:%d}, {0:%y}".format(d)
	
	def _repr_(self):
		return '<User %r>' % (self.username)

	def get_image_url(self):
		return '/uploads/{0}'.format(self.image)
	
	def toJSON(self):
		return jsonify(username = self.username, userid = self.id)