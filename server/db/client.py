# dummy client

class DbClient():
    def __init__(self) -> None:
        pass

    def getPrompts(self):
        pass

    def insertPrompt(self, query):
        pass

    def getResponses(self, promptId):
        pass

    def insertResponse(self, promptId, content, sentiment):
        pass
