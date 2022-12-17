import cohere

DEFAULT_MODEL_SIZE = "medium"


class CohereClient:
    def __init__(self, apiKey) -> None:
        self.client = cohere.Client(apiKey)

    def get_score(self, exampleResponses, actualResponse):
        response = self.client.classify(
            model=DEFAULT_MODEL_SIZE,
            inputs=[actualResponse],
            examples=exampleResponses,
        )

        result = response.classifications[0]

        sentiment = result.prediction
        score = result.confidence * 100

        if sentiment == "Bad":
            score = 100 - score

        return score
