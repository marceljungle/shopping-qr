import flask
from flask import Flask
from cloudant.client import Cloudant
from flask import render_template
import requests
import json
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/shopping', methods=['GET'])
def index():
    valor = request.args.get("id")
    consulta = requests.get(
        "https://c0cb63ab.us-south.apigw.appdomain.cloud/apishopping/getProduct?id=" + valor)
    json_body = consulta.json()
    print(json_body.items())
    nombreProducto = json_body["producto"]
    intolerancias = str()
    if(json_body["celiaco"] == '1'):
        intolerancias = intolerancias + "<span>" + "Apto para celiacos: NO❌" + "</span>"
        print("Apto para celiacos: NO")
    else:
        intolerancias = intolerancias + "<span>" + \
            "Apto para celiacos: SI✔️" + "</span>"
        print("Apto para celiacos: SI")

    if(json_body["diabetes"] == '1'):
        intolerancias = intolerancias + "<span>" + \
            "Apto para diabeticos: NO❌" + "</span>"
        print("Apto para diabeticos: NO")
    else:
        intolerancias = intolerancias + "<span>" + \
            "Apto para diabeticos: SI✔️" + "</span>"
        print("Apto para diabeticos: SI")

    if(json_body["cereales"] == '1'):
        intolerancias = intolerancias + "<span>" + "Cereales: SI✔️" + "</span>"
        print("Cereales: SI")
    else:
        intolerancias = intolerancias + "<span>" + "Cereales: NO❌" + "</span>"
        print("Cereales: NO")

    if(json_body["fructosa"] == '1'):
        intolerancias = intolerancias + "<span>" + "Fructosa: SI✔️" + "</span>"
        print("Fructosa: SI")
    else:
        intolerancias = intolerancias + "<span>" + "Fructosa: NO❌" + "</span>"
        print("Fructosa: NO")

    if(json_body["frutosSecos"] == '1'):
        intolerancias = intolerancias + "<span>" + "Frutos secos: SI✔️" + "</span>"
        print("Frutos secos: SI")
    else:
        intolerancias = intolerancias + "<span>" + "Frutos secos: NO❌" + "</span>"
        print("Frutos secos: NO")

    if(json_body["histamina"] == '1'):
        intolerancias = intolerancias + "<span>" + "Histamina: SI✔️" + "</span>"
        print("Histamina: SI")
    else:
        intolerancias = intolerancias + "<span>" + "Histamina: NO❌" + "</span>"
        print("Histamina: NO")

    if(json_body["huevo"] == '1'):
        intolerancias = intolerancias + "<span>" + "Huevo: SI✔️" + "</span>"
        print("Huevo: SI")
    else:
        intolerancias = intolerancias + "<span>" + "Huevo: NO❌" + "</span>"
        print("Huevo: NO")

    if(json_body["lactosa"] == '1'):
        intolerancias = intolerancias + "<span>" + "Lactosa: SI✔️" + "</span>"
        print("Lactosa: SI")
    else:
        intolerancias = intolerancias + "<span>" + "Lactosa: NO❌" + "</span>"
        print("Lactosa: NO")

    if(json_body["legumbres"] == '1'):
        intolerancias = intolerancias + "<span>" + "Legumbres: SI✔️" + "</span>"
        print("Legumbres: SI")
    else:
        intolerancias = intolerancias + "<span>" + "Legumbres: NO❌" + "</span>"
        print("Legumbres: NO")

    if(json_body["mar"] == '1'):
        intolerancias = intolerancias + "<span>" + \
            "Productos del mar: SI" + "✔️</span>"
        print("Productos del mar: SI")
    else:
        intolerancias = intolerancias + "<span>" + "Productos del mar: NO❌" + "</span>"
        print("Productos del mar: NO")

    return """      
<!DOCTYPE html>
<html lang="en" >
<head>
  <meta charset="UTF-8">
  <title>Copper - ShoppingQR</title>
  <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Maitree'><link rel="stylesheet" href="./style.css">
    <style>
/* Basic styles */
*,
*::before,
*::after {
  box-sizing: border-box;
}

:root{
    --bg-color: #D8D8D8;
}

body {
  display: flex;
  align-items: stretch;
  justify-content: center;
  overflow: hidden;
  width: 100vw;
  height: 100vh;
  color: #000;
  background-color: var(--bg-color);
  font-family: 'Maitree', serif;
}
h1{
    font-size: 3em;
    font-weight: normal;
}

/* title styles */
.home-title span{
    position: relative;
    overflow: hidden;
    display: block;
    line-height: 1.2;
}

.home-title span::after{
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 100%;
    height: 100%;
    background: white;
    animation: a-ltr-after 2s cubic-bezier(.77,0,.18,1) forwards;
    transform: translateX(-101%);
}

.home-title span::before{
    content: '';
    position: absolute;
    top: 0;
    right: 0;
    width: 100%;
    height: 100%;
    background: var(--bg-color);
    animation: a-ltr-before 2s cubic-bezier(.77,0,.18,1) forwards;
    transform: translateX(0);
}

.home-title span:nth-of-type(1)::before,
.home-title span:nth-of-type(1)::after{
    animation-delay: 1s;
}

.home-title span:nth-of-type(2)::before,
.home-title span:nth-of-type(2)::after{
    animation-delay: 1.5s;
}

@keyframes a-ltr-after{
    0% {transform: translateX(-100%)}
    100% {transform: translateX(101%)}
}

@keyframes a-ltr-before{
    0% {transform: translateX(0)}
    100% {transform: translateX(200%)}
}
</style>
</head>
<body>
<!-- partial:index.partial.html -->
<h1 class="home-title">
  <span> """ + "<b>Nombre del Producto:</b> " + nombreProducto + """ </span>
  <br>
  """ + intolerancias + """
  
</h1>
<!-- partial -->
  
</body>


<footer>
<img src="https://www.cloudbuilders.es/wp-content/uploads/2018/10/ibm-cloud-logo.png" style="width:450px;height:250px;justify-content:center ">
<img src="https://i.imgur.com/0EbiphT.png" style="width:450px;height:250px">


</footer>
</html>
"""


@app.route('/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"


variable = "mierda"  # ejemplo utilizacion con variable


@app.route('/' + variable, methods=['GET'])
def mierda():
    return "<h1>Has entrado en la MIERDA.</p>"


app.run(host='0.0.0.0')
