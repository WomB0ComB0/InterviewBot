from config import AppConfig
from app.resources.interview import InterviewResource
from app.clients.cohere import CohereClient
from app.clients.db import DbClient
from app.database.schema import SentimentType
from app.server import App
import click
import json


@click.group()
def cmdln():
    pass


@cmdln.command("populate-db")
@click.option("--env")
def populate(env):
    cfg = AppConfig.new_config(env)
    db_client = DbClient(cfg.db_address)

    with open(f"./server/data.json", "r", encoding="utf8") as f:
        data = json.load(f)
        prompts = data["interviewer-reviewer"]

        for prompt in prompts:
            query = prompt["prompt"]
            prompt_id = db_client.insert_prompt(query)
            samples = prompt["sampleResponses"]

            for sample in samples:
                response = sample[0]
                sentiment = SentimentType.value_of(sample[1])
                db_client.insert_response(prompt_id, response, sentiment)


@cmdln.command("runserver")
@click.option("--env")
def runserver(env):
    cfg = AppConfig.new_config(env)

    cohere_client = CohereClient(cfg.cohere_api_key)
    db_client = DbClient(cfg.db_address)

    interview_resource = InterviewResource(cohere_client, db_client)

    app = App(interview_resource)

    app.start(cfg.app_host, cfg.app_port)


if __name__ == "__main__":
    cmdln()
