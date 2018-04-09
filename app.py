import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
"""from config import mongo_uri"""

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contribute')
def contribute():
    return render_template("contribute.html")

@app.route('/view_recipe')
def viewRecipe():
    return render_template("view_recipe.html")
    
@app.route('/edit_recipe')
def editRecipe():
    return render_template("edit_recipe.html") 
    
@app.route('/add_cuisine')
def addCuisine():
    return render_template("add_cuisine.html")

@app.route('/view_cuisine')
def viewCuisine():
    return render_template("view_cuisine.html")    
    
@app.route('/edit_cuisine')
def editCuisine():
    return render_template("edit_cuisine.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)