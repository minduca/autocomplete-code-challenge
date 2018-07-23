## search (application component)
This component handles the search at application level. It contains :

- A ```PlaceSearchEngine``` that manages the whole flow of the search with the help of many different implementations of ```IResultHandler```.
- A ```IPlaceSearchQueryStrategy``` implementation that that handles the **query** part of the search.

### Main scores of the search
- Score by word approximation
- Score by coordinates approximation
- Score by population size
