from scrape_linkedin import ProfileScraper
import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/linkedin/profile', methods=['GET'])
def get_profile():
    username = request.args.get('username')
    with ProfileScraper() as scraper:
        return scraper.scrape(user=username).to_dict()


app.run()