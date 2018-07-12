import unittest
from helloSuggestions import serializationHelper

class Test_serializationHelper(unittest.TestCase):
    
    def test_toJson_complexOjbect_dictionary(self):

        #arrange
        xVal = 'X'
        zxVal = "ZX"

        obj = B()
        obj.x = xVal
        obj.z = A()
        obj.z.x = zxVal

        #act
        objDic = serializationHelper.toJson(obj)

        #assert
        self.assertDictEqual(objDic, { 'x': xVal, 'z': { 'x': zxVal, 'y': None }})

    #No support to cyclic references
    def test_toJson_cyclicReferences_error(self):

        #arrange
        xVal = 'X'
        zyVal = "ZY"

        obj = B()
        obj.x = xVal
        obj.z = obj
        obj.z.y = zyVal

        #act / assert
        self.assertRaises(ValueError, serializationHelper.toJson, obj)

class A(object):
    
    def __init__(self):
        self.x : str = None
        self.y : int = None

class B(A):
    
    def __init__(self):
        self.z : A = None
