import asyncio
from typing import Tuple, List
from hello.core import IDb, IDataReader, Place

class InMemoryDb(IDb):

    def __init__(self, reader: IDataReader):
        self._reader :IDataReader = reader
        self._data : Tuple[Place, ...] = None
        self._loadtask = None

    async def getAllAsync(self) -> Tuple[Place, ...]: 

        if not self._data:
            if self._loadtask:
                await asyncio.wait([self._loadtask])
            else: 
                self.load()

        return self._data

    async def initAsync(self):
        loop = asyncio.get_event_loop()
        self._loadtask = loop.run_in_executor(None, self.load)

    def load(self):
        # tuple is an immutable type of array.  This will help us reduce the
        # surface of operations on the collection.
        result : List[Place] = self._reader.readAll()
        self._data = tuple(result)
