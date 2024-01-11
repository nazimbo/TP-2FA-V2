from flask import Flask, render_template, redirect, url_for, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import pyotp
import qrcode

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Check the hardcoded password
        if password == 'password':
            # Generate TOTP secret
            totp = pyotp.TOTP(pyotp.random_base32())
            totp_secret = totp.secret

            # Create a QR code
            uri = totp.provisioning_uri(name=username, issuer_name="Flask 2FA Demo")
            img = qrcode.make(uri)
            img.save('static/qrcode.png')

            # Render the TOTP secret for the user
            return render_template('enable_2fa.html', username=username, totp_secret=totp_secret)
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html', form=form)

@app.route('/verify_2fa/<username>/<totp_secret>', methods=['POST'])
def verify_2fa(username, totp_secret):
    verification_code = request.form.get('verification_code')
    
    # Verify the entered code
    totp = pyotp.TOTP(totp_secret)
    if totp.verify(verification_code):
        # Successful verification, you can redirect to a success page or perform further actions
        return "Verification successful! You can now proceed with 2FA."
    else:
        # Failed verification
        flash('Invalid verification code', 'danger')
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
