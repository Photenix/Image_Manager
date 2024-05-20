import unittest

from tools import FilterInformation

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

    def test_get_list_dir_meme( self ):
        info = FilterInformation( "E:/Descargas/Memes/" )
        self.assertEqual( info.get_list_dir() , ['gif', 'h', None, None, None, None, None, None, None, None])
    
    def test_get_list_dir_hen( self ):
        info = FilterInformation( "E:/Descargas/Ricura/" )
        self.assertEqual( info.get_list_dir() , ['furry', 'loli', None, None, None, None, None, None, None, None])

    def test_is_not_dir( self ):
        info = FilterInformation( "E:/Descargas/Ricura/" )
        self.assertEqual( info.is_dir("juan.jpg") , False )
    
    def test_is_dir( self ):
        info = FilterInformation( "E:/Descargas/Ricura/" )
        self.assertEqual( info.is_dir("juan") , True )


if __name__ == '__main__':
    unittest.main()
