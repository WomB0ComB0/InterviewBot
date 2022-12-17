from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, BigInteger, Enum
import enum

Base = declarative_base()


class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(String, primary_key=True)
    query = Column(String)
    createdAt = Column(BigInteger)

    def __repr__(self):
        return f"<Prompt(id={self.id}, query={self.query}, createdAt={self.createdAt})"


class SentimentType(enum.Enum):
    BAD = "bad"
    GOOD = "good"


class Response(Base):
    __tablename__ = "responses"

    id = Column(String, primary_key=True)
    promptId = Column(String)
    content = Column(String)
    sentiment = Column(Enum(SentimentType))
    createdAt = Column(BigInteger)

    def __repr__(self):
        return f"<Response(id={self.id}, promptId={self.promptId}, content={self.content},sentiment={self.sentiment}, createdAt={self.createdAt})"
