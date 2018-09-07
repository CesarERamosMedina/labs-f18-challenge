from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/pokemon/<endpoint>", methods=['GET'])
def pokemon_display(endpoint):
	url = 'http://pokeapi.co/api/v2/pokemon/'+endpoint
	r = requests.get(url)
	json_response = r.json()

	name = json_response['name'].capitalize()
	id = str(json_response['id'])

	if endpoint.isdigit():
		return render_template('name.html', name=name,id=id)
	else:
		return render_template('id.html', name=name,id=id)
		

if __name__ == '__main__':
    app.run()
