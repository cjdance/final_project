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

@app.route('/fighters', methods = ['GET'])
def get_fighter():

    fighters = fighterModel.query.all()
    results = [{
        "name": fighter.name,
        "stance": fighter.stance,
        "weight": fighter.weight,
        "SApM": fighter.sig_str_abs_pM,
        "SLpM": fighter.sig_str_land_pM,
        "SDpct": fighter.sig_str_def_pct,
        "SLpct": fighter.sig_str_land_pct,
        "TDavg": fighter.td_avg,
        "TDacc": fighter.td_land_pct,
        "wins": fighter.n_win,
        "losses": fighter.n_loss,
        "draws": fighter.n_draw
    } for fighter in fighters]

    response = jsonify(results)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/flyweight', methods = ['GET'])
def get_flyweight():
    fighters = fighterModel.query.filter(fighterModel.weight == "125 lbs.")
    results = [{
        "name": fighter.name,
        "stance": fighter.stance,
        "weight": fighter.weight,
        "SApM": fighter.sig_str_abs_pM,
        "SLpM": fighter.sig_str_land_pM,
        "SDpct": fighter.sig_str_def_pct,
        "SLpct": fighter.sig_str_land_pct,
        "TDavg": fighter.td_avg,
        "TDacc": fighter.td_land_pct,
        "wins": fighter.n_win,
        "losses": fighter.n_loss,
        "draws": fighter.n_draw
    } for fighter in fighters]

    response = jsonify(results)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/bantamweight', methods = ['GET'])
def get_bantamweight():
    fighters = fighterModel.query.filter(fighterModel.weight == "135 lbs.")
    results = [{
        "name": fighter.name,
        "stance": fighter.stance,
        "weight": fighter.weight,
        "SApM": fighter.sig_str_abs_pM,
        "SLpM": fighter.sig_str_land_pM,
        "SDpct": fighter.sig_str_def_pct,
        "SLpct": fighter.sig_str_land_pct,
        "TDavg": fighter.td_avg,
        "TDacc": fighter.td_land_pct,
        "wins": fighter.n_win,
        "losses": fighter.n_loss,
        "draws": fighter.n_draw
    } for fighter in fighters]

    response = jsonify(results)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/featherweight', methods = ['GET'])
def get_featherweight():
    fighters = fighterModel.query.filter(fighterModel.weight == "145 lbs.")
    results = [{
        "name": fighter.name,
        "stance": fighter.stance,
        "weight": fighter.weight,
        "SApM": fighter.sig_str_abs_pM,
        "SLpM": fighter.sig_str_land_pM,
        "SDpct": fighter.sig_str_def_pct,
        "SLpct": fighter.sig_str_land_pct,
        "TDavg": fighter.td_avg,
        "TDacc": fighter.td_land_pct,
        "wins": fighter.n_win,
        "losses": fighter.n_loss,
        "draws": fighter.n_draw
    } for fighter in fighters]

    response = jsonify(results)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    app.run(debug=True)