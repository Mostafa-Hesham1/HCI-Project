from flask import Blueprint, request, jsonify
from models.patient import patients_collection
from bson import ObjectId

patients_bp = Blueprint('patients', __name__)

@patients_bp.route('/api/patients', methods=['GET', 'POST'])
def patients():
    if request.method == 'GET':
        try:
            patients = list(patients_collection.find({}, {'_id': 1, 'name': 1, 'injury': 1, 'exercises': 1}))
            for patient in patients:
                patient['_id'] = str(patient['_id'])  # Convert ObjectId to string
                for exercise in patient.get('exercises', []):
                    if isinstance(exercise, dict) and '_id' in exercise:
                        exercise['_id'] = str(exercise['_id'])  # Convert ObjectId to string in exercises
            return jsonify(patients)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    elif request.method == 'POST':
        try:
            data = request.json
            patient = {
                "name": data["name"],
                "injury": data["injury"],
                "exercises": data["exercises"]  # List of exercises with sets and reps
            }
            result = patients_collection.insert_one(patient)
            patient['_id'] = str(result.inserted_id)  # Correctly retrieve the ObjectId and convert it
            return jsonify(patient), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@patients_bp.route('/api/patients/<patient_id>', methods=['PUT'])
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
