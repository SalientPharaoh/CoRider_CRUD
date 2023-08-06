from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from database import *


app = Flask(__name__)
api = Api(app)

class User(Resource):
    def __init__(self):
        self.db= database().collection
        app.logger.info('Database connection established.')

    def post(self, id=None):
    #adding the data if a POST request is made
        try:
            data = request.get_json()
            #checking whether the entry is already present
            result = self.db.count_documents({'id':data['id']})
            if result == 1:
                return {"message": "Data already present"}, 404
            #Adding the data to the database
            new_document = {
                "id": data['id'],
                "name": data['name'],
                "email": data['email'],
                "password" : data['password']
            }
            insert_result = self.db.insert_one(new_document)
            return {"message": "Data added successfully"}, 200
        except Exception as e:
            app.logger.error(f'Error: {e}')
            return {"error": str(e)}, 400

    def get(self, id=None):
    #returning all the data in database in case of GET request
        if id is None:
            try:
                #checking whether the database is empty
                if self.db.count_documents({})==0:
                    return {"message": "Empty user resources"}, 404
                #returning the all data present in the database
                data = self.db.find({})
                return get_list(data),200
            except Exception as e:
                app.logger.error(f'Error: {e}')
                return {"error": str(e)}, 400
        else:
            try:
                query = {'id': id}
                if self.db.count_documents(query)!=0:
                    result = self.db.find(query)
                    return get_list(result), 200
                else:
                    return {"message": "Document not found"}, 404
            except Exception as e:
                app.logger.error(f'Error: {e}')
                return {"error": str(e)}, 400


    def put(self, id):
    #updating the details of a specific user
        try:
            update_data = request.get_json()
            #checking whether the document exists in database
            if self.db.count_documents({"id": id}) == 1:
                result = self.db.update_one({"id": id}, {"$set": update_data})
                return {"message": "Data updated successfully"}, 200
            else:
                return {"message": "Document not found"}, 404

        except Exception as e:
            app.logger.error(f'Error: {e}')
            return {"error": str(e)}, 400

    def delete(self, id):
        try:
            result = self.db.delete_one({"id": id})
            if result.deleted_count == 1:
                return {"message": "Document deleted successfully"}, 200
            else:
                return {"message": "Document not found"}, 404

        except Exception as e:
            app.logger.error(f'Error: {e}')
            return {"error": str(e)}, 400



api.add_resource(User, '/users', '/users/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
