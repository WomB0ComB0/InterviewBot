from flask import Flask
from waitress import serve
from server.resources.interview import InterviewResource
from server.utils import new_logger


# represents out REST server
class App(Flask):
    def __init__(self, interview_resource: InterviewResource):
        super().__init__(__name__)
        self.log = new_logger(__name__)
        self.register_blueprint(interview_resource, url_prefix="/api/interview")

    def start(self, host: str, port: int):
        self.log.info(f"host {host} running on port {port}")
        serve(self, host=host, port=port)


# TODO: make this take in command
if __name__ == "__main__":
    ir = InterviewResource()
    server = App(ir)
    server.start("localhost", 8009)
