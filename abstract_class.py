from abc import abstractmethod
class TestBase:
    @abstractmethod
    def abstract_method1(self):
        raise Exception("Not implemented")
