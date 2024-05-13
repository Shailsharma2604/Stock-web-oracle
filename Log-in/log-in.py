from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# db=SQLAlchemy()
# db.init_app(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/stock_web_oracle"


# clss sign_in(db.Model):
#     Email = db.Column(db.String(255), unique = True, nullable = False),
#     Password = db.Column(db.String(255), nullable = False),
#     Sno = db.Column(db.Integer, primary_key = True)


# class create_account(db.Model):
#     Sno = db.Column(db.Integer, primary_key = True),
#     Name = db.Column(db.String(255), unique = True, nullable = False),
#     Email = db.Column(db.String(255), unique = True, nullable = False),
#     Password = db.Column(db.String(255), nullable = False)a


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/')
def index():
    return render_template('about.html')@app.route('/about')
def index():
    return render_template('index.html')@app.route('/')
def index():
    return render_template('index.html')




if __name__ == '__main__':
    app.run(debug=True)