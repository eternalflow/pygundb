import os
from gundb.server import app
from gundb.gunrequesthandler import GUNRequestHandler

HOST = os.getenv('HOST', '0.0.0.0').strip()
PORT = int(os.getenv('PORT', '8080').strip())


def build_app(backend):
    app.config["handler"] = GUNRequestHandler(backend)
    app.config['HOST'] = HOST
    app.config['PORT'] = PORT
    return app
