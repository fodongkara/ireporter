from datetime import datetime

class Incident:
    """ model class for red-flags """

    def __init__(self, status="draft", **kwargs):
        self.createdOn = datetime.now()
        self.createdBy = kwargs["createdBy"]
        self.type = kwargs["type"]
        self.location = kwargs["incident_location"]
        self.status = status
        self.Images = []
        self.Videos = []
        self.comment = kwargs["comment"]
