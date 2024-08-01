from flask import Flask, render_template_string

app = Flask(__name__)

# Define a template with HTML content
template = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to My Flask App</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; }
        h1 { color: #3498db; }
        p { font-size: 18px; }
    </style>
</head>
<body>
    <h1>Welcome!</h1>
    <p>Hello, I'm Prateek. Explore my sample Flask application!</p>
    <img src="https://via.placeholder.com/400" alt="Sample Image">
    <p><a href="https://flask.palletsprojects.com/">Learn More About Flask</a></p>
</body>
</html>
"""

@app.route("/")
def hello():
    # Render the HTML template
    return render_template_string(template)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
