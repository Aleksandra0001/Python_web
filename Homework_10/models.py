from mongoengine import *
# import configparser
# import pymongo
#
# config = configparser.ConfigParser()
# config.read('config.ini')
#
#
# mongo_user = config.get('DB', 'user')
# mongodb_pass = config.get('DB', 'pass')
# mongo_cluster = config.get('DB', 'cluster_address')
#
# client = pymongo.MongoClient(f'mongodb+srv://{mongo_user}:{mongodb_pass}@{mongo_cluster}/personal-assistant?retryWrites=true&w'
#                     f'=majority')
#
# client.test()
# URL = f"mongodb+srv://{mongo_user}:{mongodb_pass}@{mongo_cluster}/personal-assistant?retryWrites=true&w=majority"

# connect(host="mongodb+srv://goitlearn:goit@cluster0.qh8el1i.mongodb.net/personal-assistant?retryWrites=true&w=majority")


class Contact(Document):
    first_name = StringField(required=True, max_length=50)
    last_name = StringField(required=True, max_length=50)
    email = EmailField(required=True, unique=True)
    phone = ListField(StringField(max_length=13))

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


