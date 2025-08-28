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
4) Use

Ubuntu 22.04.5 LTS
1) Download+Unzip
2)

Other: afraid you will have to comile the project using the steps below, sorry.


If working on project then note the following:

To Do:
-Functionality
  - Need to be able to click on the plot to pick a point -- Dificult to actually implement
  - need t implemented so functions may be f(x,y,t) -- Not so Dificult to implement, but have not taken the time to do it
  - Make it so the blank graph is made after the program user first downloads the program, this will make the program downlaod take up less space. 

- Feature
  - should also save time based data as part of a numpy array so that  be nice you could also get different time based.
  - would be nice if the user could specify a specific h value and the amount of time they would like to simulate.
  - would be good to add Huen's method, but not required.
  - would be nice to add settings so plot does not reset, that way could plot using multiple different methods and have them all displayed at the same time. 

- Display
  - would be nice if the plot scaled as the plot was moved
  - should not have to replot everything if only a small thing is changed such as backwards time being added or title being changed

- Settings
  - should be more than 2 colors for plotted lines and there should be a setting for picking colors
  - Need to test all of the settings and things to make sure the program is working properly

- Warnings Update:
  - warnings should all appear in a single popup at the end of processing and should be listed off

- Possible Errors:
  - a while ago I had an issue where the arrows seemed to be scaled based on the xdensity and ydensity, but this no longer seems to be the case,
    either this was inadvertently fixed or is an uncommon error.
  - Would be good to check over variables section along with the sections responsible for producing the
    phase plots just to have checked them over. They seem to be working, but good to check.

- DimensionalA
  - for sure should be able to use 1D and get a nice plot

- DimensionalB
  - should also be able to use 3D, but the might be for later

Low Priority
- Would be good to generate a loading bar if plot it taking a while
- no saftey when loading a json file - program may crash if broken json loaded 
  (low priority since it requires that user went into json file and then modified it)

To work in vscode will need
git config --global user.email "samuelcstreet@gmail.com"
git config --global user.name "SamuelStreet"

1)
Windows:
Install python + pip
In command
"C:/Users/Samuel/Downloads/Programming related/Python/SPPP_TESTING_ENVIRONMENT"
"C:/Users/Samuel/Downloads/Programming related/Python/SPPP_ENVIRONMENT"
python -m venv SPPP_Environment/location/you/want/it
path\of\SPPP_Environment\Scripts\activate

DEBIAN/Ubuntu:
#python
(((
  For specific version of python
  sudo apt-get update
  sudo add-apt-repository ppa:deadsnakes/ppa
  sudo apt-get update
  sudo apt-get install python3.12 (will have to adjust other commands that use python3 to python3.12, also do not remove python initially installed on device as other people have said that is a bad idea on stack exchange)
)))
sudo apt-get install python3
sudo apt-get install python3-pip
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
Explination only for one line
                                                                                              #gtk 3
                                                                                              sudo apt-get install python3

                                                                                              sudo apt-get install libgtk-3-dev

                                                                                              #gstreamer and gstreamer-plugins-base
                                                                                              apt-get install libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio

                                                                                              #glut
                                                                                              sudo apt-get install freeglut3-dev

                                                                                              #libwebkit
                                                                                              sudo add-apt-repository "deb http://gb.archive.ubuntu.com/ubuntu jammy main"; sudo apt-get update; sudo apt-get install libwebkit2gtk-4.0-dev -y;

                                                                                              #libjpeg 
                                                                                              sudo apt-get install libjpeg-dev

                                                                                              #libpng
                                                                                              sudo apt-get install libpng-dev

                                                                                              #libtiff
                                                                                              Ubuntu 14.04-22.04
                                                                                              sudo apt install libtiff5
                                                                                              Ubuntu 23.04-24.10
                                                                                              sudo apt install libtiff6

                                                                                              #libsdl (from gemni instructions with some optional packages that might make things work better)
                                                                                              sudo apt install libsdl2-dev
                                                                                              sudo apt install libsdl2-image-dev
                                                                                              sudo apt install libsdl2-mixer-dev
                                                                                              sudo apt install libsdl2-ttf-dev

                                                                                              #libnotify
                                                                                              sudo apt-get install libnotify4

                                                                                              # libsm
                                                                                              sudo apt-get install libsm6:i386

#As One Command:
Ubuntu 22.04
sudo apt-get install update; sudo apt-get install libgtk-3-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio freeglut3-dev; sudo add-apt-repository "deb http://gb.archive.ubuntu.com/ubuntu jammy main"; sudo apt-get update; sudo apt-get install libwebkit2gtk-4.0-dev libjpeg-dev libpng-dev; sudo apt install libtiff5 libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev; sudo apt-get install libnotify4 libsm6:i386
Ubuntu 24.04
sudo apt-get install update; sudo apt-get install libgtk-3-dev libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev libgstreamer-plugins-bad1.0-dev gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav gstreamer1.0-tools gstreamer1.0-x gstreamer1.0-alsa gstreamer1.0-gl gstreamer1.0-gtk3 gstreamer1.0-qt5 gstreamer1.0-pulseaudio freeglut3-dev; sudo add-apt-repository "deb http://gb.archive.ubuntu.com/ubuntu jammy main"; sudo apt-get update; sudo apt-get install libwebkit2gtk-4.0-dev libjpeg-dev libpng-dev; sudo apt install libtiff6 libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev; sudo apt-get install libnotify4 libsm6:i386

Ubuntu 22.04
pip install -U     -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-22.04.5     wxPython
Ubunut 24.04
pip install -U     -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-24.04.2     wxPython
(to make it so popups will work, might only be required for some hardware)
sudo apt-get install libnvidia-egl-wayland1

pip install plotly pyinstaller

(possibly need sudo apt-get install libnvidia-egl-wayland1 then re-start, but I think it wont make a difference)

3)
If using Windows make sure vs code changes directory to venv directory


4) Compile Project:

(when using pyinstaller use -D to get a way faster program, slightly more work for user to accesss first time but loads way quicker)

Windows
pyinstaller -D --name "SPPP V0.2.4" --icon="C:/Users/Samuel/Downloads/Programming related/Python/PPP/Photos/PPP_Logo.ico" --noconsole --add-binary "c:\Users\Samuel\AppData\Local\Programs\Python\Python312\Lib\site-packages\wx\WebView2Loader.dll;.\wx" --add-data "C:/Users/Samuel/Downloads/Programming related/Python/PPP/Graphs;Graphs" --add-data "C:/Users/Samuel/Downloads/Programming related/Python/PPP/Photos;Photos" "C:/Users/Samuel/Downloads/Programming related/Python/PPP/Phase_Plot_App_Launcher.py"


FOR ALL LINUX -- Should find a way to add --strip to make files smaller
https://pyinstaller.org/en/stable/usage.html

LINUX Debian12
/home/samuelstreet/Downloads/PPP_python_environtment/bin/pyinstaller -D --icon="/home/samuelstreet/Downloads/PPP Github Space/PPP/Photos/PPP_Logo.ico" --noconsole --add-data "/home/samuelstreet/Downloads/PPP Github Space/PPP/Graphs:Graphs" --add-data "/home/samuelstreet/Downloads/PPP Github Space/PPP/Photos:Photos" "/home/samuelstreet/Downloads/PPP Github Space/PPP/Phase_Plot_App_Launcher.py"

LINUX Ubuntu 24.04.2 LTS
a) pyinstaller -D --icon="/home/Downloads/SPPP_code/PPP/Photos/PPP_Logo.ico" --noconsole --add-data "/home/samuelcstreet/Downloads/SPPP_code/PPP/Graphs:Graphs" --add-data "/home/samuelcstreet/Downloads/SPPP_code/PPP/Photos:Photos" "/home/samuelcstreet/Downloads/SPPP_code/PPP/Phase_Plot_App_Launcher.py"
Go into internals once compiled grab Graphs and Photos then place them in parent directory

b) after application is made with pyinstaller copy and past the file using:
cp --dereference -r old/file/path new/file/path
to get source of all symbolic links

5) In the Dist\internals folder cut the Graphs and Photos 

LINUX Ubuntu 22.04.5 LTS
a) pyinstaller -D --clean --strip --name "SPPP v0.2.4" --noconsole --add-data "/home/samuelstreet/Downloads/sppp_github_code/PPP/Graphs:Graphs" --add-data "/home/samuelstreet/Downloads/sppp_github_code/PPP/Photos:Photos" "/home/samuelstreet/Downloads/sppp_github_code/PPP/Phase_Plot_App_Launcher.py"

b) 