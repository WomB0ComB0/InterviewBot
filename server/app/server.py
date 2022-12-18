from flask import Flask
from waitress import serve
from app.resources.interview import InterviewResource
from app.utils import new_logger


# represents out REST server
class App(Flask):
    def __init__(self, interview_resource: InterviewResource):
        super().__init__(__name__)
        self.log = new_logger(__name__)
        self.register_blueprint(interview_resource, url_prefix="/api/interview")

    def start(self, host: str, port: int):
        self.log.info(f"host {host} running on port {port}")
        serve(self, host=host, port=port)
