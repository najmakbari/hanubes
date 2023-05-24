from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
  return "Hello World"

@app.route("/NL")
def helloNL():
  return "Hallo Wereld"

@app.route("/hoofdstad/<land>")
def hoofdstad(land):
  plaats="land onbekend"
  if (land=="Duitsland"): plaats="Berlijn"
  if (land=="Nederland"): plaats="Amsterdam"
  if (land=="Frankrijk"): plaats="Parijs"

  return plaats


app.run(host='0.0.0.0')