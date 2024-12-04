from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog_full_width')
def blog_full_width():
    return render_template('blog_full_width.html')

@app.route('/blog_left')
def blog_left():
    return render_template('blog_left.html')

@app.route('/blog_right')
def blog_right():
    return render_template('blog_right.html')

@app.route('/blog_detail')
def blog_detail():
    return render_template('blog-detail.html')

@app.route('/category_one_ori')
def category_one_ori():
    return render_template('category_one_ori.html')

@app.route('/category_one')
def category_one():
    return render_template('category_one.html')

@app.route('/category_three')
def category_three():
    return render_template('category_three.html')

@app.route('/category_two')
def category_two():
    return render_template('category_two.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/home_02')
def home_02():
    return render_template('home-02.html')

@app.route('/home_03')
def home_03():
    return render_template('home-03.html')

@app.route('/product_detail')
def product_detail():
    return render_template('product-detail.html')

@app.route('/shopping_cart')
def shopping_cart():
    return render_template('shopping-cart.html')

if __name__ == '__main__':
    app.run(debug=True)