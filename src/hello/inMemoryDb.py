from hello.core import IDb, IDataReader, Tuple, Place
import asyncio

class InMemoryDb(IDb):

    def __init__(self, reader: IDataReader):
        self._reader :IDataReader = reader
        self._data : Tuple[Place, ...] = None
        self._loadtask = None

    def data(self) -> Tuple[Place, ...]: 

        # Tuple is an immutable type of array.  This will help us reduce the
        # surface of operations on the collection.
        return self._data

    async def loadAsync(self):

        def loadcore():
            result : list = self._reader.readAll()
            self._data = tuple(result)

        loop = asyncio.get_event_loop()
        self._loadtask = loop.run_in_executor(None, loadcore)
        

    