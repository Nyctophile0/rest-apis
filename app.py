from flask import Flask
from resources.item import blp as ItemBluePrint
from resources.user import blp as UserBluePrint
from flask_smorest import Api

app = Flask(__name__) #constructor of this class

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Items Rest API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

#@app.get("/items")
#def getitems():
#    return {"Items": items} #return only keys

api = Api(app)

api.register_blueprint(ItemBluePrint)
api.register_blueprint(UserBluePrint)