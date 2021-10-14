#Dependencies and Setup
from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#use flask_pymongo to set up mongo connection
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:cdw@localhost/ufc"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class fighterModel(db.Model):
    __tablename__ = 'fighters'

    index = db.Column(db.Integer(), primary_key=True)
    dob = db.Column(db.Integer())
    height = db.Column(db.String())
    n_draw = db.Column(db.Integer())
    n_loss = db.Column(db.Integer())
    n_win = db.Column(db.Integer())
    name = db.Column(db.String())
    reach = db.Column(db.Integer())
    sig_str_abs_pM = db.Column(db.Float())
    sig_str_def_pct = db.Column(db.Float())
    sig_str_land_pM = db.Column(db.Float())
    sig_str_land_pct = db.Column(db.Float())
    stance = db.Column(db.String())
    sub_avg = db.Column(db.Float())
    td_avg = db.Column(db.Float())
    td_def_pct = db.Column(db.Float())
    td_land_pct = db.Column(db.Float())
    weight = db.Column(db.String())
    total_fights = db.Column(db.Integer())
    

    def __init__(self, name, stance, weight):
        self.name = name
        self.stance = stance
        self.weight = weight

    def __repr__(self):
        return f"<Fighter {self.name}>"


@app.route('/')
def hello():
    return "Hello World!"



#================================================================================

#################################################
# Flask Routes
#################################################

@app.route('/fighters')
def get_fighter():

    fighters = fighterModel.query.all()
    results = [{
        "name": fighter.name,
        "stance": fighter.stance,
        "weight": fighter.weight
    } for fighter in fighters]

    return {"count": len(results), "fighters": results}


if __name__ == "__main__":
    app.run(debug=True)