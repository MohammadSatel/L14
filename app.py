from flask import Flask, render_template, request

app = Flask(__name__)

cart = []

product_list = [
    {"prod_name": "Eggs", "prod_price": 7.95},
    {"prod_name": "Milk", "prod_price": 3.75},
    {"prod_name": "Cheese", "prod_price": 7.95},
    {"prod_name": "Coffee", "prod_price": 5.25},
    {"prod_name": "Bread", "prod_price": 2.45}
]

links = [
    {"prod_name": "Cart", "url": "/cart"},
]

@app.route('/')
def homepage():
    return render_template('index.html', links=links, product_list=product_list)

@app.route('/cart', methods=['GET', 'POST'])
def view_cart():
    if request.method == 'POST':
        # Get the selected product name from the form
        selected_product_name = request.form.get('product_name')

        # Find the selected product in the product list
        selected_product = next((product for product in product_list if product['prod_name'] == selected_product_name), None)

        if selected_product:
            # Add the selected product to the cart
            cart.append(selected_product)

    return render_template('cart.html', links=links, cart=cart)

if __name__ == '__main__':
    app.run(debug=True)
