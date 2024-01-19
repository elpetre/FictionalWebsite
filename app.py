from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('homepage.html')
@app.route('/products')
def products():
    return render_template('products.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact-us')
def contact_us():
    return render_template('contact-us.html')


if __name__ == '__main__':
    app.run(debug=True, port=3000)