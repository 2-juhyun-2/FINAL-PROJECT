from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, RadioField, DateTimeField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email


# login
class UserLoginForm(FlaskForm):
    username = StringField('사용자 아이디', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])


# signup
class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다.')])
    password2 = PasswordField('비밀번호 확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])
    level = RadioField('레벨', choices = [('level1','1'),('level2','2'),('level3','3')])
    created_at = DateTimeField('생성시간')