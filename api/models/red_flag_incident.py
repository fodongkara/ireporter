from datetime import datetime

my_red_flags = []


class Redflag:
    """ model class for red-flags """

    def __init__(self, **kwargs):
        self._id = len(my_red_flags)+1
        self.createdOn = datetime.now()
        self.createdBy = kwargs["createdBy"]
        self.type = kwargs["type"]
        self.location = kwargs["place"]
        self.status = kwargs["status"]
        self.Images = kwargs["Images"]
        self.Videos = kwargs["Videos"]
        self.comment = kwargs["comment"]

    def format_record(self):
        """ Method that returns dictionary representation of the object """
        return {
            "id": self._id,
            "createdOn": self.createdOn,
            "createdBy": self.createdBy,
            "type": self.type,
            "location": self.location,
            "status": self.status,
            "Images": self.Images,
            "Videos": self.Videos,
            "comment": self.comment
        }
