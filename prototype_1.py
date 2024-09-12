from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

# Define a basic route
@app.route('/')
def home():
    return "Welcome to Study Buddy AI!"

# Define another basic route
@app.route('/about')
def about():
    return "About Study Buddy AI"

# Define a basic route to check models
#@app.route('/users')
#def users():
 #   users = User.query.all()
  #  return render_template('users.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        new_user = User(name=name)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('users'))
    return '''
        <form method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name">
            <button type="submit">Add User</button>
        </form>
    '''


# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
