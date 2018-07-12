from typing import Tuple
from .place import Place

# Interface for data access
class IDb(object):
    def data(self) -> Tuple[Place]:
        raise NotImplementedError

s = Place #shortcut alias to improve readability of the strings

class InMemoryDb(IDb):
    def data(self) -> Tuple[Place, ...]: 

        # It seems that Tuple is an immutable type of array.  This will help us
        # to reduce the surface of available operations.

        # The access to the collection is a method instead of an attribute
        # since we want to avoid modifications of items inside the collection.
            # Despite the fact that we are using an immutable reference for the
            # Tuple (and so are the pointers to the references of each item),
            # the items are stored onto the heap and each item itself can have
            # its properties changed on the outside.

            # Apparently there is also no notion of accessors other than
            # public.  It seems to me that pyhton's philosophy is to trust on
            # the developer.  Maybe it's just a shift of perception that's
            # needed, but this kind of openess is a little odd for me, since it
            # might open space to some unwanted, non-orthodox creativity from
            # unexperienced developers.

        return (s("Gotham City"),
            s("Bikini bottom"),
            s("The Shire"),
            s("Tatooine"))
