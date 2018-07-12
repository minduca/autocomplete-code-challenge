from typing import List
from decimal import Decimal

class Place(object):
    
    def __init__(self, id:int, name: str, nameAscii:str, nameAlternative: str, country: str, latitude: Decimal, longitude: Decimal):
        self.name : str = name
        self.nameAscii :str = nameAscii
        self.nameAlternative : str = nameAlternative
        self.country : str = country
        self.latitude : Decimal = latitude
        self.longitude :Decimal = longitude
#todo


