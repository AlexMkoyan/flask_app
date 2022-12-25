from flask import Flask
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--dev", help="development mode")
parser.add_argument("--prod", help="production mode")
args = parser.parse_args()

app = Flask(__name__)

@app.route("/")

def hello_world():
    return "<p>Hellooooooooo, World!</p>"

if __name__ == "__main__":
    if args.dev:
        app.run(host="0.0.0.0", port=int("3000"),debug=True)
    elif args.prod:
        app.run(host="0.0.0.0", port=int("3000"),debug=False)

# python3 ./index.py --dev or --prod 1
