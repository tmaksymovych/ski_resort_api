from flask import Flask, request, jsonify, abort
from datetime import datetime

app = Flask(__name__)

visitors_db = [
    {"id": 1, "name": "John Doe", "email": "qwerty555@example.com", "registration_date": datetime.now().isoformat()}
    ]
SkiPasses_db = [
    {"id": 101, "visitor_id": 1, "type": "day", "valid_from": datetime.now().isoformat(), "valid_to": (datetime.now()).isoformat()}
    ]  

@app.route('/visitors', methods=['GET'])
def get_visitors():
    limit = int(request.args.get('limit', 10))
    return jsonify(visitors_db[:limit]), 200

@app.route('/visitors', methods=['POST'])
def create_visitor():
    data = request.get_json()
    
    new_visitor = {
        "id": len(visitors_db) + 1,
        "name": data.get("name"),
        "email": data.get("email"),
        "registration_date": datetime.now().isoformat()
    }
    visitors_db.append(new_visitor)
    return jsonify(new_visitor), 201

@app.route('/visitors/<int:visitor_id>/ski-passes', methods=['GET'])
def get_ski_passes(visitor_id):
    SkiPasses = [x for x in SkiPasses_db if x["visitor_id"] == visitor_id]
    return jsonify(SkiPasses), 200

@app.route('/visitors/<int:visitor_id>/ski-passes', methods=['POST'])
def purchase_SkiPass(visitor_id):    
    data = request.get_json()

    new_SkiPass = {
        "id": len(SkiPasses_db) + 101,
        "visitor_id": visitor_id,
        "type": data.get("type"),
        "valid_from": datetime.now().isoformat(),
        "valid_to": (datetime.now()).isoformat()
    }
    SkiPasses_db.append(new_SkiPass)
    return jsonify(new_SkiPass), 201

if __name__ == '__main__':
    app.run(debug=True)