from flask.ext.wtf import Form
from flask.ext.pagedown.fields import PageDownField
from wtforms.fields import SubmitField

class PageDownFormTest(Form):
    pagedown = PageDownField('Enter markdown')
    submit = SubmitField('Submit')