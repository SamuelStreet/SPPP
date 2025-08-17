Installation instructions:
Windows:
1) Download+Unzip
2) Use

Debian12:
1) Download+Unzip
2) Use

Ubuntu24.04.2
1) Download+Unzip
2) sudo add-apt-repository "deb http://gb.archive.ubuntu.com/ubuntu jammy main"; sudo apt-get update; sudo apt-get install libwebkit2gtk-4.0-dev -y;
3) Expand Window a little
4) Use application

Other: afraid you will have to comile the project using the steps below, sorry.


If working on project then note the following:

To Do:
-Functionality
  - Would be good to check over variables section, should be able to use any variable that is not a
    python reserved <= 10 characters, but had to modify variable names so would be good to check (Euler)
  - Rung Kutta Needs added
  - Need to be able to click on the plot to pick a point
  - Need to make it so graphs and photos do not need to be moved to the same folder as the exe, makes it so links do not work as well

- Feature
  - should also save time based data as part of a nump array so that  be nice you could also get different time based.
  - would be nice if the user could specify a specific h value and the amount of time they would like to simulate.
  - would be good to add Huen's method, but not required.

- Display
  - would be nice if the plot scaled as the plot was moved
  - should not have to replot everything if only a small thing is changed such as backwards time being added or title being changed

- Settings
  - would be nice if the legend could be turned on or off
  - should be more than 2 colors for plotted lines and there should be a setting for picking colors
  - Need to test all of the settings and things to make sure the program is working properly

- Warnings Update:
  - warnings should all appear in a single popup at the end of processing and should be listed off

Low Priority
- Would be good to generate a loading bar if plot it taking a while
- no saftey when loading a json file - program may crash if broken json loaded 
  (low priority since it requires that user went into json file and then modified it)

To work in vscode will need
1)
Windows:
Install python + pip
In command
python -m venv SPPP_Environment/location/you/want/it
path\of\SPPP_Environment\Scripts\activate

DEBIAN/Ubuntu:
Install python + pip
sudo apt install python3-venv
python3 -m venv SPPP_Environment (makes a virtual environment for storing python packages this is used to store python packages)
source directory/of/SPPP_Environment/bin/activate (will make it so that, when compiling SPPP, only packages loaded in SPPP_Environment will be used so less space is taken up)

2)
Windows:
pip install wxpython numpy plotly pyinstaller

Debian:
pip install numpy plotly pyinstaller
sudo apt-get update;
sudo apt-get install python-dev-is-python3 libgtk-3-dev snapd  libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio freeglut3-dev libwebkit2gtk-4.0-dev libjpeg62 libpng-dev libtiff-dev libsdl2-2.0-0 libnotify-bin libsm6 -y
sudo snap install snapd -y;
sudo snap install gstreamer --edge;
sudo ldconfig;
(was told in instructions to get same version as gtk, this is not the same version, but it could be downloaded)
Then follow https://wxpython.org/blog/2017-08-17-builds-for-linux-with-pip/index.html
and it will work (saved wheel file so it will work from the .whl file to make things easier)


Ubuntu:
pip install numpy plotly pyinstaller
pip install -U     -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-24.04.2     wxPython

3)
If using Windows make sure vs code changes directory to venv directory


4) Compile Project:

(when using pyinstaller use -D to get a way faster program, slightly more work for user to accesss first time but loads way quicker)

Windows
pyinstaller -D --icon="C:/Users/Samuel/Downloads/Programming related/Python/PPP/Photos/PPP Logo.png" --noconsole --add-binary "c:\Users\Samuel\AppData\Local\Programs\Python\Python312\Lib\site-packages\wx\WebView2Loader.dll;.\wx" --add-data "C:/Users/Samuel/Downloads/Programming related/Python/PPP/Graphs;Graphs" --add-data "C:/Users/Samuel/Downloads/Programming related/Python/PPP/Photos;Photos" "C:/Users/Samuel/Downloads/Programming related/Python/PPP/Phase_Plot_App_Launcher.py"

LINUX Debian12
/home/samuelstreet/Downloads/PPP_python_environtment/bin/pyinstaller -D --icon="/home/samuelstreet/Downloads/PPP Github Space/PPP/Photos/PPP Logo.png" --noconsole --add-data "/home/samuelstreet/Downloads/PPP Github Space/PPP/Graphs:Graphs" --add-data "/home/samuelstreet/Downloads/PPP Github Space/PPP/Photos:Photos" "/home/samuelstreet/Downloads/PPP Github Space/PPP/Phase_Plot_App_Launcher.py"

LINUX Ubuntu 24.04.2 LTS
a) pyinstaller -D --icon="/home/Downloads/SPPP_code/PPP/Photos/PPP Logo.png" --noconsole --add-data "/home/samuelcstreet/Downloads/SPPP_code/PPP/Graphs:Graphs" --add-data "/home/samuelcstreet/Downloads/SPPP_code/PPP/Photos:Photos" "/home/samuelcstreet/Downloads/SPPP_code/PPP/Phase_Plot_App_Launcher.py"
Go into internals once compiled grab Graphs and Photos then place them in parent directory

b) after application is made with pyinstaller copy and past the file using:
cp --dereference -r old/file/path new/file/path
to get source of all symbolic links

5) In the Dist\internals folder cut the Graphs and Photos 
