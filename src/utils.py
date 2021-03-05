import os
import pygame

def _sizemap(imgsize, base_image):
    # Esta funcion cambia el tamaño de la imagen
    return pygame.transform.scale(base_image, (imgsize, imgsize))

def charge_images(path, zoom_list, start="images/lowRes"):
    # Esta funcion precarga las imagenes de images (strings) usando los zooms de zoom_list
    images = {}
    imagesStrings = {}
    lista = os.listdir (start)

    for subd in lista:
        lista2 = os.listdir(os.path.join(start, subd))
        images[subd] = {}
        imagesStrings[subd] = {}
        
        for subd2 in lista2:
            lista3 = os.listdir(os.path.join(start, subd, subd2))
            images[subd][subd2] = []
            imagesStrings[subd][subd2] = []

            for imgfile in lista3:    
                idic = {}
                idicS = {}
                base_image = pygame.image.load(os.path.join(start, subd, subd2, imgfile))
                
                for size in zoom_list:
                    idic[size] = _sizemap(size, base_image)
                    idicS[size] = pygame.image.tostring(idic[size], 'RGB')
                images[subd][subd2].append(idic)
                imagesStrings[subd][subd2].append(idicS)

    print(images)
    return images, imagesStrings