from flask import Flask, render_template, jsonify, request
import random, time

app = Flask(__name__)
users = [] # local storage

car_data = {"car_id": "CAR-001", "lat": 4.0511, "lng": 9.7679, "speed": 0}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/register', methods=['POST'])
def register():
    data = request.json
    users.append(data)
    print(f"New User: {data}")
    return jsonify({"status": "success", "message": "Account created"})

@app.route('/api/login', methods=['POST'])
def login():
    return jsonify({"status": "success", "message": "Logged in"})

@app.route('/api/location')
def get_location():
    car_data['lat'] += random.uniform(-0.0005, 0.0005)
    car_data['lng'] += random.uniform(-0.0005, 0.0005)
    car_data['speed'] = random.randint(0, 80)
    car_data['last_update'] = time.strftime("%H:%M:%S")
    return jsonify(car_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
