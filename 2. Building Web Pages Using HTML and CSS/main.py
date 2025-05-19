# Importing the Flask class and the render_template function from the flask module
from flask import Flask, render_template, jsonify

# Creating an instance of the Flask class.
# __name__ is a special variable that gets the name of the current module.
# Flask uses it to determine the root path for the application.
app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Hderabad",
        "Salary":"10,00,0000",
    },
 
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Benguluru",
        "Salary":"9,00,0000",
    },

    {
        "id": 3,
        "title": "Digital marketing",
        "location": "Remote",
        "Salary":"12,00,0000",
    },

    {
        "id": 4,
        "title": "Backend Engeneer",
        "location": "Delhi",
        "Salary":"16,00,0000",
    },

]

# This is a route decorator.
# It tells Flask to execute the 'home' function when someone visits the "/" URL (i.e., the homepage).
@app.route("/")
def home():
    # This function will return the rendered 'index.html' file from the 'templates' folder.
    return render_template("Home.html", jobs = JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

# This condition checks if this script is being run directly (not imported as a module).
if __name__ == "__main__":
    # Runs the Flask web server in debug mode.
    # Debug mode allows automatic reloading and gives detailed error messages.
    app.run(debug=True)
