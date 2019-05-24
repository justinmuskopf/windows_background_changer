import ctypes
from sys import argv
from os.path import isfile

class WindowsBackgroundChanger:
    @staticmethod
    def change_background(path_to_image):
        SPI_SETDESKWALLPAPER = 20
        
        if not isfile(path_to_image):
            raise FileNotFoundError(path_to_image)
        
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER,
                                                   0,
                                                   path_to_image,
                                                   0)

if __name__ == "__main__":
    if len(argv) != 2:
        print("USAGE: {} PATH_TO_IMAGE".format(argv[0]))
        exit(1)

    WindowsBackgroundChanger.change_background(argv[1])
