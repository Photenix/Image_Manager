from os import listdir
import re
class FilterInformation:
    # te alista los archivos tipo .png y .jpg para su revision

    address = ""
    n_files = 0
    n_dirs = 0
    list_files: list = []

    def __init__( self, address:str ) -> None:
        
        self.address = address
        self.list_files = [i for i in listdir(address) if self.is_image_type(i)]
        self.list_dir = [i for i in listdir(address) if self.is_dir(i)]
        
        for i in range(10 - len(self.list_dir)):
            self.list_dir.append(None)
        self.n_files = len(self.list_files)
        self.n_dirs = len(self.list_dir)

    def get_list_files(self):
        return self.list_files
    
    def get_list_dir(self):
        return self.list_dir
    
    def get_number_dir(self):
        return self.n_dirs

    def get_number_files(self):
        return self.n_files
    
    def is_image_type( self, name ):
        x = re.search("\\.(jpg|png|jpeg)$", name)
        return x != None
        
    def is_dir( self, name ):
        x = re.match( "^\\w+$", name )
        return x != None