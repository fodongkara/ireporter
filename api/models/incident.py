from datetime import datetime


class Incident:
    """ model class for red-flags """

    def __init__(self, **kwargs):
        self.createdOn = datetime.now()
        self.createdBy = kwargs["createdBy"]
        self.type = kwargs["type"]
        self.location = kwargs["place"]
        self.status = kwargs["status"]
        self.Images = kwargs["Images"]
        self.Videos = kwargs["Videos"]
        self.comment = kwargs["comment"]
