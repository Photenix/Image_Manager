def resize_image( type_img, height:int=700, width:int = 450 ):
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

    compareWidth = type_img.width - width
    compareHeight = type_img.height - height

    newH = height
    newW = width

    percentX = (type_img.height/type_img.width) * 100 
    percentY = (type_img.width/type_img.height) * 100

    print( percentX, percentY, percentX > percentY )

    if( compareWidth > compareHeight or percentX > percentY ):
        newH = type_img.height * (( (width * 100) / type_img.width) / 100)
        newH = int(newH)
    else:
        newW = type_img.width * (( (height * 100) / type_img.height) / 100)
        newW = int(newW)
    #equal dimension 
    img_copy = type_img.resize((newW, newH))
    return img_copy
