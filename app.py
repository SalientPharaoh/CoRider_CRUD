from flask import Flask, request, jsonify
from database import * #contains the database initialization code

app = Flask(__name__)
#initializing the database connection
db= database().collection
app.logger.info('Database connection established.')

@app.route('/users', methods=['GET','POST'])
def users():
    #adding the data if a POST request is made
    if request.method == "POST":
        try:
            data = request.get_json()
            #checking whether the entry is already present
            result = db.count_documents({'id':data['id']})
            if result == 1:
                return jsonify({"message": "Data already present"}), 404
            #Adding the data to the database
            new_document = {
                "id": data['id'],
                "name": data['name'],
                "email": data['email'],
                "password" : data['password']
            }
            insert_result = db.insert_one(new_document)
            return jsonify({"message": "Data added successfully"}), 200
        except Exception as e:
            app.logger.error(f'Error: {e}')
            return jsonify({"error": str(e)}), 400

    #returning all the data in database in case of GET request
    elif request.method == "GET":
        try:
            #checking whether the database is empty
            if db.count_documents({})==0:
                return jsonify({"message": "Empty user resources"}), 404
            #returning the all data present in the database
            data = db.find({})
            return jsonify(get_list(data)),200
        except Exception as e:
            app.logger.error(f'Error: {e}')
            return jsonify({"error": str(e)}), 400

@app.route('/users/<string:id>', methods=['PUT'])
def users_query(id):
    #updating the details of a specific user
    if request.method == "PUT":
        try:
            update_data = request.get_json()
            #checking whether the document exists in database
            if db.count_documents({"id": id}) == 1:
                result = db.update_one({"id": id}, {"$set": update_data})
                return jsonify({"message": "Data updated successfully"}), 200
            else:
                return jsonify({"message": "Document not found"}), 404

        except Exception as e:
            app.logger.error(f'Error: {e}')
            return jsonify({"error": str(e)}), 400


@app.route('/users/<string:id>', methods=['GET'])
def get_user(id):
    #retrieving specific document from the database based on usear id
   if request.method == "GET":
        try:
            query = {'id': id}
            if db.count_documents(query)!=0:
                result = db.find(query)
                return jsonify(get_list(result)), 200
            else:
                return jsonify({"message": "Document not found"}), 404
        except Exception as e:
            app.logger.error(f'Error: {e}')
            return jsonify({"error": str(e)}), 400


@app.route('/users/<string:id>', methods=['DELETE'])
def delete_user(id):
    #deleting the document when the method is DELETE
    if request.method == "DELETE":
        try:
            result = db.delete_one({"id": id})
            if result.deleted_count == 1:
                return jsonify({"message": "Document deleted successfully"}), 200
            else:
                return jsonify({"message": "Document not found"}), 404

        except Exception as e:
            app.logger.error(f'Error: {e}')
            return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True)