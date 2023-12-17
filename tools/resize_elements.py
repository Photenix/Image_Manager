from  customtkinter import CTkScrollableFrame

def resize_elements (event, app, element_list, max_space = {}):
    """
    max_space = values(int) : 0.0 to 1.0


    problema:
    tenemos tres elementos en pantalla con iguales cantidades de espacio ocupado
    - objetivo es que cogiendo solamente un elemento  ordenarlo con el espacio sobrante dado por el espacio de la ventana

    - secundario organizarlos tres elementos con la misma dispocision de elementos

    - terciario organizar objetos selecionados sin mover el resto

    """
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

def resize_one_element ( event, app, elements, mod_element ):
    "resize in X eje one element"

    a_width = app.winfo_width()

    #space in use
    siu = 0

    for i in elements:
        if i == mod_element: continue
        siu += i.cget("width")
    
    mod_element.configure( width = a_width - siu - 125 )