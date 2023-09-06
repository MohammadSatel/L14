from flask import Flask, render_template

app = Flask(__name__)

# Sample list of names and emails
user_data = [
    {"name": "User 1", "email": "user1@example.com"},
    {"name": "User 2", "email": "user2@example.com"},
    {"name": "User 3", "email": "user3@example.com"}
]

# Define a list of dictionaries for the links
links = [
    {"name": "Link 1", "url": "/page/1"},
]

@app.route('/')
def homepage():
    return render_template('index.html', links=links)

@app.route('/page/<int:page_num>')
def page(page_num):
    # Ensure that the page_num is within the valid range (1-1 for "page1")
    if page_num == 1:
        return render_template('page1.html', links=links, user_data=user_data)
    else:
        return "Page not found"

if __name__ == '__main__':
    app.run(debug=True)
