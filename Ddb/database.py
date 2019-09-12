import os
import json
from typing import List

class StorageDriver(object):
    """ Data storage for database operations. Basically a wrapper around json
    """

    def __init__(self, file_name: str):
        self._file_handler = open(file_name, "w+")

    def _read(self) -> dict:
        """ Return rows from the database, if empty, return None
        """
        # Go to file end to get size
        self._file_handler.seek(0, os.SEEK_END)
        size = self._file_handler.tell()

        if size == 0:
            return None

        self._file_handler.seek(0)
        data = json.load(self._file_handler)
        return data

    def _write(self, data: dict):
        """ Write dict data into our datafile
        """
        self._file_handler.seek(0)
        self._file_handler.write(json.dumps(data, indent=4))
        self._file_handler.flush()

        # force file to update and trim excess
        os.fsync(self._file_handler.fileno())
        self._file_handler.truncate()


class Database(object):
    def __init__(self, datafile: str):
        """
            Create instance of the database.

            :param datafile: name of the location to store the data ex: 'data.json'
        """
        self._storage = StorageDriver(datafile)

    def table(self, table_name: str):
        """
            Creates a table if it doesn't exist and return it to the user.
        """
        table = Table(table_name, self._storage)
        return table


class Table(object):
    """ Handles all the read and write operations to the storage driver
    """

    def __init__(self, table_name: str, storage: StorageDriver):
        """ Creates the table
        """
        self._name = table_name
        self._storage = storage

    def insert(self, data: dict):
        """ insert data into our storage driver and only affect THIS table
        """
        table = self._storage._read()
        # Handles empty file case
        if table == None:
            table = {self._name: {"rows": []}}
        # Handles first usage of table case
        if self._name not in table:
            table[self._name] = {"rows": []}
        table[self._name]["rows"].append(data)
        self._storage._write(table)

    def all(self) -> List[dict]:
        """ Get all documents stored in table.

            :returns: a list of documents
            :rtype: list[dict]
        """
        return self._storage._read()[self._name]['rows']
