from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from .models import Symptom, User
from . import db

# Create a Blueprint for routes
main = Blueprint('main', __name__, url_prefix='/')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=150)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


@main.route('/')
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('main.login'))
    return render_template('index.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            flash('Login successful!')
            return redirect(url_for('main.index'))
        else:
            flash('Login failed. Check your username and/or password.')

    return render_template('login.html', form=form)


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('You have successfully registered!')
        return redirect(url_for('main.login'))

    return render_template('register.html', form=form)


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.login'))


@main.route('/symptoms', methods=['GET', 'POST'])
@login_required
def symptoms():
    if request.method == 'POST':
        date = request.form['date']
        severity = request.form['severity']
        treatment = request.form['treatment']
        dose = request.form['dose']
        trigger = request.form['trigger']

        if not date or not severity:
            error = "Date and severity are required."
            return render_template('symptom_form.html', error=error)

        new_symptom = Symptom(date=date, severity=severity, treatment=treatment, dose=dose, trigger=trigger, user_id=current_user.id)
        db.session.add(new_symptom)
        db.session.commit()
        flash('Symptom added successfully!')
        return redirect(url_for('main.index'))

    return render_template('symptom_form.html')


@main.route('/symptoms/list')
@login_required
def symptom_list():
    page = request.args.get('page', 1, type=int)
    symptoms = Symptom.query.filter_by(user_id=current_user.id).paginate(page=page, per_page=10)
    return render_template('symptoms.html', symptoms=symptoms)


@main.route('/symptoms/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_symptom(id):
    symptom = Symptom.query.get_or_404(id)
    if request.method == 'POST':
        symptom.date = request.form['date']
        symptom.severity = request.form['severity']
        symptom.treatment = request.form['treatment']
        symptom.dose = request.form['dose']
        symptom.trigger = request.form['trigger']
        db.session.commit()
        flash('Symptom updated successfully!')
        return redirect(url_for('main.symptom_list'))

    return render_template('edit_symptom.html', symptom=symptom)


@main.route('/symptoms/delete/<int:id>', methods=['POST'])
@login_required
def delete_symptom(id):
    symptom = Symptom.query.get_or_404(id)
    db.session.delete(symptom)
    db.session.commit()
    flash('Symptom deleted successfully!')
    return redirect(url_for('main.symptom_list'))


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')
