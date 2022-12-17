from flask import Blueprint


class InterviewResource(Blueprint):
    def __init__(self):
        super().__init__("interview", __name__)
        self.add_url_rule("/prompts", view_func=self.get_prompts, methods=["GET"])
        self.add_url_rule("/answer", view_func=self.answer_prompt, methods=["POST"])

    def get_prompts(self):
        return {}

    def answer_prompt(self):
        return {}
