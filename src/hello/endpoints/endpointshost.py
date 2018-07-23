# Encapsulates Flask to minimize its spread and coupling through the application
from flask import Flask
from flask_restplus import Api


class EndpointsHost:

    def __init__(self, app: Flask, api: Api):
        self.app: Flask = app
        self.api: Api = api

    def run(self, serverHost: str, port: int) -> None:
        self.loadendpoints()
        self.app.run(serverHost, port, use_reloader=True)

    def loadendpoints(self) -> None:
        import hello.endpoints.suggestions
