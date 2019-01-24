from flask import jsonify, request
from api.models.incident import Incident
from api.utility.validation import ValidateRecord


class RedflagController():
    def __init__(self):
        pass

    def home(self):
        return jsonify({
            'message': 'Welcome to ernest\'s iReporter app.',
            'status': '200'
        }), 200

    def create_redflag(self):
        data = request.get_json()

        created_by = data.get("createdBy")
        incident_type = data.get("type")
        red_flag_status = data.get("status")
        images = data.get("Images")
        red_flag_location = data.get("location")
        videos = data.get("Videos")
        comments = data.get("comment")

        if not created_by or not incident_type or not red_flag_location \
                or not red_flag_status or not images \
                or not videos or not comments:
            return jsonify({
                "Error": "Required field is missing"
            }), 400

        for comment in my_red_flags:
            if comment["comment"] == comments:
                return jsonify({
                    "Error": "Redflag record exists",
                    "status": 400

                }), 400

        if not ValidateRecord.validate_type(incident_type):
            return jsonify({'status': 400,
                            'Error': 'type must a string and must be a red-flag'
                            }), 400
        if not ValidateRecord.validate_comment(comments):
            return jsonify({'status': 400,
                            'error': 'comment must be a string'}), 400

        if not ValidateRecord.validate_status(red_flag_status):
            return jsonify({'status': 400,
                            'error': "Status must either be resolved, rejected or under investigation"
                            }), 400
        if not ValidateRecord.validate_location(red_flag_location):
            return jsonify({'status': 400,
                            'error': 'Location field only takes in a list of valid Lat and Long cordinates'
                            }), 400

        red_flag = Redflag(createdBy=created_by, type=incident_type,
                           place=red_flag_location, status=red_flag_status,
                           Images=images, Videos=videos, comment=comments)

        my_red_flags.append(
            red_flag.format_record()
        )

        if len(my_red_flags) == 0:
            return jsonify({
                "status": 400,
                "Error": "Invalid request"
            }), 400
        return jsonify({
            "data": red_flag.format_record(),
            "status": 201,
            "Message": "Created red-flag record"
        }), 201

    def get_all_red_flags(self):
        if len(my_red_flags) > 0:
            return jsonify({
                "status": 200,
                "data": [red_flag for red_flag in my_red_flags]
            }), 200
        return jsonify({
            "status": 400,
            "Error": "There are no records"
        })

    def get_a_redflag(self, flag_id):
        red_flag_record = [
            red_flag for red_flag in my_red_flags if red_flag['id'] == flag_id]
        if red_flag_record:
            return jsonify({
                "status": 200,
                "redflag": red_flag_record
            }), 200
        return jsonify({
            "status": 404,
            "Error": " Record does not exist"
        }), 404

    def delete_red_flag(self, flag_id):
        red_flag_record = [
            flag for flag in my_red_flags if flag['id'] == flag_id]
        if len(my_red_flags) == 0:
            return jsonify({
                "status": "200",
                "Error": "There is nothing found"
            }), 200
        my_red_flags.remove(red_flag_record[0])
        return jsonify({
            'Result': "record was deleted successfully"
        }), 200

    def edit_red_flag_location(self, flag_id):
        data = request.get_json()
        for red_flag_record in my_red_flags:
            if red_flag_record['id'] == flag_id:
                red_flag_record["location"] = data["location"]
                return jsonify({
                    "data": red_flag_record,
                    "status": 200,
                    "message": "Updated red-flag's record location"
                }), 200
            if not red_flag_record:
                return jsonify({
                    "status": "400",
                    "Error": "Red flag is not available"
                }), 400

    def edit_red_flag_comment(self, flag_id):
        data = request.get_json()
        for red_flag_record in my_red_flags:
            if red_flag_record['id'] == flag_id:
                red_flag_record["comment"] = data["comment"]
                return jsonify({
                    "data": red_flag_record,
                    "status": 200,
                    "message": "Updated red-flag's record comment"
                }), 200
            if not red_flag_record:
                return jsonify({
                    "status": "400",
                    "Error": "Red flag is not available"
                })
