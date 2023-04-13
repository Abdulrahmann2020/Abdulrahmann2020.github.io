from flask import Flask, request, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

@app.route('/')
def index():
    message = "Hello, Flask!"  # Example dynamic data
    return render_template('index.html', message=message)

# Set up Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'flaskm51@gmail.com'  # Your Gmail email address
app.config['MAIL_PASSWORD'] = 'gzxzbegysnflrhbe'  # Your Gmail password

mail = Mail(app)

@app.route('/send', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Create and send email
    msg = Message('Contact Form Submission', sender=email, recipients=['flaskm51@gmail.com'])  # Your Gmail email address
    msg.body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    mail.send(msg)

    return 'Message sent successfully'

if __name__ == '__main__':
    app.run(debug=True)
