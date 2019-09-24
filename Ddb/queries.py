

class Query(object):
    def __init__(self):
        """
        """
        self._path = () # keeps track of attribute path

    def __getattr__(self, item):
        query = type(self)()
        query._path = self._path + (item, ) # update path to include item
        return query # return back query so we can chain getattr calls like key1.key2.key3
    
    def _create_query(self, comparison_func):
        """ Wrapper around common method of creating a query from a specific comparison
        """
        def query(value):
            try:
                for key in self._path:
                    value = value[key]
            except (KeyError, TypeError):
                return False
            else:
                return comparison_func(value)
        
        return query

    def __eq__(self, rhs):
        """ get a function to call on every document using the provided path
        """
        return self._create_query( lambda value : value == rhs)
    
    def __ne__(self, rhs):
        """ compare against !=
        """
        return self._create_query( lambda value : value != rhs)

    def __lt__(self, rhs):
        """ compare against < rhs
        """
        return self._create_query( lambda value : value < rhs)

    def __le__(self, rhs):
        """ compare against <= rhs
        """
        return self._create_query( lambda value : value <= rhs)
        
    def __gt__(self, rhs):
        """ compare against > rhs
        """
        return self._create_query( lambda value : value > rhs)

    def __ge__(self, rhs):
        """ compare against >= rhs
        """
        return self._create_query( lambda value : value >= rhs)
    
    def _in(self, rhs):
        """ check if value is contained in the provided list
        """
        return self._create_query( lambda value : value in rhs)

    def _contains(self, rhs):
        """ check if rhs is contained in the value
        """
        return self._create_query( lambda value : rhs in value)
