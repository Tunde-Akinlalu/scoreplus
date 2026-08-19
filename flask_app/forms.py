from flask_wtf import FlaskForm
from wtforms import (StringField, PasswordField, SubmitField, SelectField,
                     FloatField, IntegerField, DateField, FieldList, FormField)
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, NumberRange


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=80)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class EventForm(FlaskForm):
    name = StringField('Event Name', validators=[DataRequired(), Length(max=200)])
    date = DateField('Event Date', validators=[Optional()])
    submit = SubmitField('Create Event')


class CategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[DataRequired(), Length(max=100)])
    piece_type = SelectField('Type', choices=[('5P', '5 Piece'), ('4P', '4 Piece'), ('2P', '2 Piece')])
    submit = SubmitField('Add Category')


class SchoolForm(FlaskForm):
    name = StringField('School Name', validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('Add School')


class AthleteForm(FlaskForm):
    number = IntegerField('Number', validators=[DataRequired(), NumberRange(min=1)])
    name = StringField('Name', validators=[Optional(), Length(max=150)])
    submit = SubmitField('Add Athlete')


class ScoreForm(FlaskForm):
    set_vault = FloatField('Set Vault', validators=[Optional()], default=0.0)
    vol_vault = FloatField('Vol Vault', validators=[Optional()], default=0.0)
    set_floor = FloatField('Set Floor', validators=[Optional()], default=0.0)
    vol_floor = FloatField('Vol Floor', validators=[Optional()], default=0.0)
    submit = SubmitField('Save Scores')


class AddSchoolToCategory(FlaskForm):
    school_id = SelectField('School', coerce=int, validators=[DataRequired()])
    num_athletes = IntegerField('Number of Athletes', default=6,
                                validators=[DataRequired(), NumberRange(min=1, max=12)])
    submit = SubmitField('Add School to Category')
