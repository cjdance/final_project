#Dependencies and Setup
from flask import Flask, jsonify
from sqlalchemy import create_engine
from sqlalchemy import or_
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


class weightModel(db.Model):
    __tablename__ = 'weight_data'

    index = db.Column(db.Integer(), primary_key=True)
    weight_name = db.Column(db.String())
    weight = db.Column(db.String())


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


@app.route('/weight', methods = ['GET'])
def get_weights():

    weights = weightModel.query.all()
    results = [{
        "name": weight.weight_name,
        "weight": weight.weight
    } for weight in weights]

    response = jsonify(results)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/Flyweight', methods = ['GET'])
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


@app.route('/Bantamweight', methods = ['GET'])
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


@app.route('/Featherweight', methods = ['GET'])
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

@app.route('/Lightweight', methods = ['GET'])
def get_lightweight():
    fighters = fighterModel.query.filter(fighterModel.weight == "155 lbs.")
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


@app.route('/Welterweight', methods = ['GET'])
def get_welterweight():
    fighters = fighterModel.query.filter(fighterModel.weight == "170 lbs.")
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

@app.route('/Middleweight', methods = ['GET'])
def get_middleweight():
    fighters = fighterModel.query.filter(fighterModel.weight == "185 lbs.")
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

@app.route('/Light-Heavyweight', methods = ['GET'])
def get_lightheavyweight():
    fighters = fighterModel.query.filter(fighterModel.weight == "205 lbs.")
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

@app.route('/Heavyweight', methods = ['GET'])
def get_heavyweight():
    fighters = fighterModel.query.filter(or_(fighterModel.weight != weight for weight in ["205 lbs.", "185 lbs.", "170 lbs.", "155 lbs.", "145 lbs.", "135 lbs.", "125 lbs."]))
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