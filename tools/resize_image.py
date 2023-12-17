def resize_image( type_img, width = 450 ):
    """
    Re-dimensiona una imagen en un tamaño a igual proporción de lado y lado 
    10 x 15 = -2 =  8 x 13

    500 = 100%
    25 x 100 / 500
    2500 / 500
    25  = 5%

    5/100 = 0.05
    """
    #print( img_original.width )
    #print( img_original.height )

    min_height = type_img.height * (( (width * 100) / type_img.width) / 100)
    min_height = int(min_height)
    #equal dimension 
    img_copy = type_img.resize((width, min_height))
    return img_copy
