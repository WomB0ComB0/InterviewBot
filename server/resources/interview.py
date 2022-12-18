from flask import Blueprint, jsonify, Response, request
from server.cohere.client import CohereClient
from server.db.client import DbClient

# resource to handle the endpoints related to interviewing
class InterviewResource(Blueprint):
    def __init__(self, cohere_client: CohereClient, db_client: DbClient):
        super().__init__("interview", __name__)
        self.cohere_client = cohere_client
        self.db_client = db_client
        # configuring routes
        self.add_url_rule("/prompts", view_func=self.get_prompts, methods=["GET"])
        self.add_url_rule("/answer", view_func=self.answer_prompt, methods=["POST"])

    def get_prompts(self) -> Response:
        prompts = self.db_client.get_prompts()
        res = [prompt.to_dict() for prompt in prompts]
        return jsonify(data=res)

    def answer_prompt(self) -> Response:
        return {"score": 99}
