from db.user import UserDatabase
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import UserSchema, UserQuerySchema, SuccessMessage
import argon2

blp = Blueprint("Users", __name__, description="Operations on Users")

@blp.route("/user")

class Item(MethodView):

    def __init__(self) -> None:
        self.obj = UserDatabase()
        self.ph = argon2.PasswordHasher(time_cost=2, memory_cost=2**15,parallelism=8, hash_len=16, salt_len=16)

    @blp.response(200, UserSchema)
    @blp.arguments(UserQuerySchema, location="query")
    def get(self, args):
        id = args.get('id')
        result = self.obj.get_user(id)
        if result is None:
            abort(404,message="User does not exist.")
        return result


    @blp.arguments(UserSchema)
    #@blp.response(200, SuccessMessage)
    def post(self, request_data):
        username = request_data['username']
        password = self.ph.hash(request_data['password'])
        
        if self.obj.add_user(username, password):
            return {"message": "User added Successfully!"}
        abort(403,message="User already exist.")
        

    @blp.response(200, SuccessMessage)
    @blp.arguments(UserQuerySchema, location="query")
    def delete(self, args):
        id = args.get('id')
        if self.obj.delete_user(id):
            return {"Message": "User deleted successfully!"}
        abort(404, message="User not deleted.")