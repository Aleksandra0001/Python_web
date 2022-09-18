from view import main
from mongo_client import mongo_client

if __name__ == '__main__':
    if mongo_client:
        try:
            main()
        except Exception as e:
            print('Error: ', e)
    else:
        print('Error: mongo_client is None')