import json
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/comps")
@cross_origin()
def comps():
    comps_list = [
        {
            "id": 1,
            "ip": "192.168.0.1",
            "name": "Wolverine",
            "ping": "13"
        },
        {
            "id": 2,
            "ip": "192.168.0.2",
            "name": "Cyclops",
            "ping": "21"
        },
        {
            "id": 3,
            "ip": "192.168.0.3",
            "name": "Jean Grey",
            "ping": "10"
        },
        {
            "id": 4,
            "ip": "192.168.0.4",
            "name": "Rogue",
            "ping": "8"
        }
    ]
    return json.dumps(comps_list)

if __name__ == "__main__":
    app.run(debug=True)