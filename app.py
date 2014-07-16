from flask import Flask, render_template
from local_config import SECRET_KEY
from flask.ext.pagedown import PageDown
from forms import PageDownFormTest

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config['DEBUG'] = True
app.config['PROPOGATE_EXCEPTIONS'] = True
pagedown = PageDown(app)



@app.route("/")
def index():
    return render_template('base.html',)

@app.route("/mdtest")
def mdtest():
    form = PageDownFormTest()
    return render_template('md.html', form=form)

if __name__ == "__main__":
    app.run()