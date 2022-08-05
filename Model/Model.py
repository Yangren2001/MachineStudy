#encoding = utf-8

"""
     @describe: Model Class
"""

class Model:

    def __new__(cls, *args, **kwargs):

        return super(Model, cls).__new__(*args, **kwargs)

    def __init__(self, *args, **kwargs):
        pass

    def build(self):
        pass

    def model(self):
        pass

    def fit(self,x ,y):
        pass

    def predict(self, x):
        pass

    def loss(self):
        pass

    def test(self):
        pass