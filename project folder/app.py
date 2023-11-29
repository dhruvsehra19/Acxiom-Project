

from flask import Flask, render_template

app = Flask(name)

# Route for the home page
@app.route('/home')
def home():
    return render_template('home.html', username="John")  # Pass the username dynamically

# Add other routes for different pages...

if name == 'main':
    app.run(debug=True)