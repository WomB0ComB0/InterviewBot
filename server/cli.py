from server.config import AppConfig
from server.resources.interview import InterviewResource
from server.cohere.client import CohereClient
from server.db.client import DbClient
from server.app import App
import click


@click.group()
def cmdln():
    pass


@cmdln.command("runserver")
@click.option("--env")
def runserver(env):
    cfg = AppConfig.new_config(env)

    cohere_client = CohereClient(cfg.cohere_api_key)
    db_client = DbClient(cfg.db_address)

    interview_resource = InterviewResource(cohere_client)

    app = App(interview_resource)

    app.start(cfg.app_host, cfg.app_port)


if __name__ == "__main__":
    cmdln()
