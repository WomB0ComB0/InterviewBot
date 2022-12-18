from flask import Blueprint, jsonify, Response, request
from app.clients.cohere import CohereClient
from app.clients.db import DbClient

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
        body = request.json

        prompt_id = body.get("promptId")
        answer = body.get("answer")

        if prompt_id is None:
            return jsonify(message="promptId must be specified"), 400

        if answer is None:
            return jsonify(message="answer must be specified"), 400

        existing_prompt = self.db_client.get_prompt(prompt_id)
        if existing_prompt is None:
            return jsonify(message=f"prompt {prompt_id} does not exist"), 404

        sample_responses = self.db_client.get_responses(prompt_id)

        score, sentiment = self.cohere_client.get_analysis(sample_responses, answer)

        self.db_client.insert_response(prompt_id, answer, sentiment)

        return jsonify(score=score)
