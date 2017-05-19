from app import app, db
from flask import render_template, request, redirect, url_for, flash
from forms import CreateUserForm 
from models import Users

import json

def algorithm(username):
    current_user= Users.query.filter_by(username=username).first()
    matches=[]
    count = 0

    for user in Users.query.all():
        if user.username == username:
            continue
        else:
            if current_user.f == user.gender:
                count+= 1

            if current_user.c == user.height:
                count += 1

            if current_user.r == 1 and user.userrel == 1 and current_user.r1 == user.userrelty:
                count ++ 1

            if current_user.a == user.age:
                count += 1

            if current_user.seeking_honesty == "True" and user.honesty == "True":
                count += 1

            if current_user.seeking_friendly == "True" and user.firendly == "True":
                count += 1

            if current_user.seeking_loyalty == "True" and user.loyalty == "True":
                count += 1

            if current_user.seeking_integrity == "True" and user.integrity == "True":
                count += 1

            if current_user.seeking_respectful == "True" and user.respectful == "True":
                count += 1

            if current_user.seeking_compassionate == "True" and user.compassionate == "True":
                count += 1

            if current_user.seeking_fair == "True" and user.fair == "True":
                count += 1

            if current_user.seeking_forgiving == "True" and user.forgiving == "True":
                count += 1

            if current_user.seeking_courageous == "True" and user.courageous == "True":
                count += 1

            if current_user.seeking_generous == "True" and user.generous == "True":
                count += 1

            if current_user.seeking_polite == "True" and user.polite == "True":
                count += 1

            if current_user.seeking_kind == "True" and user.kind == "True":
                count += 1

            if current_user.seeking_loving == "True" and user.loving == "True":
                count += 1

            if current_user.seeking_optimistic == "True" and user.optimistic == "True":
                count += 1

            if current_user.seeking_reliable == "True" and user.reliable == "True":
                count += 1

            if current_user.seeking_conscious == "True" and user.conscious == "True":
                count += 1
        if count > 10:
            matches.append(user)
    return matches

def Match():
    user_form = CreateUserForm()
    mymatch = []  
    
    username="JLONG" #should be removed 
    myname=username
    # thisUser= user_form.name.data
    user = Users.query.filter_by(username="")
    curuser = db.session.query(CreateUserForm).filter(CreateUserForm.username==myname).first() 
    #  curUser = db.session.query(User).all()
    users = db.session.query(CreateUserForm).all() # or you could have used User.query.all()
    
    currentUser = {"firstname": curuser.firstname, "lastname": curuser.lastname, "age":curuser.age,
    "skill": curuser.skill, "gender": curuser.gender, "height": curuser.height, 
     "religion": curuser.religion,
    
    "honesty": curuser.honesty, "friendly": curuser.friendly, "loyalty": curuser.loyalty,
    "respectful": curuser.respectful,"compassionate": curuser.compassionate, "fair": curuser.fair, 
    "forgiving": curuser.forgiving, "courageous": curuser.courageous, "generous": curuser.generous,
    "polite": curuser.polite, "kind": curuser.kind, "loving": curuser.loving, "optimistic": curuser.optimistic,
    "reliable": curuser.reliable, "conscious": curuser.conscious,
    
    "food": curuser.food, "sports": curuser.sports, "movies": curuser.movies, "exercising": curuser.exercising,
    "shopping": curuser.shopping, "music": curuser.music, "singing": curuser.singing, "dancing": curuser.dancing, 
    "reading": curuser.reading, "fashion": curuser.fashion, "pets": curuser.pets}

    # for user in curUser : 
        # currentUser= None 
    #     if user.name == myname: 
    #         currentUser=user 
    for user in users:
        # print user.skill 
        # print currentUser["skill"] 
        # if currentUser["skill"] == user.skill:
        
        if (currentUser["skill"] == user.skill and currentUser["education"] == user.education and 
            currentUser["gender"] == user.gender and currentUser["height"] == user.height and
            currentUser["religion"] == user.religion) :
                
            mymatch.append(user)
        
    # mymatch = [] 
    # print thisUser 
    # return render_template('match.html', mymatch=mymatch) 
    # return json.dumps(me, default=lambda x: None)
    return mymatch 
    

  