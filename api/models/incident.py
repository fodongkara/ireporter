from datetime import datetime


class Incident:
    """ model class for red-flags """

    def __init__(self, status="draft", **kwargs):
        self.createdOn = kwargs["createdOn"]
        self.createdBy = kwargs["createdBy"]
        self.type = kwargs["type"]
        self.location = kwargs["place"]
        self.status = "draft"
        self.Images = []
        self.Videos = []
        self.comment = kwargs["comment"]
