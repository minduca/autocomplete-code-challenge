from typing import Tuple, List
from decimal import Decimal

# Apparently python has no notion of accessors other than
    # public.  It seems to me that pyhton's philosophy is to trust on
    # the developer.  Maybe it's just a shift of perception that's
    # needed, but this kind of openess is a little odd for me, since it
    # might open space to some unwanted, non-orthodox creativity from
    # unexperienced developers.

#About the mutability of an instance from this class :
    
    # I was looking to make this class immutable, since the database is in
    # memory and changing its attributes will make the data dirty.  From what
    # I've found, this is not a explicit feature.  There are
    # some "tweaks" and "workarounds" that emulates immutability in a class,
    # but the code is ugly.  For simplicity purposes, I will ignore this issue
    # for now.

    # Update : Apparently, the Python guideline PEP-08 ("Style Guide for Python
    # Code" - https://www.python.org/dev/peps/pep-0008/) encourages direct
    # access to fields for simplicity purposes, and increment the design as
    # needs arise from the context, as we can see in this little extraction :

        #With this in mind, here are the Pythonic guidelines:
        #...
            #For simple public data attributes, it is best to expose just the
            #attribute name, without complicated accessor/mutator methods.
            #Keep in #mind that Python provides an easy path to future
            #enhancement, should #you find that a simple data attribute needs
            #to grow functional behavior.  In that case, use properties to hide
            #functional implementation behind simple data attribute access
            #syntax.
    
    #It's indeed important not to overdesign, but since this application comes
    #from a code challenge, little extras counts.
class Place(object):
    
    def __init__(self, id:int, name: str, nameAscii:str, namesAlternatives: Tuple[str, ...], country: str, latitude: Decimal, longitude: Decimal):
        self.id : int = id
        self.name : str = name
        self.nameAscii : str = nameAscii
        self.namesAlternatives : Tuple[str, ...] = namesAlternatives
        self.country : str = country
        self.latitude : Decimal = latitude
        self.longitude : Decimal = longitude

    def getAllNames(self) -> list:
        
        allNames: list = list(self.namesAlternatives)

        def appendIfDoesntExist(text: str):
            if not text in allNames:
                allNames.append(text)

        appendIfDoesntExist(self.name)
        appendIfDoesntExist(self.nameAscii)

        return allNames

    def __repr__(self):
        return self.name