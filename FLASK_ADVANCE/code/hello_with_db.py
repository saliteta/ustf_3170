from flask import render_template
from db import Item, app


'''
    The __name__ reference the name of python file you are working with

'''

@app.route('/') #decorator, will be excuated one step ahead of the function # / means the home page, or the default of the web page
@app.route('/home')
def home_page():
    return render_template('home_from_base.html')  # the return value should be HTML. Use hello world to dispaly


@app.route('/about')
def about_page():
    return "<h1>About</h1>"

'''
automatically creating a webpage
'''
@app.route('/user/<username>') #passing username as a parameter to the function
def user_page(username):
    # passing argument to the html pages
    return render_template('user.html', username = username)
    #using the Jinjia to get username

@app.route('/market') #passing username as a parameter to the function
def market_page():
    items = Item.query.all()
    return render_template('market_from_base.html', dict_item = items)
    #using the Jinjia to get dict_item
    #using the jinjia table to format dict_item


'''
    Using styling frame work, which is Bootstrap
'''