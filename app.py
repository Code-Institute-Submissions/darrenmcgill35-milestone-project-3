import os
from flask import Flask, render_template, redirect, request, flash, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = 'darren_secret'

app.config["MONGO_DBNAME"] = 'msProject3'
app.config["MONGO_URI"] = 'mongodb+srv://darrenmcgill:darrenmcgill35@myfirstcluster-qtggr.mongodb.net/msProject3'

mongo = PyMongo(app)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        flash("Thanks, You have subscribed")
    return render_template("index.html")


@app.route('/review', methods=["GET", "POST"])
def review():
    return render_template("review.html", page_title="Reviews")


@app.route('/add_a_player', methods=["GET", "POST"])
def add_a_player():
    return render_template("add_a_player.html", page_title="Add & Review", players=mongo.db.players.find())


@app.route('/insert_player', methods=['POST'])
def insert_player():
    reviews = mongo.db.reviews
    reviews.insert_one(request.form.to_dict())
    return redirect(url_for('review_a_player'))


@app.route('/review_a_player', methods=["GET", "POST"])
def review_a_player():
    return render_template("review_a_player.html", page_title="Edit & Delete", reviews=mongo.db.reviews.find())


@app.route('/merchandise', methods=["GET", "POST"])
def merchandise():
    return render_template("merchandise.html", page_title="Merchandise")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
