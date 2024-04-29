from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from secure_check import authenticate, identity
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'mykey'

# Setup Flask-JWT
#app.config['JWT_SECRET_KEY']
jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != 'test' or password != 'test':
        return {'msg': "Bad username or password"}, 401
    
    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


puppies = []

class PuppyNames(Resource):

    def get(self, name):
        for pup in puppies:
            if pup['name'] == name:
                return pup
        
        return {'name': None}, 404

    def post(self, name):
        pup = {'name': name}
        puppies.append(pup)
        return pup
    

    def delete(self, name):
        for idx, pup in enumerate(puppies):
            if pup['name'] == name:
                deleted_pup = puppies.pop(idx)
                return{'note': 'delete success'}
            
        return {'note': None}
    
class AllNames(Resource):
    
    @jwt_required()
    def get(self):
        return {'puppies': puppies}
    
api.add_resource(PuppyNames, '/puppy/<string:name>')
api.add_resource(AllNames, '/puppies')

if __name__ == "__main__":
    app.run(debug=True)