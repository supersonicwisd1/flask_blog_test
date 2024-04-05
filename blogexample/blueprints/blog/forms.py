from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, BooleanField, FieldList, StringField
from wtforms.validators import DataRequired, Length
# from flask_ckeditor import CKEditorField
    
# I had to change TextField to StringField due to the update from WTFORMS

class AddPostForm(FlaskForm):
    # title = TextField('Title', [DataRequired(), Length(1, 40)])
    title = StringField('Title', [DataRequired(), Length(1, 40)])
    body = TextAreaField('Body', [DataRequired(), Length(1, 8192)])
    # tags = TextAreaField('tags', [DataRequired(), Length(3, 100)])
    taglist = StringField('taglist')
    # tags = FieldList(StringField('tags'), min_entries=1)
    visible = BooleanField('Published')
    # body = CKEditorField('Body', [DataRequired(), Length(1, 8192)])


class UpdatePostForm(FlaskForm):
    # title = TextField('Title', [DataRequired(), Length(1, 40)])
    title = StringField('Title', [DataRequired(), Length(1, 40)])
    body = TextAreaField('Body', [DataRequired(), Length(1, 8192)])
    # taglist = TextAreaField('tags', [DataRequired(), Length(3, 100)])
    # tagstring = StringField('tagstring')
    taglist = StringField('taglist')
    visible = BooleanField('Published')
    # body = CKEditorField('Body', [DataRequired(), Length(1, 8192)])