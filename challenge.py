from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/pokemon/<endpoint>", methods=['GET'])
def pokemon_display(endpoint):
	url = 'http://pokeapi.co/api/v2/pokemon/'+endpoint
	r = requests.get(url)
	json_response = r.json()
	if(endpoint.isdigit()):
		return "<h1>The pokemon with id " + str(json_response['id']) + " is " + json_response['name'] + "<h1>"
	else:
		return "<h1>"+ json_response['name'].capitalize() +" has id "+ str(json_response['id']) + "<h1>"
		

if __name__ == "__main__":
    app.run()
