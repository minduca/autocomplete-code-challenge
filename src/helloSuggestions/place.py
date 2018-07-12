from typing import List
from decimal import Decimal

# Apparently there is also no notion of accessors other than
    # public.  It seems to me that pyhton's philosophy is to trust on
    # the developer.  Maybe it's just a shift of perception that's
    # needed, but this kind of openess is a little odd for me, since it
    # might open space to some unwanted, non-orthodox creativity from
    # unexperienced developers.

# There are some "tweaks" and "workarounds" that emulates immutability by
    # inheriting from Tuple and overriding a couple of things.  For simplicity
    # purposes, I will ignore this issue for now.

class Place(object):
    
    def __init__(self, id:int, name: str, nameAscii:str, nameAlternative: str, country: str, latitude: Decimal, longitude: Decimal):
        self.name : str = name
        self.nameAscii :str = nameAscii
        self.nameAlternative : str = nameAlternative
        self.country : str = country
        self.latitude : Decimal = latitude
        self.longitude :Decimal = longitude

