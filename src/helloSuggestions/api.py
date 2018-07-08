from helloSuggestions import app, searchEngine
from .place import Place
from .serialisationHelper import toJSON
from typing import Tuple
from flask import request

#REST Api.  I found a lot of REST libraries for Flask.  However, since the
#problem don't have a lot of requirements I decided not to add unecessary
#dependencies.

@app.route('/suggestions', methods=['GET']) # method decoration that links the route to the service
def suggestions() -> str:
    query = request.args.get('q')
    places : Tuple[Place] = searchEngine.search(query)
    return toJSON(places)
