import csv
from typing import Tuple, List
from decimal import Decimal
from hello.core import IDataReader, Place


class TsvPlacesReader(IDataReader):

    def __init__(self, path: str):
        self.path: str = path

    def readAll(self) -> List[Place]:

        placesList: List[Place] = []

        with open(self.path, encoding='utf-8') as tsvFileBin:

            # By reading as a dictionary, we can use the header names as
            # leverage for indexing and better maintainability
            dictionaryReader = csv.DictReader(tsvFileBin,
                                              dialect='excel-tab',
                                              quoting=csv.QUOTE_NONE)

            for row in dictionaryReader:
                place: Place = self.parsePlace(row)
                placesList.append(place)

        return placesList

    def parsePlace(self, row) -> Place:

        name: str = row['name'].strip()
        nameAscii: str = row['ascii'].strip()
        namesAlternatives: Tuple[str, ...] = tuple(
            row['alt_name'].strip().split(','))

        return Place(uid=int(row['id']),
                     name=name,
                     nameAscii=nameAscii,
                     namesAlternatives=namesAlternatives,
                     country=row['country'].strip(),
                     latitude=Decimal(row['lat']),
                     longitude=Decimal(row['long']))
