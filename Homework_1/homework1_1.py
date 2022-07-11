from abc import abstractmethod, ABC
import pickle
import json

FILE_NAME = "data"


class SerializationInterface(ABC):
    @abstractmethod
    def serialize(self, data):
        pass

    @abstractmethod
    def deserialize(self, data):
        pass


class Bin_serialization(SerializationInterface):
    def serialize(self, data):
        with open(FILE_NAME + ".bin", 'wb') as f:
            pickle.dump(data, f)

    def deserialize(self, data):
        with open(FILE_NAME + ".bin", 'rb') as f:
            return pickle.load(f)


class Json_serialization(SerializationInterface):
    def serialize(self, data):
        with open(FILE_NAME + ".json", 'w') as f:
            json.dump(data, f)

    def deserialize(self, data):
        with open(FILE_NAME + ".json", 'r') as f:
            return json.load(f)


if __name__ == "__main__":
    profile = {"name": "Sasha", "city": "Odessa", "age": 22}
    bin_file = Bin_serialization()
    bin_file.serialize(profile)
    bin_file.deserialize(profile)

    json_file = Json_serialization()
    json_file.serialize(profile)
    json_file.deserialize(profile)
