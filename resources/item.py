from flask import request
import uuid
from db.database import ItemDatabase
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import ItemSchema, ItemGetSchema, SuccessMessage, ItemOptionalQuerySchema, ItemQuerySchema

blp = Blueprint("items", __name__, description="Operations on items")

@blp.route("/item")

class Item(MethodView):

    def __init__(self) -> None:
        self.obj = ItemDatabase()

    @blp.response(200, ItemGetSchema(many=True))
    @blp.arguments(ItemOptionalQuerySchema, location="query")
    def get(self, args):
        id = args.get('id')
        if id is None:
            return self.obj.get_items()

        result = self.obj.get_item(id)
        if result is None:
            abort(404,message="Record does not exist.")
        return self.obj.get_item(id)

   
    @blp.arguments(ItemSchema)
    @blp.response(200, SuccessMessage)
    @blp.arguments(ItemQuerySchema, location="query")
    def put(self, request_data, args):
        #request_data = request.get_json()
        id = args.get('id')
        if self.obj.update_item(id, request_data):
            return {"Message": "item updated!"}
        abort(404,message="Item could not be updated.")

   
    @blp.arguments(ItemSchema)
    #@blp.response(200, SuccessMessage)
    def post(self, request_data):
        id = uuid.uuid4().hex
        self.obj.add_item(id, request_data)
        #request_data = request.get_json()
        return {"message": "item added Successfully!"}
        #return {"message": "item already present"}


    @blp.response(200, SuccessMessage)
    @blp.arguments(ItemQuerySchema, location="query")
    def delete(self, args):
        id = args.get('id')
        if self.obj.delete_item(id):
            return {"Message": "Item deleted successfully!"}

        abort(404, message="Item not deleted.")