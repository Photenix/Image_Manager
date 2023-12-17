import unittest

deleteList = [ 0,  2]

def getNext ( number, add ):
    #get index if not in list delete
    x = lambda num : num in deleteList
    y = x(number + add)
    return number + add if y == False else getNext( number + add,  add)


class TestStringMethods(unittest.TestCase):

    def test_isNext_1(self):
        self.assertEqual( getNext(0,1), 1 )

    def test_isNext_2( self ):
        self.assertEqual( getNext(2,1), 3 )

    def test_isNextNegative_1( self ):
        self.assertEqual( getNext(2,-1), 1 )


if __name__ == '__main__':
    unittest.main()
