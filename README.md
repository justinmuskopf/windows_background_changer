# Windows Background Changer
A simple python module that changes the current desktop background on Windows to a provided image.

## Requirements
* Python (2.7 or 3.x)

## Usage
Running the script independently requires that you provide the image's path to the script via a commandline argument as so:
  `python windows_background_changer /my/path/to/image`
    
Using the class within code is even more simple. 
A basic usage might look like this:

```py
from windows_background_changer import WindowsBackgroundChanger
 
WindowsBackgroundChanger.change_background('/my/path/to/image')
```

## Example
My personal usage of this script is included in the [example](/example) directory.
It accepts an API key to the NASA Astronomy Picture of the Day (APOD) API and sets your Windows background to today's picture.


And that's all!
