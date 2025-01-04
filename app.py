from flask import Flask
import os

# Create a Flask app instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return "Hello, Greatcoders version-2"

# Run the application
if __name__ == '__main__':
    port=int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
    
