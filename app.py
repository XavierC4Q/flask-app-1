from flask import Flask, render_template, request
import helpers as h

app = Flask(__name__)
app.debug = True

@app.route('/')
def home_route():
    return ' '.join(h.show_users())