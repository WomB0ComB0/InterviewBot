from flask import Flask
from waitress import serve
from server.resources.interview import InterviewResource
from server.utils import new_logger


class App(Flask):
    def __init__(self, interview_resource: InterviewResource):
        super().__init__(__name__)
        self.register_blueprint(interview_resource, url_prefix="/api")
        self.log = new_logger(__name__)

    def start(self, host: str, port: int):
        self.log.info(f"server {host} running on port {port}")
        serve(self, host=host, port=port)


if __name__ == "__main__":
    ir = InterviewResource()
    server = App(ir)
    server.start("localhost", 8009)
