import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from config import mongo_uri
from flask_uploads import UploadSet, configure_uploads, IMAGES
from wtforms import Form, BooleanField, StringField, validators, IntegerField, SelectField


app = Flask(__name__)
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/file_uploads'
configure_uploads(app, photos)
app.config["MONGO_DBNAME"] = 'wok_on_the_wild_side'
app.config["MONGO_URI"] = mongo_uri
mongo = PyMongo(app)



class FormValidation(Form):
    v_dish_name = StringField('dish_name', 
        [
            validators.Length(min=4, message=(u'Not enough characters.')),
            validators.InputRequired(message=(u'Input required'))
        ])
    v_descr = StringField('descr', 
        [
            validators.Length(min=4, message=(u'Not enough characters.')),
            validators.InputRequired(message=(u'Input required'))
        ])
    v_ingr = StringField('ingr', 
        [
            validators.Length(min=4, message=(u'Not enough characters.')),
            validators.InputRequired(message=(u'Input required'))
        ])
    v_step = StringField('step', 
        [
            validators.Length(min=4, message=(u'Not enough characters.')),
            validators.InputRequired(message=(u'Input required'))
        ])
    v_c_time = IntegerField('c_time', 
        [
            validators.NumberRange(min=5, max=180, message=(u'Minimum time: 5mins, Maximum time: 180mins')),
            validators.InputRequired(message=(u'Input required'))
        ])
    v_serves = SelectField('serves', 
        [
            validators.NumberRange(min=1, max=8, message=(u'Minimum time: 5mins, Maximum time: 180mins')),
            validators.InputRequired(message=(u'Input required'))
        ])
    v_cuisine = SelectField('cuisine', 
        [
            validators.Length(min=4, message=(u'Not enough characters.')),
            validators.InputRequired(message=(u'Input required'))
        ])
    v_author = StringField('author', 
        [
            validators.Length(min=4, message=(u'Not enough characters.')),
            validators.InputRequired(message=(u'Input required'))
        ])


@app.route('/')
def index():
    return render_template("index.html",
    recipes=mongo.db.recipes.find())

@app.route('/contribute', methods=['GET', 'POST'])
def contribute():
    _cuisines = mongo.db.cuisines.find()
    cuisine_list = [cuisine for cuisine in _cuisines]
    return render_template("contribute.html", cuisines=cuisine_list)

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    form = FormValidation(request.form)
    if request.method == 'POST' and form.validate() and 'photo' in request.files:
        ### File upload
        filename = photos.save(request.files['photo'])
        new_recipe = {
        "dish_name": request.form.get('dish_name'),
        "descr": request.form.get('descr'),
        "ingr": request.form.getlist('ingr'),
        "step": request.form.getlist('step'),
        "c_time": request.form.get('c_time'),
        "serves": request.form.get('serves'),
        "cuisine": request.form.get('cuisine'),
        "author": request.form.get('author'),
        "file_name": str(filename)
        }
        recipes.insert_one(new_recipe)
        return redirect(url_for('contribute', form=form))
    return render_template("index.html")
    

@app.route('/view_recipe/<recipe_id>')
def viewRecipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html",
    recipe=the_recipe)

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