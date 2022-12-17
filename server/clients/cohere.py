import cohere

DEFAULT_MODEL_SIZE = "medium"


class CohereClient:
    def __init__(self, apiKey):
        self.client = cohere.Client(apiKey)

    def get_score(self, example_responses, actual_response):
        response = self.client.classify(
            model=DEFAULT_MODEL_SIZE,
            inputs=[actual_response],
            examples=example_responses,
        )

        result = response.classifications[0]

        sentiment = result.prediction
        score = result.confidence * 100

        if sentiment == "Bad":
            score = 100 - score

        return score
