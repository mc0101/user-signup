from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('form.html')
    return template.render()

@app.route('/', methods=['POST'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    verpw = request.form['verpw']
    email = request.form['email']
    username_error = ''
    password_error = ''
    verpw_error = ''
    email_error = ''
    if len(username) < 4 or len(username) > 21:
        username_error = "Please select a valid username."
        username = username
        password = ""
        verpw = ""
        email = email
    if " " in username:
        username_error = "Please select a valid username."
        username = username
        password = ""
        verpw = "" 
        email = email
    if username == "":
        username_error = "Please select a username."
        username = username
        password = ""
        verpw = ""
        email = email   
    if len(password) < 4 or len(password) > 21:
        password_error = "Please enter a valid password. Passwords must be between 3 and 20 characters long and contain no spaces."
        username = username
        password = ""
        verpw = ""
        email = email
    if " " in password:
        password_error = "Please enter a valid password. Passwords must be between 3 and 20 characters long and contain no spaces."
        password = ""
        username = username
        verpw = ""
        email = email
    if password_error == "":
        if verpw == "":
            verpw_error = "Please re-enter your password."
            username = username
            password = ""
            email = email
        if verpw != password:
            verpw_error = "Your passwords do not match. Please re-enter your password."
            verpw = ""
            password = ""
            username = username
            email = email
    if email != "":
        if "@" not in email or "." not in email or " " in email or len(email) < 4 or len(email) > 21:
            email_error = "Please enter a valid email."
            username = username
            email = ""
            password = ""
            verpw = ""
    '''
    if request.method != 'POST':
        username = ""
        password = ""
        verpw = ""
        email = ""
        username_error = ""
        password_error = ""
        verpw_error = ""
        email_error = ""
        '''
    if not username_error and not password_error and not verpw_error and not email_error:
        approvedusername = request.args.get('username')
        template = jinja_env.get_template('welcome.html'.format(approvedusername))
        return template.render(approvedusername = username)
    else:
        template = jinja_env.get_template('form.html')
        return template.render(username_error = username_error, password_error = password_error, verpw_error = verpw_error, email_error = email_error, username = username, password = password, verpw = verpw, email = email)

app.run()