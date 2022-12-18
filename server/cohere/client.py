import cohere
from cohere.classify import Example
from server.db.schema import SentimentType, Response
from typing import Tuple, List

DEFAULT_MODEL_SIZE = "medium"


class CohereClient:
    def __init__(self, apiKey) -> None:
        self.client = cohere.Client(apiKey)

    def get_analysis(
        self, responses: List[Response], response: str
    ) -> Tuple[int, SentimentType]:
        examples = [
            Example(response.content, response.sentiment.value)
            for response in responses
        ]

        response = self.client.classify(
            model=DEFAULT_MODEL_SIZE,
            inputs=[response],
            examples=examples,
        )

        result = response.classifications[0]

        sentiment = SentimentType.value_of(result.prediction)
        score = result.confidence * 100

        if sentiment == SentimentType.BAD:
            score = 100 - score

        return score, sentiment
