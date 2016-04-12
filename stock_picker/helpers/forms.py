from flask_wtf import Form
from wtforms import  StringField, SelectField, DateField, SubmitField, BooleanField, TextField, PasswordField, validators
from wtforms.validators import DataRequired
from werkzeug import secure_filename
from flask.ext.uploads import UploadSet, IMAGES, TEXT
from flask_wtf.file import FileField, FileAllowed, FileRequired

text = UploadSet('text', TEXT)

class PickForm(Form):
	textType = SelectField('Type', choices=[('book', 'BOOK'), ('poem', 'POEM'), ('lyric', 'LYRIC'), ('custom', 'CUSTOM')], validators=[DataRequired()])
	title = StringField('Title', validators=[DataRequired(), validators.Length(min = 1, max = 200)])
	author = StringField('Author', validators=[DataRequired(), validators.Length(min=4, max = 60)])
	description = StringField('Description')
	pub_date = DateField('Publication date')
	upload = FileField('Your text file', validators=[FileRequired(), FileAllowed(text, "Text only!")])
	submit = SubmitField("Submit")

	#def save_file():
	#	filename = secure_filename(form.upload.data.filename)
	#	form.upload.save(os.path.join(app.config['UPLOADED_TEXT_DEST'], filename))
	#	