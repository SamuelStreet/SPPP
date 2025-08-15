Notes:
- when using pyinstaller use -D to get a way faster program, slightly more work for user to accesss first time but loads way quicker

To Do:
- Settings
  - currently the same number of steps are used for forwards and backwards time should be custome
  - should not need to do forward and backward time at the same time
  - Too many warnings setting to shut all warnings off needed
  - Need to make it so settings can be scrolled through so they are not quite so overwhelming (may need settings tabs or at least sections)

-Functionality
  - Would be good to check over variables section, should be able to use any variable that is not a
    python reserved <= 10 characters, but had to modify variable names so would be good to check (Euler)
  - Rung Kutta Needs added
  - Need to be able to click on the plot to pick a point
  - Need to make it so graphs and photos do not need to be moved to the same folder as the exe, makes it so links do not work as well

- Feature
  - should also save time based data as part of a nump array so that  be nice you could also get different time based 


Low Priority
- Would be good to generate a loading bar if plot it taking a while
- no saftey when loading a json file - program may crash if broken json loaded 
  (low priority since it requires that user went into json file and then modified it)

- Display
  - would be nice if the plot scaled as the plot was moved

- Settings
  - would be nice if the legend could be turned on or off


To work in vscode will need
- pip install wx 
- pip install wx.html2 (For linux the above to are done together using a slightly more complex method described below)
- pip install numpy
- pip install plotly

(Should be in python to start)
- shutil
- json 
- os

Need to make a virtual environment when done otherwise pyinstaller includes 
every library installed system python environment which can be quite a few and end file will be bigger


To compile porject can use:

Windows
pyinstaller -D --icon="C:/Users/Samuel/Downloads/Programming related/Python/PPP/Photos/PPP Logo.png" --noconsole --add-binary "c:\Users\Samuel\AppData\Local\Programs\Python\Python312\Lib\site-packages\wx\WebView2Loader.dll;.\wx" --add-data "C:/Users/Samuel/Downloads/Programming related/Python/PPP/Graphs;Graphs" --add-data "C:/Users/Samuel/Downloads/Programming related/Python/PPP/Photos;Photos" "C:/Users/Samuel/Downloads/Programming related/Python/PPP/Phase_Plot_App_Launcher.py"

LINUX Debian12
/home/samuelstreet/Downloads/PPP_python_environtment/bin/pyinstaller -D --icon="/home/samuelstreet/Downloads/PPP Github Space/PPP/Photos/PPP Logo.png" --noconsole --add-data "/home/samuelstreet/Downloads/PPP Github Space/PPP/Graphs:Graphs" --add-data "/home/samuelstreet/Downloads/PPP Github Space/PPP/Photos:Photos" "/home/samuelstreet/Downloads/PPP Github Space/PPP/Phase_Plot_App_Launcher.py"

LINUX Ubuntu 24.04.2 LTS
pyinstaller -D --icon="/home/Downloads/SPPP_code/PPP/Photos/PPP Logo.png" --noconsole --add-data "/home/samuelcstreet/Downloads/SPPP_code/PPP/Graphs:Graphs" --add-data "/home/samuelcstreet/Downloads/SPPP_code/PPP/Photos:Photos" "/home/samuelcstreet/Downloads/SPPP_code/PPP/Phase_Plot_App_Launcher.py"
Go into internals once compiled grab Graphs and Photos then place them in parent directory












To install wxPython in Linux (Debian specific, but same instuctions for other distros, packages might just have different names)
(It will be just as agognizingly painful as it looks \)

Building wxPython on Debian12

sudo apt update

sudo apt install python-dev-is-python3

sudo apt install libgtk-3-dev

sudo apt install snapd -y
sudo snap install snapd
sudo snap install gstreamer --edge

apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio -y

sudo apt-get install freeglut3-dev

sudo apt install libwebkit2gtk-4.0-dev   (was told in instructions to get same version as gtk, this is not the same version, but it could be downloaded)

apt-get install libjpeg62

sudo apt-get install libpng-dev

sudo apt-get install libtiff-dev

sudo apt-get install libsdl2-2.0-0

sudo apt install libnotify-bin

sudo apt-get install libsm6
sudo ldconfig

Then follow https://wxpython.org/blog/2017-08-17-builds-for-linux-with-pip/index.html

and it will work (saved wheel file so it will work from the .whl file to make things easier)



LINUX Ubuntu 24.04.2 (should work for other  ubuntu distrobutions)
run:
pip install -U     -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-24.04.2     wxPython