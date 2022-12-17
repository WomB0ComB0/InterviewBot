from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from server.db.schema import Prompt, Response


class DbClient():
    def __init__(self, address) -> None:
        self.session = Session(create_engine(address))

    def getPrompts(self):
        return self.session.query(Prompt).all()

    def insertPrompt(self, query):
        prompt = Prompt(
            id="",
            query=query,
            createdAt=123
        )
        self.session.add(prompt)
        self.session.commit()

    def getResponses(self, promptId):
        return self.session.query(Response).filter_by(promptId=promptId)

    def insertResponse(self, promptId, content, sentiment):
        response = Response(
            id="",
            promptId=promptId,
            content=content,
            sentiment=sentiment,
            createdAt=123
        )
        self.session.add(response)
        self.session.commit()
