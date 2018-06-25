from flask import Flask, render_template, request

app = Flask(__name__)


users ={}

@app.route('/')
def home():
    return render_template("home.html")
@app.route('/login', methods=['POST'])
def login():
    error = None
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        for user in users:
            if users[user]['name'] == name and users[user]['password'] == password:
                return redirect(url_for('books'))
        
                error = 'invalid credentials.Please try again.'
        
    return render_template('books.html', error=error)

 
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']


        id = len(users) + 1

        users[id] = { 'username': username, 'email': email}
         


    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)