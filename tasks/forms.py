from wtforms import Form, StringField, TextAreaField

class TaskForm(Form):
    title = StringField('Title')
    body = TextAreaField('Body')
    
    
