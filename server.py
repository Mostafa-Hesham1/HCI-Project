from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from pymongo import MongoClient
from config import Config
from routes.patients import patients_bp
from routes.injuries import injuries_bp
from routes.exercises import exercises_bp
# from TUIO import socketio

app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

# Initialize SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

# MongoDB connection
client = MongoClient('mongodb+srv://mostafaahesham12:TtqslmSrekYVVjzy@hci.xfv9n.mongodb.net/recovery_hub?retryWrites=true&w=majority&appName=Hci')
db = client['recovery_hub']
patients_collection = db['patients']
injuries_collection = db['injuries']
exercises_collection = db['exercises']

def test_db_connection():
    try:
        print("Attempting to connect to the database...")
        # Attempt to list the collections in the database
        collections = db.list_collection_names()
        print("Connected to the database. Collections:", collections)
    except Exception as e:
        print("Failed to connect to the database:", e)

# Register Blueprints
app.register_blueprint(patients_bp)
app.register_blueprint(injuries_bp)
app.register_blueprint(exercises_bp)

@app.route('/')
def index():
    return "TUIO Server Running"

@app.route('/tuio_event', methods=['POST'])
def tuio_event():
    data = request.json
    print('Received TUIO message:', data['message'])
    socketio.emit('tuio_event', data)
    return "Message received", 200

@app.route('/patients', methods=['GET'])
def get_patients():
    try:
        patients = list(patients_collection.find({}, {'_id': 0}))
        return jsonify(patients), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/patients', methods=['POST'])
def add_patient():
    try:
        data = request.json
        print("Received data:", data)  # Add this line to log the received data
        if not data.get("name") or not data.get("injury") or not data.get("exercises"):
            return jsonify({"error": "Missing required fields"}), 400

        patient = {
            "name": data["name"],
            "injury": data["injury"],
            "exercises": data["exercises"]  # List of exercises with sets and reps
        }
        print("Patient to insert:", patient)  # Add this line to log the patient data to be inserted
        patients_collection.insert_one(patient)
        patient['_id'] = str(patient['_id'])  # Convert ObjectId to string
        return jsonify({"message": "Patient added successfully", "patient": patient}), 201
    except Exception as e:
        print("Error:", e)  # Add this line to log the error
        return jsonify({"error": str(e)}), 500

@app.route('/patients/<patient_id>', methods=['PUT'])
def update_patient(patient_id):
    try:
        data = request.json
        result = patients_collection.update_one({'_id': ObjectId(patient_id)}, {'$set': data})
        if result.matched_count == 0:
            return jsonify({"error": "Patient not found"}), 404
        updated_patient = patients_collection.find_one({'_id': ObjectId(patient_id)}, {'_id': 1, 'name': 1, 'injury': 1, 'exercises': 1})
        updated_patient['_id'] = str(updated_patient['_id'])  # Convert ObjectId to string
        return jsonify(updated_patient), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/patients/<patient_id>', methods=['DELETE'])
def delete_patient(patient_id):
    try:
        result = patients_collection.delete_one({'_id': ObjectId(patient_id)})
        if result.deleted_count == 0:
            return jsonify({"error": "Patient not found"}), 404
        return jsonify({"message": "Patient deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Test the database connection
    test_db_connection()
    
    # socketio.init_app(app, cors_allowed_origins="*")
    socketio.run(app, host='0.0.0.0', port=5000)