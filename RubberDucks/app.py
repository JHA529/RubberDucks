from flask import Flask, render_template, request, session, redirect
import mysql.connector
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="orders_db"
)

def send_email(subject, message, recipient):
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_email_password'
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())

@app.route('/')
def index():
    # Fetch products from the database and render them on the webpage
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products")  # Replace 'products' with your table name
    products = cursor.fetchall()
    cursor.close()
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    # Add the selected product to the cart
    if 'cart' not in session:
        session['cart'] = {}
    if product_id in session['cart']:
        session['cart'][product_id] += 1
    else:
        session['cart'][product_id] = 1
    return redirect('/')

@app.route('/checkout')
def checkout():
    if 'cart' in session:
        cart = session['cart']
        cursor = db.cursor()
        for product_id, quantity in cart.items():
            cursor.execute("INSERT INTO orders (product_id, quantity, customer_email) VALUES (%s, %s, %s)",
                           (product_id, quantity, 'customer@example.com'))  # Replace with actual customer's email
        db.commit()
        cursor.close()

        # Send email confirmation
        send_email('Order Confirmation', 'Thank you for your order!', 'customer@example.com')  # Replace with actual customer's email

        # Clear the cart
        session.pop('cart', None)

    return render_template('checkout.html')

if __name__ == '__main__':
    app.run(debug=True)
