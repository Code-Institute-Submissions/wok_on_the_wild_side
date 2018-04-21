import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from config import mongo_uri
from flask_uploads import UploadSet, configure_uploads, IMAGES


app = Flask(__name__)
photos = UploadSet('photos', IMAGES)
app.config['UPLOADED_PHOTOS_DEST'] = 'static/file_uploads'
configure_uploads(app, photos)
app.config["MONGO_DBNAME"] = 'wok_on_the_wild_side'
app.config["MONGO_URI"] = mongo_uri
mongo = PyMongo(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    selection = request.form.get('filter_by')
    if selection == "time":
        _recipes = mongo.db.recipes.find().sort("c_time")
    elif selection == "cuisine":
        _recipes = mongo.db.recipes.find().sort("cuisine")
    elif selection == "name":
        _recipes = mongo.db.recipes.find().sort("dish_name")
    else:
        _recipes = mongo.db.recipes.find()
    return render_template("index.html",
    recipes=_recipes)


@app.route('/contribute', methods=['GET', 'POST'])
def contribute():
    _cuisines = mongo.db.cuisines.find()
    cuisine_list = [cuisine for cuisine in _cuisines]
    return render_template("contribute.html", cuisines=cuisine_list)

@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipes
    if request.method == 'POST' and 'photo' in request.files:
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
        "photo": str(filename)
        }
        recipes.insert_one(new_recipe)
        return redirect(url_for('index'))
    return render_template("contribute.html")

@app.route('/view_recipe/<recipe_id>')
def view_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("view_recipe.html",
    recipe=the_recipe)
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    _cuisines = mongo.db.cuisines.find()
    return render_template('edit_recipe.html', recipe=the_recipe, cuisines=_cuisines)

@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipes
    recipes.update(
    { '_id': ObjectId(recipe_id)},
        {
            "$set": {
            "dish_name": request.form.get('dish_name'),
            "descr": request.form.get('descr'),
            "ingr": request.form.getlist('ingr'),
            "step": request.form.getlist('step'),
            "c_time": request.form.get('c_time'),
            "serves": request.form.get('serves'),
            "cuisine": request.form.get('cuisine'),
            "author": request.form.get('author')
            }
        }
    )
    return redirect(url_for('index'))
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('index'))

@app.route('/edit_photo/<recipe_id>')
def edit_photo(recipe_id):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template('edit_photo.html', recipe=the_recipe)

@app.route('/update_photo/<recipe_id>', methods=['POST'])
def update_photo(recipe_id):
    recipes = mongo.db.recipes
    filename = photos.save(request.files['photo'])
    recipes.update(
    { '_id': ObjectId(recipe_id)},
        {
            "$set": {
            "photo": str(filename)
            }
        }
    )
    return redirect(url_for('index'))
    
@app.route('/add_cuisine')
def add_cuisine():
    return render_template("add_cuisine.html")

@app.route('/view_cuisine')
def view_cuisine():
    return render_template("view_cuisine.html")    
    
@app.route('/edit_cuisine')
def edit_cuisine():
    return render_template("edit_cuisine.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)