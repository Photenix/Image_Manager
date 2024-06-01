#external code import
import customtkinter as ctk
from PIL import Image
from CTkListbox import *
from shutil import move

#my code import
from tools import FilterInformation, resize_image, resize_one_element

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

#----------------------- VARIABLES -----------------------#

#? Images creation test
STR_IMG = "E:/Descargas/Memes/07319bb167b4c38afbf5600551d3e09de3875f2435cd7f8197e7fb2d74f8850b.jpg"

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
	height= height - 100,
	label_anchor = "center", # "w",  # n, ne, e, se, s, sw, w, nw, center
	corner_radius = 20,
)
tools_frame.grid( row = 0, column = 1, sticky='ns')

image_frame = ctk.CTkScrollableFrame(app,
	orientation="vertical",
	width=500,
	height= height - 100,
	label_anchor = "center", # "w",  # n, ne, e, se, s, sw, w, nw, center
	corner_radius = 20,
)
image_frame.grid(row=0, column=3, sticky='ns')

#----------------------- !FRAMES -----------------------#


#----------------------- FUNCTIONS -----------------------#
def browseFiles():
    #puedo abrir un directorio
    global dirname, lbl_list, isOpen, information

    dirname = ctk.filedialog.askdirectory()

    if dirname == '':
        return None

    information = FilterInformation(dirname)

    arr_dir = information.get_list_dir()

    #show directory
    if len(lbl_list) != 0:
        for i in lbl_list:
            i.destroy()
    
    lbl_list = []
    for i in range(9):
        lbl_list.append( ctk.CTkLabel( tools_frame, text= f"Numero {i}: {arr_dir[i]}", anchor='w' ) )
        lbl_list[i].pack( pady= 5 )

    list_box.delete("all")

    #show images file
    insert_list( list_box, information.get_list_files() )

    # print( listbox.buttons )
    
    isOpen = True

    #print(x.get_list_files())
    """
    InfoWindow( dirname, handle_image )
    # Change label contents
    label_name_file.configure(text="Directory Opened: " + dirname)
    """

def insert_list( list:CTkListbox, arr ):
    #Init change of color
    progressbar_files._progress_color = ['#3B8ED0', '#123f63']
    progressbar_files._draw()
    num_arr = len(arr)
    for n, i in enumerate(arr):
        # list.insert( "end", i, update=False )
        list.insert( index=n, option=i, update=False )
        if n % 100 == 0 :
            progressbar_files.set(n/num_arr)
            list.update()
        if n > 1100: break
    #end return the original color
    progressbar_files._progress_color = ['#3B8ED0', '#1F6AA5']
    progressbar_files._draw()
    progressbar_files.set(1)
    list.update()

def handle_select( event ):
    global dirname, main_image, image_label, image_frame
    link = f"{dirname}/{event}"

    #! corregir 
    __windows = image_label.master.cget("width")
    __height = image_label.master.cget("height")

    main_image = resize_image( Image.open(link), __height, __windows - 25 )
    # image_frame._parent_canvas.yview("scroll", 0, "units") ver como funciona
    image_label.configure( image=pre_img(main_image) )

def pre_img ( img: ctk.CTkImage ):
    return ctk.CTkImage(light_image= img, dark_image= img, size= size_main_image(img))

def getNext ( number, add ):
    #get index if not in listDelete 
    global deleteList
    x = lambda num : num in deleteList
    y = x(number + add)
    # print(f"---resultado lamda getNext: {y}")
    # print(f"---numero dado getNext: {number + add}")
    return number + add if y == False else getNext( number + add,  add)

def command_keys (event):
    global deleteList
    if not isOpen : return None
    #* get index
    index = list_box.curselection()
    index = index if index != None else 0

    if event.keysym == 'Up':
        value = getNext(index, -1) if index > 0 else 0
        list_box.select( value )
        # print( value )

    elif event.keysym == 'Down':
        # print( f"---test index: {index}" )
        # print( f"---test deleteList: {deleteList}" )
        # print( f"---test getNext: {getNext(index, 1)}" )
        # print( f"---test list size: {list_box.size()}" )
        # print( f"---test else list_box.size(): {list_box.size() - 1}" )
        # print( "\n\n" )
        value = getNext(index, 1) if index < list_box.size() - 1 else list_box.size() - 1
        list_box.select( value )
    
    elif (event.keycode >= 48 and event.keycode <= 57) or (event.keycode >= 96 and event.keycode <= 105):
        global dirname

        dir_list = information.get_list_dir()
        index_dir = event.keycode % 48 if event.keycode >= 48 and event.keycode <= 57 else event.keycode % 96
        if dir_list[index_dir] != None:
            oldDirection = f"{dirname}/{list_box.get()}"
            newDirection = f"{dirname}/{dir_list[index_dir]}"
            move(oldDirection, newDirection)
            deleteList.append( index )
            list_box.delete( index )
            list_box.select(index - 1 if index > 0 else 0)
    
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
btn_file.pack( side = ctk.BOTTOM, fill= None, expand=False )

progressbar_files = ctk.CTkProgressBar(app, orientation="vertical", progress_color=['#3B8ED0', '#1F6AA5'])
progressbar_files.grid( row=0, column=2, sticky='nsew', pady=4 )
progressbar_files.set(1)

list_box = CTkListbox(app, command= lambda event : handle_select(event), height= app.winfo_reqheight(), width= 300)
#listbox.grid(row=0, column=0, sticky='ns')
list_box.grid(row=0, column=0, sticky='nsew')

main_image = resize_image(Image.open(STR_IMG))
image_label = ctk.CTkLabel( image_frame, image=pre_img(main_image), text="")
image_label.pack( side = "top" )

mod_elements.append( list_box )
mod_elements.append( tools_frame )
mod_elements.append( image_frame )

app.bind('<KeyRelease>', lambda event : command_keys(event) )

app.bind( '<Configure>', lambda event : resize_one_element(event, app, mod_elements, image_frame) )


if "__main__" == __name__:
    app.mainloop()