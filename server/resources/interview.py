from flask import Blueprint, jsonify, Response
from server.clients.cohere import CohereClient

# resource to handle the endpoints related to interviewing
class InterviewResource(Blueprint):
    def __init__(self, cohere_client: CohereClient):
        super().__init__("interview", __name__)
        self.cohere_client = cohere_client
        self.add_url_rule("/prompts", view_func=self.get_prompts, methods=["GET"])
        self.add_url_rule("/answer", view_func=self.answer_prompt, methods=["POST"])

    # TODO: implement
    def get_prompts(self) -> Response:
        return jsonify(prompts=["prompt1", "prompt2", "prompt3"])

    # TODO: implement
    def answer_prompt(self) -> Response:
        return {"score": 99}
