import os
from datetime import date
from forms import CreateUserForm
from app import app, models, forms, db
from models import Users 
from match import algorithm 
from werkzeug.utils import secure_filename
from flask import render_template, request, redirect, url_for, flash, session, abort, jsonify, send_from_directory, session,make_response
from sqlalchemy.sql import exists
from werkzeug.wsgi import SharedDataMiddleware
#import alg#

#@app.route(/matched profiles?)
# def Matchprofile():
	# pass current user profile to algorithm
	
	#matched_users = [('username1', 'photo.jpg', '98%'), ('username2', 'photo2.jpg', '52%'), ('username3', 'photo3.jpg', '96%')]
	#return render_template('template.html', users=matched_users)

# @app.route('/api/api/route/database')
# def view():

@app.route('/map')
def geomap():
	return render_template('map.html')
@app.route('/api/profile')
def profiler():
	form = ProfileInfo()
	return render_template('ProfileInfo.html', form = form)
	
@app.route('/')
def home():
	form = CreateUserForm()
	return render_template('home.html')

@app.route('/profile', methods=['POST', 'GET'])
@app.route('/profile/<username>', methods = ['GET'])
def profile(username = None):
	form = CreateUserForm()
	user = None
	if request.method == 'POST':
		username = form.username.data
		if not db.session.query(exists().where(Users.username == username)).scalar():
			gender_type = form.gender.data + '.png'

			user = Users(first_name = form.firstname.data, last_name = form.lastname.data, 
				username = username, password = form.password.data, age = form.age.data, 
				gender = form.gender.data, profile_photo = gender_type, bio = form.bio.data, 
				country=form.country.data, origin=form.origin.data, height=form.height.data, 
				professional=form.professional.data, userrel=form.userrel.data, userrelty = form.userrelty.data, 
				honesty=form.honesty.data, firendly=form.friendly.data, loyalty=form.loyalty.data, 
				integrity=form.integrity.data, respectful=form.respectful.data, 
				compassionate=form.compassionate.data, fair=form.fair.data, forgiving=form.forgiving.data, 
				courageous=form.courageous.data, polite=form.polite.data, kind=form.kind.data, 
				loving=form.loving.data, optimistic=form.optimistic.data, reliable=form.reliable.data, 
				conscious=form.conscious.data)

			filefolder = app.config["UPLOAD_FOLDER"]
			file = request.files['image']
			if file and validate_file(file.filename):
				filename = secure_filename(file.filename)
				filename = '{0}.{1}'.format(user.username,filename.split('.')[-1])
				file.save(os.path.join(filefolder, filename))
				user.profile_photo = filename

			user.f = form.f.data
			user.c = form.c.data
			user.r = form.r.data
			user.r1 = form.r1.data
			user.a = form.a.data

			user.seeking_honesty = form.seeking_honesty.data
			user.seeking_friendly = form.seeking_friendly.data
			user.seeking_loyalty = form.seeking_loyalty.data
			user.seeking_integrity = form.seeking_integrity.data
			user.seeking_respectful = form.seeking_respectful.data
			user.seeking_compassionate = form.seeking_compassionate.data   
			user.seeking_fair = form.seeking_fair.data       
			user.seeking_courageous = form.seeking_courageous.data      
			user.seeking_generous  = form.seeking_generous.data       
			user.seeking_polite    = form.seeking_polite.data
			user.seeking_kind      = form.seeking_kind.data
			user.seeking_loving     = form.seeking_loving.data
			user.seeking_optimistic = form.seeking_optimistic.data
			user.seeking_reliable   = form.seeking_reliable.data
			user.seeking_conscious  = form.seeking_conscious.data
			
			user.traveling	= form.traveling.data
			user.food		= form.food.data
			user.sports	    = form.sports.data
			user.movies     = form.movies.data
			user.exercising = form.exercising.data
			user.shopping   = form.shopping.data
			user.music   = form.music.data
			user.singing = form.singing.data
			user.dancing = form.dancing.data
			user.reading = form.reading.data                 
			user.fashion = form.fashion.data         
			user.pets    = form.pets.data

			db.session.add(user)
			db.session.commit()

			matches = algorithm(username=user.username)
			if not matches == []:
				print matches
			else:
				print "No matches"

			return redirect(url_for('home'))
			
			# return render_template('ProfileInfo.html', form = form, user=user)
		else:
			flash('Username already in use.', 'danger')
			return render_template('form.html', form = form)
	elif username:
		user = Users.query.filter_by(username=username).first()
		return render_template('profile.html', user = user)
	return render_template('form.html', form = form)
	
@app.route('/profileinfo', methods=['POST'])
def profile_info():
	form=ProfileInfo()
	if request.method == "POST":
		username = request.form.username
		user = Users.query.filter_by(username=username).first()
		
		user.f = form.f.data
		user.c = form.c.data
		user.r = form.r.data
		user.r1 = form.r1.data
		user.a = form.a.data
		user.honesty = form.honesty.data
		user.friendly = form.friendly.data
		user.loyalty = form.loyalty.data
		user.integrity = form.integrity.data
		user.respectful = form.respectful.data
		user.compassionate = form.compassionate.data   
		user.fair = form.fair.data       
		user.courageous = form.courage.data      
		user.generous  = form.generous.data       
		user.polite    = form.polite.data
		user.kind      = form.kind.data
		user.loving     = form.loving.data
		user.optimistic = form.optimistic.data
		user.reliable   = form.reliable.data
		user.conscious  = form.conscious.data
		
		user.traveling	= form.traveling.data
		user.food		= form.food.data
		user.sports	    = form.sports.data
		user.movies     = form.movies.data
		user.exercising = form.exercising.data
		user.shopping   = form.shopping.data
		user.music   = form.music.data
		user.singing = form.singing.data
		user.dancing = form.dancing.data
		user.reading = form.reading.data                 
		user.fashion = form.fashion.data         
		user.pets    = form.pet.data  
	    
		db.session.add(user)
		db.session.commit()

		return redirect(url_for(profile))
		
		
	

def validate_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

def display_profile():
	if 'username' in session:
		return redirect(url_for('profile'), username = session['username'])
	return redirect(url_for('home'))
	
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate_on_submit():
        return redirect(url_for('home'))
        form = LoginForm() 
        if form.username.data:
            # Get the username and password values from the form.
            username=form.username.data
            password=form.password.data 
            # using your model, query database for a user based on the username
            # and password submitted
            # store the result of that query to a `user` variable so it can be
            # passed to the login_user() method.
            user = UserProfile.query.filter_by(username = username, password=password).first()
        if user is not None:
            # get user id, load into session
            login_user(user)

            # remember to flash a message to the user
            flash("Successful Login")
            
            return redirect(url_for("profile")) # they should be redirected to a secure-page route instead
        else:
            flash("Password or Username incorrcet.", "danger")
        return render_template("login.html", form=form)


@app.route("/profiles", methods = ['GET'] )
def profiles():
	# users = Users.query.all()
	user=db.session.query(Users).filter(first_name="Javoun").first() 
	print user
	# match = []
	
	# for user in users:
	# 	matching statements with user as param
	# 	if match leve good: 
	# 		match.append(user)
	"""Render the website profile page"""
	return render_template("profiles.html", users = users)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response

@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404

def timeinfo():
	date.today()
	return "Today's date is {0:%a}, {0:%d} {0:%b} {0:%y}".format(d)

# @app.route('/api/all') 
# def JSONcall():
# 	users 					= Users.query.all()
# 	ls 						= []
# 	jSON					= {}
# 	for user in users:
# 		jSON['username'] 	= user.username 
# 		jSON['userid'] 		= user.person_id
# 		ls 					= ls + [jSON]
# 		jSON 				= {}
	
# 	return jsonify({'users' : ls})

@app.route('/logout')
def logout():
	pass

@app.route('/match')
def match():
	mymatch=Match()
	
	render_template('match.html, mymatch=mymatch')
	
@app.route('/api/<username>')
def userJSON(username = None):
	users = Users.query.all()
	if not username:
		return render_template('404.html'), 404
	for user in users:
		if user.username == username:
			gender = "Female"
			if user.gender == 1:
				gender = "Male"
			jSON = {
				"userid"			: user.person_id,
				"username"			: user.username,
				"image"				: user.profile_photo,
				"gender"			: gender,
				"age"				: user.age,
				"profile_created_on": user.date_created
			} 
			return jsonify(jSON)
	return "User Not Found"

			
			
@app.route('/uploads/<filename>')
def uploaded_file(filename):
	return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

app.add_url_rule('/uploads/<filename>', 'uploaded_file', build_only=True)
app.wsgi_app = SharedDataMiddleware(app.wsgi_app, { '/uploads':  app.config['UPLOAD_FOLDER'] })

if __name__ == '__main__':
	app.run(debug=True,host="0.0.0.0",port="8081")

