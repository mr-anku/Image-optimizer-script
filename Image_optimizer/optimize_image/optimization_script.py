
import os
import urllib.request
from PIL import Image

from optimize_image.exceptions.format_error import FormatError


'''
This provides ('PNG', 'JPEG', 'GIF', 'WEBP') file format support, an efficient internal representation, and fairly powerful image processing capabilities.
You can get Optimized image in the same file format.
'''

class Optimization():
    
    '''
    optimize_image function takes three arguments 
    1. img_url : Url of the image you want to optimize
    2. img_quality : space covered by the image depends on this. less quality means less size of the image .
    3. filename : Name you want to give you optimized image without format
    '''

    def optimize_image(img_url, img_quality, filename):
        
        valid_formats =['PNG', 'JPEG', 'GIF', 'WEBP']

        try:
            
            urllib.request.urlretrieve(img_url, 'original')
            img  = Image.open("original")

            format = img.format

            if format not in valid_formats:
                msg = "###====>> File format ",format," not supported <<====###"
                os.remove('original')
                raise FormatError(501, msg)

            file_name = filename + "." + format

            optimized_image =img.save(file_name, optimize=True, quality = img_quality)
            os.remove('original')

            return optimized_image

        except Exception as e:
            print(e)
