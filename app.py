from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

toolbar = DebugToolbarExtension(app)

@app.route('/')
def home():
    """ Create and show form to ask for words for story """
    prompts = story.prompts
    return render_template('home.html', prompts=prompts)

@app.route('/story')
def get_story():
    """ Show story with words from form """
    text = story.generate(request.args)
    return render_template('story.html', text=text)