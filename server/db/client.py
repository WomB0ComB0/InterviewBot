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

    def get_prompt(self, id: str) -> Optional[Prompt]:
        return self.session.query(Prompt).filter_by(id=id).one_or_none()

    def insert_prompt(self, query: str):
        prompt = Prompt(id=generate_uuid(), query=query, createdAt=time_now())
        self.session.add(prompt)
        self.session.commit()

    def get_responses(self, prompt_id: str) -> List[Response]:
        return self.session.query(Response).filter_by(promptId=prompt_id)

    def insert_response(self, prompt_id: str, content: str, sentiment: SentimentType):
        response = Response(
            id=generate_uuid(),
            promptId=prompt_id,
            content=content,
            sentiment=sentiment,
            createdAt=time_now(),
        )

        self.session.add(response)
        self.session.commit()
