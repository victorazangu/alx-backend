# 0x0A. i18n

## Description
What you should learn from this project:

---

### [0. Basic Flask app](./0-app.py)
* First you will setup a basic Flask app in 0-app.py. Create a single / route and an index.html template that simply outputs “Welcome to Holberton” as page title (<title>) and “Hello world” as header (<h1>).


### [1. Basic Babel setup](./1-app.py)
* Install the Babel Flask extension:


### [2. Get locale from request](./2-app.py)
* Create a get_locale function with the babel.localeselector decorator. Use request.accept_languages to determine the best match with our supported languages.


### [3. Parametrize templates](./3-app.py)
* Use the _ or gettext function to parametrize your templates. Use the message IDs home_title and home_header.


### [4. Force locale with URL parameter](./4-app.py)
* In this task, you will implement a way to force a particular locale by passing the locale=fr parameter to your app’s URLs.


### [5. Mock logging in](./5-app.py)
* Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in 5-app.py.


### [6. Use user locale](./6-app.py)
* Change your get_locale function to use a user’s preferred local if it is supported.


### [7. Infer appropriate time zone](./7-app.py)
* Define a get_timezone function and use the babel.timezoneselector decorator.

---

## Author
* **Felipe Satizabal** - [felipesv](https://github.com/felipesv)