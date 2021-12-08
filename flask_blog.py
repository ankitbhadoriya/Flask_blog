from os import truncate
from flask import Flask , render_template,url_for


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello_world():
    return render_template('home.html',posts=posts , title='Home')

@app.route("/about")
def hello_about():
    return render_template("about.html",title='About')


posts=[ 
        {   "Title":"Pirate kings Blog",
            "Author":"Luffy",
            "Date":"21st April 1982",
            "content":"I am going to be the king of pirates \
                 But first i need some meat"
        },
        {   "Title":"Ussop the brave's Blog",
            "Author":"God Ussop",
            "Date":"1st April 1982",
            "content":"I am going to be the brave warrior of albaf"
        },
        {   "Title":"Zoros Blog",
            "Author":"Roronoa Zoro",
            "Date":"31st April 1982 ",
            "content":"I am going to be the best swordsman in th world"
        }
]



if __name__=="__main__":
    app.run(debug=True)