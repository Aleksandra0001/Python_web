from abc import abstractmethod, ABC
from collections import UserDict


class SomeBook(ABC, UserDict):
    @abstractmethod
    def save_data_to_db(self):
        pass

    @abstractmethod
    def load_data_from_db(self):
        pass

    @abstractmethod
    def add_record(self, record):
        pass

    @abstractmethod
    def delete_record(self, name):
        pass

    @abstractmethod
    def update_record(self, name, value):
        pass

    @abstractmethod
    def find_record(self, name):
        pass


class SomeRecord(ABC):
    @abstractmethod
    def add_address(self):
        pass

    @abstractmethod
    def add_birthday(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class SomeNoteBookRecord(ABC):
    @abstractmethod
    def add_tag(self):
        pass

    @abstractmethod
    def del_tag(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class SomeField(ABC):
    @abstractmethod
    @property
    def value(self):
        pass

    @abstractmethod
    @value.setter
    def value(self, value):
        pass


if __name__ == "__main__":
    pass
