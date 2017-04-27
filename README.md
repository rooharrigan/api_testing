## An Introduction to the Slack API: Easy-Peasy Incoming Webhooks check it out

This repo contains a starting point for exploring the Slack APIs using incoming webhooks.
It's a simple app written in Python using Flask.

## What's inside
- base.html:  some bootstrap and formatting setup for flash messages
- index.html: a simple form and a navbar that links out to further Slack resources
- a server.py file with a single route to handle form submission
- a few static elements as a starting place (favicon, .css file, etc.) as well as the env requirements


## How to make it go
- `git clone` the repo from github to your desktop
- In a terminal session, open the repo and open up the file `renametosecrets.sh`
- Go to [api.slack.com](api.slack.com), select Create a Custom Integration, and follow the prompts to set up an incoming webhook on your personal test team.
- Copy the URL for your incoming webhook here and save it. Rename the this file `secrets.sh`
- Double check that you have a .gitignore file in this repo and that `secrets.sh` is in it (so your URL will never accidentally get committed)
- Back in your terminal, set up your virtual environment:
 	- `virtualenv env`
	- `source env/bin/activate`
	- `pip install -r requirements.txt`
	- `source secrets.sh`
	- `python server.py`
- Once your server starts successfully, navigate to localhost:5000 and check that the form has successfully loaded.
	*Note that if you are not connected to the internet, the bootstrap will not load and the page will look very 90's. Once the page loads, it should look very early 2000's (feel free to customize!)
- Open up your `server.py` and `index.html` files in your text editor of choice and have at it.


## Workshop Steps: Easy Peasy Incoming Webhooks

Once you have your server up and running, modify the code you are given to learn more about sending notifications in Slack! Open [our incoming webhooks page](https://api.slack.com/incoming-webhooks) as a guide for completing the following tasks.  There are lots of in-line comments to guide you, but here they are in order:

1. Set up the form and the server so that the form submits a post to the server's /submit route.

2.  Edit the route so the server can get the 'main-text' out of the request it is receiving.

3. Add another text field to accept 'moar-text'.  Make sure the server can parse this one too, and add it into the dictionary we are using to construct JSON.

4. Add in a field and try sending a link!

5. Try sending an emoji using the Slack notation, like `:tada:`, in one of your existing fields.

6. Try sending a message with formatting: bold, italics, etc.

7. Add in three more form elements to capture title, text, and color inputs.  Update the server code to handle these elements use them to add an attachment to your JSON.  The structure of the attachemnts dictionary has already been started for you, but don't forget to add commas!

8. Go wild! Add some more attachments, put links and emojis in them, and play with formatting some more.

9. See if you can figure out how to change the icon your webhook is posting with.


If you find yourself lost lost, there is directory in this repo called 'final' that has one version of how your app could work.  Feel free to peek in there!

## Final Product
![Something like this.](/templates/static/final_example.png)
