import ctypes
import sys
from os.path import isfile

class WindowsBackgroundChanger:
    @staticmethod
    def change_background(path_to_image):
        SPI_SETDESKWALLPAPER = 20
        
        if not isfile(path_to_image):
            raise FileNotFoundError(path_to_image)
 
        if sys.version_info[0] < 3:
            bg_change_function = ctypes.windll.user32.SystemParametersInfoA
        else:
            bg_change_function = ctypes.windll.user32.SystemParametersInfoW

        bg_change_function(SPI_SETDESKWALLPAPER, 0, path_to_image, 0)



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("USAGE: {} PATH_TO_IMAGE".format(sys.argv[0]))
        exit(1)

    WindowsBackgroundChanger.change_background(sys.argv[1])
