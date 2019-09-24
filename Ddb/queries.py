

class Query(object):
    def __init__(self):
        """
        """
        self._path = () # keeps track of attribute path

    def __getattr__(self, item):
        query = type(self)()
        query._path = self._path + (item, ) # update path to include item
        return query # return back query so we can chain getattr calls like key1.key2.key3

    def __eq__(self, rhs):
        """ get a function to call on every document using the provided path
        """
        def query(value):
            try:
                for key in self._path:
                    value = value[key]
            except (KeyError, TypeError):
                return False
            else:
                return value == rhs
        return query


    def __lt__(self, rhs):
        """ compare against < rhs
        """
        def query(value):
            try:
                for key in self._path:
                    value = value[key]
            except (KeyError, TypeError):
                return False
            else:
                return value < rhs
        return query
