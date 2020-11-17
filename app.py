import flask
from flask import Flask
from cloudant.client import Cloudant
from flask import render_template
username = "b6d7fc1e-fac3-4f38-b18e-103d2d32bcd5-bluemix"
password = "e0bf2976fee8d2dd7b808d5a9b7f4b1e32c9c6abe6b3ca280da2ad348001a50a"
accName = "	https://b6d7fc1e-fac3-4f38-b18e-103d2d32bcd5-bluemix.cloudant.com"
api = "rdbCPpHxiOOoZ8T9XIXRETihHZQhjA76nY7oRXk4bCf0"


client = Cloudant.iam(username, api, connect=True)
session = client.session()

print(session)
#print('Username: {0}'.format(session['userCtx']['name']))
#print('Databases: {0}'.format(client.all_dbs()))


client.disconnect()
app = flask.Flask(__name__)
app.config["DEBUG"] = True

""" Consulta base de datos usuario  7812312, miras sus intolerancias* y devuelve el resultado
q será procesado aqui  ej_:asdasdasdasda.com/macarronesHacendado137821/7812312, siendo macarronesHacendado137821
el id* del producto """


@app.route('/caca', methods=['GET'])
def caca():
    return render_template("index2.html")


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


variable = "mierda"  # ejemplo utilizacion con variable


@app.route('/' + variable, methods=['GET'])
def mierda():
    return "<h1>Has entrado en la MIERDA.</p>"


app.run()
