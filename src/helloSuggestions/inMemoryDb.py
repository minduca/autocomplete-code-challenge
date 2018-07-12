from helloSuggestions.core import IDb, IDataReader, Tuple, Place
import asyncio

s = Place #shortcut alias to improve readability of the strings
class InMemoryDb(IDb):

    def __init__(self, reader: IDataReader):
        self._reader :IDataReader = reader
        self._data : Tuple[Place, ...] = None
        self._loadtask = None

    def data(self) -> Tuple[Place, ...]: 

        # It seems that Tuple is an immutable type of array.  This will help us
        # to reduce the surface of available operations.
        return self._data

    async def loadAsync(self):

        def loadcore():
            result : list = self._reader.readAll()
            self._data = tuple(result)

        loop = asyncio.get_event_loop()
        self._loadtask = loop.run_in_executor(None, loadcore)
        

    