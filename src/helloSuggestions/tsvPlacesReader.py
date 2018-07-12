import csv
from helloSuggestions.core import IDataReader, Tuple, Place
from decimal import Decimal

class TsvPlacesReader(IDataReader):
    
    def __init__(self, path: str):
        self.path : str = path

    def readAll(self) -> list :

        placesList = []

        with open(self.path, encoding='utf-8') as tsvFileBin:

            # By reading as a dictionary, we can use the header names as
            # leverage for indexing and better maintainability
            dictionaryReader = csv.DictReader(tsvFileBin, dialect='excel-tab', quoting=csv.QUOTE_NONE)

            for row in dictionaryReader:
                place : Place = self.parsePlace(row)
                placesList.append(place)

        return placesList

    def parsePlace(self, row) -> Place:
        return Place(id=int(row['id']), 
                     name=row['name'], 
                     nameAscii=row['ascii'], 
                     nameAlternative=row['alt_name'],
                     country=row['country'],
                     latitude=Decimal(row['lat']),
                     longitude=Decimal(row['long']))

