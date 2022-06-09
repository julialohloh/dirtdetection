from PIL import Image

def read_imagefile(file):
    """Takes in jpg and png file and Read it

    Parameters
    ----------

    file: Image file with extension jpg or png

    Returns
    -------

    array
        Image array data
    """
    image = Image.open(file)

    return image