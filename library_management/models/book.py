from utils.uuid_utils import generate_uuid

class Book:
    def __init__(self,id, title, author, year, status=True):
        self.id:str = id
        self.title:str = title
        self.author:str = author
        self.year:int = year
        self.status:bool = status
