# WokOnTheWildSide - Project 3

## Getting Started

This web app allows users to store and access cooking recipes (submitted by themselves and other users). 

The home page shows all the recipes which allows the user to filter by Cooking time, Recipe name and Cuisine. 
From here, they can view each recipe for more details such as the ingredients, cooking instructions and the author. 
From this screen, they have the option to edit the recipe, change the photo or delete the recipe. 
From the home page, they also have the option to submit their own recipe.

This has been written using HTML, CSS, JavaScript and Python. 
The recipe data is all stored in MongoDB. 
Pagaination has been created and used to minimise the need to scroll down the page to see the list of recipes. 
I've used Materialize for certain components and for a responsive view.

### Prerequisites

Some the tech used includes:

- [Flask](http://flask.pocoo.org/)
    - I used **Flask** (which is a python microframework) to render pages and manage the functionality.
- [materialize](https://materializecss.com/)
    - I used **Bootstrap** to give my project a simple, responsive layout.
- [npm](https://www.npmjs.com/)
    - I used **npm** to help manage some of the dependencies in our application.
- [gulp](https://gulpjs.com/)
    - **Gulp** is used to manage the tasks of running the scss and moving files from Node Modules to my project folders.
- [font-awesome](http://fontawesome.io/)
    - I used **font-awesome** to include images for icons.
- [Google Fonts](https://fonts.google.com/) 
    - **Google Fonts** is used to style the text in my site.

## WireFrame

Click [here](wireframe.pdf) to view the wireframe of this project.

## To initilise and edit

1. Download Python 3: (http://www.python.org/download/)

2. Clone the repository 

``` $ git clone https://github.com/DeanFlint/wok_on_the_wild_side.git```

3. Move into the folder

``` cd wok_on_the_wild_side ```

4. After you've that you'll need to make sure that you have **npm** installed. You can get **npm** by installing Node from [here](https://nodejs.org/en/)

``` $ npm install ```

``` $ npm start ```


5. Create and activate your virtual env:

``` $ python -m venv env ```

``` $ source env/Scripts/activate ```

6. Install requirements with pip:

``` (env)$ pip install -r requirements.txt ```

7. Run the python file:

``` python app.py ```

End with an example of getting some data out of the system or using it for a little demo

## Testing

### Break down into end to end tests

Explain what these tests test and why

```
TO DO
```

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Dean Flint** - *Initial work* - [Dean Flint](https://github.com/DeanFlint)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* The good people at CodeInstitute!

* Derek Hyland
