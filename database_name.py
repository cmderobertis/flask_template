# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database


class ClassName:

    def __init__(self, data):
        self.id = data['id']
        # Add the rest of the class attributes here...
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('database_name').query_db(query)
        # Create an empty list to append our instances of friends
        friends = []
        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append(cls(friend))
        return friends
