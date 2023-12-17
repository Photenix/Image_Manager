from os import listdir
import re

class FilterInformation:
    # te alista los archivos tipo .png y .jpg para su revision

    address = ""
    n_files = 0
    list_files = []

    def __init__( self, address ) -> None:
        self.address = address
        self.list_files = [i for i in listdir(address) if self.is_image_type(i)]
        self.list_dir = [i for i in listdir(address) if self.is_dir(i)]
        for i in range(10 - len(self.list_dir)):
            self.list_dir.append(None)
        self.n_files = len(self.list_files)

    def get_list_files(self):
        return self.list_files
    
    def get_list_dir(self):
        return self.list_dir
    
    def get_number_files(self):
        return self.n_files
    
    def is_image_type( self, name ):
        x = re.search(".jpg$", name)
        if x != None:
            return True
        else:
            x = re.search(".png$", name)
            return x != None
        
    def is_dir( self, name ):
        x = re.search( "\\.[a-z]*$", name )
        return x == None