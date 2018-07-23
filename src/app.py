# Start the application

import asyncio
from os import environ
from hello import run
from hello import settings

from flask import Flask
from flask_restplus import Api

app = Flask(__name__)
api = Api(app, version="1.0", title="Code challenge - Suggestions API")

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', settings.DEFAULT_SERVER_HOST)
    PORT = int(environ.get('SERVER_PORT', settings.DEFAULT_PORT))

    loop = asyncio.get_event_loop()
    task = loop.create_task(run(HOST, PORT, app, api))
    loop.run_until_complete(task)
