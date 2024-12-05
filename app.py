from flask import Flask

# Create a Flask app instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return "Hello, Greatcoders team"

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
