## autocomplete (independent module)
This module is a generic component that I made whilist building my solution to this code challenge. 

It basically contains a ```Trie``` data structure (aka prefix tree, radix tree) that also implements word approximation by computing the Levenshtein distance between its nodes.
- This data structure can insert with O(log(n)) and search with O(log(n)) + the complexity of the levenshtein distance. 
- The current implementation of the levenshtein algorithm adds only a small overhead. It computes with a worst case scenario of O(maxWordLength * totalNumberOfNodes), average of O(totalNumberOfWords * maxWordLength^2). For the insight of this very reasonable time complexity, I give the credits to [Steve Hanov's Blog](http://stevehanov.ca/blog/index.php?id=114).
- The result of the search (only the words that match the query) is sorted by score with O(n log(n)) at the very end of the search.

This module also contains an implementation for data normalization that scales/aggregates score results to the range of 0-1.

(Once I stabilize this module with better tests, I will problably update it to PyPI's index.)
