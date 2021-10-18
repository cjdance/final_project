#Dependencies and Setup
from flask import Flask, jsonify, render_template, request
from sqlalchemy import create_engine
from sqlalchemy import or_
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.models import load_model



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://lobpnlrdoxctkw:a9aa044b579fbbc191e8162a7b4eaffa687a966b9b9bde7f0d404e230b415102@ec2-54-164-56-10.compute-1.amazonaws.com:5432/da6f3crjlcgotj"
# "postgresql://postgres:cdw@localhost/ufc"
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


class predictModel(db.Model):
    __tablename__ = 'predict_data'

    index = db.Column(db.Integer(), primary_key=True)
    fighter_pair = db.Column(db.String())
    fighter_1 = db.Column(db.String())
    fighter_2 = db.Column(db.String())
    weight_class = db.Column(db.String())
    winner = db.Column(db.String())

@app.route('/')
def form():
    if request.method == 'GET':
        return render_template('index.html')


@app.route('/data_library')
def data_lib():
    if request.method == 'GET':
        return render_template('data_lib.html')
     


@app.route('/data', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        
        form_weight = request.form['weight']
        form_f1 = request.form['f1']
        form_f2 = request.form['f2']

        fighters = fighterModel.query.filter((fighterModel.name == form_f1) | (fighterModel.name == form_f2))
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
        "draws": fighter.n_draw,
        "subs": fighter.sub_avg
        } for fighter in fighters]

        fighters = [results[0]["SApM"],results[0]["SLpct"], results[0]["SApM"],results[1]["SApM"],results[1]["SLpct"], results[1]["SApM"]]

        
        ufc_model = load_model("models/ufc_model_trained_2.h5")

        encoded_predictions = ufc_model.predict_classes([fighters])

        if encoded_predictions == 0:

            winner = f'Predicted Winner: {results[0]["name"]}'

        else:

            winner = f'Predicted Winner: {results[1]["name"]}'

        response = jsonify(results)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return render_template("data.html", data=winner)
        

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
        "draws": fighter.n_draw,
        "subs": fighter.sub_avg
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
        "draws": fighter.n_draw,
        "subs": fighter.sub_avg
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
        "draws": fighter.n_draw,
        "subs": fighter.sub_avg
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
        "draws": fighter.n_draw,
        "subs": fighter.sub_avg
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
        "draws": fighter.n_draw,
        "subs": fighter.sub_avg
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
        "draws": fighter.n_draw,
        "subs": fighter.sub_avg
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
        "draws": fighter.n_draw,
        "subs": fighter.sub_avg
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
        "draws": fighter.n_draw,
        "subs": fighter.sub_avg
    } for fighter in fighters]

    response = jsonify(results)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# @app.route('/predict', methods = ['GET', 'POST'])
# def get_predict():

#     ufc_model = load_model("ufc_model_trained_2.h5")

#     fighter_1 = request.

#     fighters = fighterModel.query.all()
#     results = [{
#         "name": fighter.name,
#         "stance": fighter.stance,
#         "weight": fighter.weight,
#         "SApM": fighter.sig_str_abs_pM,
#         "SLpM": fighter.sig_str_land_pM,
#         "SDpct": fighter.sig_str_def_pct,
#         "SLpct": fighter.sig_str_land_pct,
#         "TDavg": fighter.td_avg,
#         "TDacc": fighter.td_land_pct,
#         "wins": fighter.n_win,
#         "losses": fighter.n_loss,
#         "draws": fighter.n_draw,
#         "subs": fighter.sub_avg
#     } for fighter in fighters]

# @app.route('/Flyweight_predictions', methods = ['GET'])
# def get_flywin():
#     fights = predictModel.query.filter(predictModel.weight_class == "125 lbs./125 lbs.")
#     results = [{
#         "fighter_pair": fight.fighter_pair,
#         "fighter_1": fight.fighter_1,
#         "fighter_2": fight.fighter_2,
#         "winner": fight.winner,
#         "weight_class": fight.weight_class
#     } for fight in fights]

#     response = jsonify(results)
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response

# @app.route('/Bantamweight_predictions', methods = ['GET'])
# def get_ban_win():
#     fights = predictModel.query.filter(predictModel.weight_class == "135 lbs./135 lbs.")
#     results = [{
#         "fighter_pair": fight.fighter_pair,
#         "fighter_1": fight.fighter_1,
#         "fighter_2": fight.fighter_2,
#         "winner": fight.winner,
#         "weight_class": fight.weight_class
#     } for fight in fights]

#     response = jsonify(results)
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response

# @app.route('/Featherweight_predictions', methods = ['GET'])
# def get_feathwin():
#     fights = predictModel.query.filter(predictModel.weight_class == "145 lbs./145 lbs.")
#     results = [{
#         "fighter_pair": fight.fighter_pair,
#         "fighter_1": fight.fighter_1,
#         "fighter_2": fight.fighter_2,
#         "winner": fight.winner,
#         "weight_class": fight.weight_class
#     } for fight in fights]

#     response = jsonify(results)
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response


# @app.route('/Lightweight_predictions', methods = ['GET'])
# def get_lightwin():
#     fights = predictModel.query.filter(predictModel.weight_class == "155 lbs./155 lbs.")
#     results = [{
#         "fighter_pair": fight.fighter_pair,
#         "fighter_1": fight.fighter_1,
#         "fighter_2": fight.fighter_2,
#         "winner": fight.winner,
#         "weight_class": fight.weight_class
#     } for fight in fights]

#     response = jsonify(results)
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response


# @app.route('/Welterweight_predictions', methods = ['GET'])
# def get_weltwin():
#     fights = predictModel.query.filter(predictModel.weight_class == "170 lbs./170 lbs.")
#     results = [{
#         "fighter_pair": fight.fighter_pair,
#         "fighter_1": fight.fighter_1,
#         "fighter_2": fight.fighter_2,
#         "winner": fight.winner,
#         "weight_class": fight.weight_class
#     } for fight in fights]

#     response = jsonify(results)
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response


# @app.route('/Middleweight_predictions', methods = ['GET'])
# def get_middwin():
#     fights = predictModel.query.filter(predictModel.weight_class == "185 lbs./185 lbs.")
#     results = [{
#         "fighter_pair": fight.fighter_pair,
#         "fighter_1": fight.fighter_1,
#         "fighter_2": fight.fighter_2,
#         "winner": fight.winner,
#         "weight_class": fight.weight_class
#     } for fight in fights]

#     response = jsonify(results)
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response


# @app.route('/Light-Heavyweight_predictions', methods = ['GET'])
# def get_lheavywin():
#     fights = predictModel.query.filter(predictModel.weight_class == "205 lbs./205 lbs.")
#     results = [{
#         "fighter_pair": fight.fighter_pair,
#         "fighter_1": fight.fighter_1,
#         "fighter_2": fight.fighter_2,
#         "winner": fight.winner,
#         "weight_class": fight.weight_class
#     } for fight in fights]

#     response = jsonify(results)
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     return response

if __name__ == "__main__":
    app.run(debug=True)