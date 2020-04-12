from abstract_class import TestBase

class ImplClass(TestBase):

    def abstract_method2(self):
        print("Hello")


if __name__ == "__main__":
    c = ImplClass()
    c.abstract_method2()
