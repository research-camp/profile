from flask import Flask
import argparse



# create a flag parser
parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", help="http port", type=int)
args = parser.parse_args()

# create a new flask app
app = Flask(__name__)



@app.route("/", methods=['GET'])
def root():
    return "OK!"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=args.port)
