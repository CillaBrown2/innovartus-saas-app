from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
   return "<h1>Welcome to Innovartus SaaS Platform 🚀</h1><p>✅ CI/CD IS WORKING PERFECTLY!</p>"

if __name__ == "__main__":
    app.run(debug=True)