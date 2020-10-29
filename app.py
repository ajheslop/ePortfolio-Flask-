from flask import Flask, render_template, url_for # url for helps with the linking of dynamic pages
app = Flask(__name__)

# url for("index")----> /
# url_for("names")----> /names
# url_for("home_name", name="Alan") ----> /home/Alan

# user the app.route decorator to define a route/endpoint
@app.route('/')
def Users():
    return render_template('index.html', title='Home', users=users)


# create another page
# using for loops in the html
@app.route('/user', methods=['GET'])
def user():
    posts =[{'title': 'Technology in 2020', 'author': 'Alan'},
    {'title': 'expansion of oil', 'author': 'bob'}]
    return render_template('user.html', user=user, sunny=False, posts=posts)

# this is known as a "dictionary"-it contains information about the users
# principle is like a database

users = {
    "Alan": {
        "name": "Alan Heslop",
        "bio": "Attending University of Sunderland, and also workds for DXC",
        "twitter_handle": "@AlanHeslop"
    },
    "Kieran": {
        "name": "Kieran Clayton",
        "bio": "Enjoys Climbing and Football",
        "twitter_handle": "@Kieran"
    },
    "Rachael": {
        "name": "Rachael Atkinson",
        "bio": "Works at an energy Callcentre.",
        "twitter_handle": "@Rachy"
    }
}


# create a route
# create a function
# create a return render_template (define where the item is in the file hierarchy)
# add a variable to the URL by using the what you want to collect in the opposing arrows
@app.route("/profile/<username>")
def profile(username): # same variable passed into the app.route
   

    user = None

    if username in users:
        user = users[username]   

    return render_template("Users/profile.html", username=username, user=user, users=username)



@app.route("/jinja")
def jinja(): # same variable passed into the app.route

    langs = ["HTML, CSS, Python, Flask (basics), JavaScript, SQL"]

    return render_template("jinja.html", langs=langs)

@app.route("/templates")
def templates(): 
    return render_template("templates.html")

if __name__ == '__main__':
    app.run(debug=True)
