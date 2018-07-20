# Encapsulates Flask to minimize its spread and coupling through the application
from flask import Flask
from flask_restplus import Api


class EndpointsHost:

    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app, version="1.0",
                       title="Code challenge - Suggestions API")

    def run(self, serverHost: str, port: int) -> None:
        self.loadendpoints()
        self.app.run(serverHost, port)

    def loadendpoints(self) -> None:
        import hello.endpoints.suggestions
