from flask import Flask, request, render_template, redirect, flash
from random import choice, sample
import requests
import json


COMPLIMENTS = ["smart", "clever", "tenacious", "awesome", "Pythonic"]

app = Flask(__name__)
app.secret_key = "What's up chickens what you bockin' with."

#######################################################################

@app.route('/')
def index():
	return render_template("index.html")


@app.route('/submit',  methods=['POST'])
def submit_json_to_webhook():
	text = request.form["text"]
	print text

	#Build the JSON to send
	payload = {
		'text' : text
	}

	url = "https://hooks.slack.com/services/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"

	print payload

	#Send it to the URL Slack provides
	r = requests.post(url, data=json.dumps(payload))
	status_code = r.status_code

	if status_code == 200:
		flash('You did it!')
		return redirect("/")
	else:
		flash('Oh no, something went wrong. You are getting a %s  status code error.' % (status_code))

	#If you get an ok=true response, flash that it worked and redirect!
	flash('You did it!')
	return redirect("/")

	#If not, flash an error and keep_input in your form




#######################################################################

if __name__ == "__main__":
    app.run(debug=True)
