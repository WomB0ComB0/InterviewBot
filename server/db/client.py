from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from server.db.schema import Prompt, Response, SentimentType
from server.utils import time_now, generate_uuid
from typing import List, Optional


class DbClient:
    def __init__(self, address: str) -> None:
        self.session = Session(create_engine(address))

    def get_prompts(self) -> List[Prompt]:
        return self.session.query(Prompt).all()

    def insert_prompt(self, query: str) -> str:
        id = generate_uuid()
        prompt = Prompt(id=id, query=query, createdAt=time_now())
        self.session.add(prompt)
        self.session.commit()
        return id

    def get_responses(self, prompt_id: str) -> List[Response]:
        return self.session.query(Response).filter_by(promptId=prompt_id)

    def insert_response(
        self, prompt_id: str, content: str, sentiment: SentimentType
    ) -> str:
        id = generate_uuid()

        response = Response(
            id=id,
            promptId=prompt_id,
            content=content,
            sentiment=sentiment,
            createdAt=time_now(),
        )

        self.session.add(response)
        self.session.commit()
        return id
