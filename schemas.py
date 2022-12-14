from marshmallow import Schema, fields

class ItemSchema(Schema):
    #used for post to take input *required*
    name = fields.Str(required=True)
    price = fields.Int(required=True)

class ItemGetSchema(Schema):
    #used for get to show data *dump only = only show*
    id = fields.Str(dump_only=True)
    name = fields.Str(dump_only=True)
    price = fields.Int(dump_only=True)

class SuccessMessage(Schema):
    #used to show success message
    Message = fields.Str(dump_only=True)

class ItemQuerySchema(Schema):
    #used to lookup the data using id which is *required*
    id = fields.Str(required=True)

class ItemOptionalQuerySchema(Schema):
    #used in get
    id = fields.Str(required=False)

class UserSchema(Schema):
    #used for get to show data
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(load_only=True)

class UserQuerySchema(Schema):
    #used to get id *arguments*
    id = fields.Int(required=True)
