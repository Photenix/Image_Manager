import customtkinter as ctk
from PIL import Image
from CTkListbox import *
from shutil import move

from tools import FilterInformation, resize_image, resize_one_element

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

#----------------------- VARIABLES -----------------------#

dirname = "E:/Descargas/Memes/"

size_main_image = lambda img : ( img.width, img.height )

lbl_list = [] #group labels

isOpen = False

information = None

deleteList = []

width = 1000
height = 700

config_space = {}
mod_elements = []

#----------------------- !VARIABLES -----------------------#

app = ctk.CTk()  # create CTk window like you do with the Tk window
app.geometry(f"{width}x{height}")
app.minsize( 500, 500)
app.grid()

#----------------------- FRAMES -----------------------#

tools_frame = ctk.CTkScrollableFrame(app,
	orientation="vertical",
	width=300,
	height= height - 50,
	label_anchor = "center", # "w",  # n, ne, e, se, s, sw, w, nw, center
	corner_radius = 20,
)
tools_frame.grid( row = 0, column = 1, padx = 10 )

image_frame = ctk.CTkScrollableFrame(app,
	orientation="vertical",
	width=500,
	height= height - 50,
	label_anchor = "center", # "w",  # n, ne, e, se, s, sw, w, nw, center
	corner_radius = 20,
)
image_frame.grid(row=0, column=2, sticky='ns')

#----------------------- !FRAMES -----------------------#


#----------------------- FUNCTIONS -----------------------#
def browseFiles():
    #puedo abrir un directorio
    global dirname, lbl_list, isOpen, information
    dirname = ctk.filedialog.askdirectory()

    if dirname == '':
        return None

    information = FilterInformation(dirname)

    insert_list( listbox, information.get_list_files() )
    arr_dir = information.get_list_dir()

    if len(lbl_list) != 0:
        for i in lbl_list:
            i.destroy()
    
    lbl_list = []
    for i in range(9):
        lbl_list.append( ctk.CTkLabel( tools_frame, text= f"Numero {i}: {arr_dir[i]}" ) )
        lbl_list[i].pack( pady= 5 )
    
    isOpen = True

    #print(x.get_list_files())
    """
    InfoWindow( dirname, handle_image )
    # Change label contents
    label_name_file.configure(text="Directory Opened: " + dirname)
    """

def insert_list( list, arr ):
    for n, i in enumerate(arr):
        list.insert( n, i )

def handle_select( event ):
    global dirname, main_image, image_label
    link = f"{dirname}/{event}"

    #! corregir 
    windows = image_label.master.cget("width")

    main_image = resize_image( Image.open(link), windows - 25 )
    image_label.configure( image=pre_img(main_image) )

def pre_img ( img ):
    return ctk.CTkImage(light_image= img, dark_image= img, size= size_main_image(img))

def getNext ( number, add ):
    #get index if not in listDelete 
    global deleteList
    x = lambda num : num in deleteList
    y = x(number + add)
    return number + add if y == False else getNext( number + add,  add)

def command_keys (event):
    global deleteList
    if not isOpen : return None
    #* get index
    index = listbox.curselection()
    index = index if index != None else 0

    if event.keysym == 'Up':
        listbox.select( getNext(index, -1) if index > 0 else 0 )

    elif event.keysym == 'Down':
        listbox.select( getNext(index, 1) if index < listbox.size() - 1 else listbox.size() - 1)
    
    elif (event.keycode >= 48 and event.keycode <= 57) or (event.keycode >= 96 and event.keycode <= 105):
        global dirname

        dir_list = information.get_list_dir()
        index_dir = event.keycode % 48 if event.keycode >= 48 and event.keycode <= 57 else event.keycode % 96
        if dir_list[index_dir] != None:
            oldDirection = f"{dirname}/{listbox.get()}"
            newDirection = f"{dirname}/{dir_list[index_dir]}"
            move(oldDirection, newDirection)
            deleteList.append( index )
            listbox.delete( index )
            listbox.select(index - 1 if index > 0 else 0)
    
    #print( deleteList )
"""
def re_size (event, element_list, max_space = {}):
    #max_space = values(int) : 0.0 to 1.0
    div = len( element_list )
    div = 2
    a_width, a_height = app.winfo_width(), app.winfo_height()
    #element height and width values
    e_h, e_w = int( a_height / div ), int( a_width / div )

    for i, value in enumerate( element_list ):
        #print( value.cget("width") )
        if i in max_space.keys():
            pass
        value.configure( width = e_w )
        pass
"""

#----------------------- !FUNCTIONS -----------------------#


# Use CTkButton instead of tkinter Button
btn_file = ctk.CTkButton(tools_frame, text="Buscar Carpeta", command= browseFiles )
btn_file.pack( side = "top" )


listbox = CTkListbox(app, command= lambda event : handle_select(event), height= app.winfo_reqheight(), width= 300)
#listbox.grid(row=0, column=0, sticky='ns')
listbox.grid(row=0, column=0, sticky='nsew')


#? Creation de imagenes
STR_IMG = "E:/Descargas/Memes/07319bb167b4c38afbf5600551d3e09de3875f2435cd7f8197e7fb2d74f8850b.jpg"
main_image = resize_image(Image.open(STR_IMG))
image_label = ctk.CTkLabel( image_frame, image=pre_img(main_image), text="")
image_label.pack( side = "top" )

mod_elements.append( listbox )
mod_elements.append( tools_frame )
mod_elements.append( image_frame )

app.bind('<KeyRelease>', lambda event : command_keys(event) )

app.bind( '<Configure>', lambda event : resize_one_element(event, app, mod_elements, image_frame) )




app.mainloop()