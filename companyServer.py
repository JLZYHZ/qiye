# encoding: utf-8
from flask import Flask,render_template
import config

app = Flask(__name__)
app.config.from_object(config)

#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/index.html')
# def index1():
#     return render_template('index.html')
#
# @app.route('/category.html')
# def category():
#     return render_template('category.html')
#
# @app.route('/about-us.html')
# def about():
#     return render_template('about-us.html')
#
# @app.route('/blog-home.html')
# def blogHome():
#     return render_template('blog-home.html')
#
# @app.route('/blog-single.html')
# def blogSingle():
#     return render_template('blog-single.html')
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
# @app.route('/elements.html')
# def elements():
#     return render_template('elements.html')
#
# @app.route('/price.html')
# def price():
#     return render_template('price.html')
#
# @app.route('/search.html')
# def search():
#     return render_template('search.html')
#
# @app.route('/single.html')
# def single():
#     return render_template('single.html')

@app.route('/')
def start():
    return render_template('category_showcompany.html')
    # return render_template('test.html')

@app.route('/category_showcompany.html')
def showcompany():
    return render_template('category_showcompany.html')

@app.route('/contact_demand.html')
def demand():
    return render_template('contact_demand.html')
if __name__ == '__main__':
    app.run(debug=True)
