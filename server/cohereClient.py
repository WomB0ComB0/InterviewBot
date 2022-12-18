import cohere
from server.db.schema import SentimentType
from typing import Tuple

DEFAULT_MODEL_SIZE = "medium"


class CohereClient:
    def __init__(self, apiKey) -> None:
        self.client = cohere.Client(apiKey)

    def get_analysis(
        self, exampleResponses, actualResponse
    ) -> Tuple[int, SentimentType]:
        response = self.client.classify(
            model=DEFAULT_MODEL_SIZE,
            inputs=[actualResponse],
            examples=exampleResponses,
        )

        result = response.classifications[0]

        sentiment = SentimentType.value_of(result.prediction.lower())
        score = result.confidence * 100

        if sentiment == SentimentType.BAD:
            score = 100 - score

        return score, sentiment
