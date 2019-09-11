
class Datastore(object):
    """ Data storage for database operations. Basically a wrapper around json
    """
    def __init__(self, file_name):
        pass

class Database(object):
    def __init__(self, datafile: str):
        """
            Create instance of the database.

            :param datafile: name of the location to store the data ex: 'data.json'
        """
        self._storage = Datastore(datafile)
    
    def table(self, table_name:str ):
        """
            Creates a table if it doesn't exist and return it to the user.
        """
        pass