import wx
import wx.html2
import shutil # for copying files
import numpy as np
from plot_maker_2D import make_figure
#from Settings_File import Settings
from Default_Settings import Default
import popup_windows
import json
import os

global filepath 
filepath = ''
class Display_Window(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self,parent=parent,id=-1)
        self.display=wx.html2.WebView.New(self, backend=wx.html2.WebViewBackendDefault)
        global filepath
        self.display.LoadURL(filepath)

#This is the main class for the application, settings stored here when running
class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title = "S Phase Plane Plotter -- V0.1.5")
        
        self.cwd = os.getcwd()
        
        if os.path.exists(self.cwd+"/Photos/PPP_Logo.png"):
            icon = wx.Icon(self.cwd+"/Photos/PPP_Logo.png")
        else:
            icon = wx.Icon(self.cwd+"/_internal/Photos/PPP_Logo.png")
        self.SetIcon(icon)
        self.SetBackgroundColour("#282a30") # dark blue grey for the time being
        self.SetMinSize((600,400))
        self.SetSize((700, 535))
        font = wx.Font(10, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        #(pixelSize, family, style(italic type), weight(boldness), underline)
        # more info at https://docs.wxpython.org/4.0.7/wx.Font.html
        self.SetFont(font)

        self.panel = wx.Panel(self) # for holding things (things should not be held just by the window)
        self.panel.SetFont(font)

        # Sets up the settings allow allowing for multiple files. 
        if not os.path.exists(self.cwd+'/settings.json'):
            default_class_instance = Default()
            self.settings = default_class_instance.settings
            with open(self.cwd+'/settings.json', "w") as f:
                f.write(json.dumps(default_class_instance.settings))
        else:
            with open(self.cwd+'/settings.json', "r") as json_file:
                self.settings = json.load(json_file)
            if not os.path.exists(self.cwd+self.settings["settings_file"]):
                variable_override_warning = popup_windows.popup_window(self)
                variable_override_warning.Error("ERROR: settings file specified "+ self.settings["settings_file"][1:] + " is missing so I have reverted to default settings", cwd=self.settings["cwd"])
                variable_override_warning.Show()
                default_class_instance = Default()
                self.settings = default_class_instance.settings
            else:
                with open(self.cwd+self.settings["settings_file"], "r") as json_file:
                    self.settings = json.load(json_file)
            
            ##NOTE: HERE NEEDS TO BE SOMETHING THAT AUTOMATICALLY UPDATES OLD
            # SETTINGS FILES TO INCLUDE NEW SETTINGS
            
            if(self.settings["stop_all_warnings"]==True):
                #This and similar if statements are placed in other spots to avoid some possible inconsistencies.
                self.stop_variable_override_warning_setting_box.SetValue("True")
                self.stop_termination_warning_setting_box.SetValue("True")
                self.stop_numerical_termination_warning_setting_box.SetValue("True")
                self.stop_improper_power_phase_plot_warning_setting_box.SetValue("True")
                self.stop_improper_power_plotted_lines_warning_setting_box.SetValue("True")
                self.stop_invalid_value_in_function_in_phase_plot_warning_setting_box.SetValue("True")
                self.stop_invalid_value_in_function_in_plotted_lines_warning_setting_box.SetValue("True")
                self.stop_overflow_in_phase_plot_warning_setting_box.SetValue("True")
                self.stop_overflow_in_plotted_lines_warning_setting_box.SetValue("True")
                self.stop_underflow_in_phase_plot_warning_setting_box.SetValue("True")
                self.stop_underflow_in_plotted_lines_warning_setting_box.SetValue("True")

        self.settings["cwd"] = self.cwd

        ## BUTTONS, pannels, textboxes, ...
        dxdt_label =wx.Panel(self.panel, size = (30, 40))
        dxdt_label.Bind(wx.EVT_ERASE_BACKGROUND, self.dxdt_label_maker)
        dxdt_label.SetBackgroundColour("#ffffff") # #ffffff = white

        dydt_label = wx.Panel(self.panel, size = (30, 40))
        dydt_label.Bind(wx.EVT_ERASE_BACKGROUND, self.dydt_label_maker)
        dydt_label.SetBackgroundColour("#ffffff") # #ffffff = white

        self.dxdt_textbox = wx.Panel(self.panel)
        self.dxdt_textbox_text = wx.TextCtrl(self.dxdt_textbox, -1, style=wx.ALIGN_LEFT|wx.TE_MULTILINE, size = (400, 40))
        self.dxdt_textbox_text.SetHint("(a)(b) or a*b for multiplication, a/b for division, ** or a^b for exponents")
        self.dxdt_textbox.SetBackgroundColour("#ffffff") # #ffffff = white
        self.dxdt_textbox.SetMaxSize(wx.Size(2000, 40))
        self.dxdt_textbox.Bind(wx.EVT_SIZE, self.dxdt_text_box_resize)

        self.dydt_textbox = wx.Panel(self.panel)
        self.dydt_textbox_text = wx.TextCtrl(self.dydt_textbox, -1, style=wx.ALIGN_LEFT|wx.TE_MULTILINE, size = (400, 40))
        self.dydt_textbox_text.SetHint("ln or log for natural log, log10 = base 10, log2 = base 2, for trig radians used")
        self.dydt_textbox.SetBackgroundColour("#ffffff") # #ffffff = white
        self.dydt_textbox.SetMaxSize(wx.Size(2000, 40))
        self.dydt_textbox.Bind(wx.EVT_SIZE, self.dydt_text_box_resize)

        self.variables_box = wx.Panel(self.panel, size = (220, 80))
        self.variables_box_text = wx.TextCtrl(parent=self.variables_box, id=-1, style=wx.ALIGN_LEFT|wx.TE_MULTILINE, size=self.variables_box.GetSize())
        self.variables_box_text.SetHint("comma separated variables here (ex. a = 5, b=7, ...)")
        self.variables_box.SetBackgroundColour("#ffffff") # #ffffff = white
        self.variables_box.SetMaxSize(wx.Size(1000, 85))
        self.variables_box.Bind(wx.EVT_SIZE, self.variable_text_box_resize) #This would activate evry time the window is re-sized (good NOTE for later)

        self.bh = 40 # button height
        self.bw = 40 # button width
        bh = 40 # button height
        bw = 40 # button width
        global filepath
        if os.path.exists(self.cwd+"/Graphs"):
            filepath = "file:///"+self.cwd+"/Graphs/Display_Plot_Clear.html"
        else:
            filepath = "file:///"+self.cwd+"/_internal/Graphs/Display_Plot_Clear.html"
        self.display = Display_Window(self.panel)
        self.display.SetBackgroundColour("#ffffff")


        '''
        # This is the old way the buttons were given a background, it does not work very well on linux which is why the 
        # switch was made am keeping this code here as it may be useful latersettings_button = wx.Button(self.panel, label="")
        settings_button.SetMinSize((bw, bh))
        settings_button.SetMaxSize((bw, bh))
        settings_button.SetBackgroundColour("#ffffff")

        settings_photo = wx.Bitmap(self.cwd+"/Photos/Settings_Icon.png")
        image = wx.ImageFromBitmap(settings_photo)
        image = image.Scale(bw, bh, wx.IMAGE_QUALITY_HIGH)
        settings_photo = wx.BitmapFromImage(image)
        settings_button.SetBitmap(settings_photo)
        '''


        ##
        if os.path.exists(self.cwd+"/Photos/Settings_Icon.png"):
            settings_photo = wx.Bitmap(self.cwd+"/Photos/Settings_Icon.png")
        else:
            settings_photo = wx.Bitmap(self.cwd+"/_internal/Photos/Settings_Icon.png")
        image = wx.ImageFromBitmap(settings_photo)
        image = image.Scale(bw, bh, wx.IMAGE_QUALITY_HIGH)
        settings_photo = wx.BitmapFromImage(image)
        settings_button=wx.BitmapButton(self.panel, -1, settings_photo, pos=(bw, bh), style=wx.NO_BORDER)
        settings_button.Bind(wx.EVT_BUTTON, self.settings_button_pushed)
        settings_button.SetBackgroundColour("#282a30")
        ##


        ##
        if os.path.exists(self.cwd+"/Photos/Save_Icon.png"):
            save_file_photo = wx.Bitmap(self.cwd+"/Photos/Save_Icon.png")
        else:
            save_file_photo = wx.Bitmap(self.cwd+"/_internal/Photos/Save_Icon.png")
        image = wx.ImageFromBitmap(save_file_photo)
        image = image.Scale(bw, bh, wx.IMAGE_QUALITY_HIGH)
        save_file_photo = wx.BitmapFromImage(image)
        save_file = wx.BitmapButton(self.panel, -1, save_file_photo, pos=(bw, bh), style=wx.NO_BORDER)
        save_file.Bind(wx.EVT_BUTTON, self.save_file_button_pushed)
        save_file.SetBackgroundColour("#282a30")
        ##

        ##
        if os.path.exists(self.cwd+"/Photos/File_Icon.png"):
            open_file_photo = wx.Bitmap(self.cwd+"/Photos/File_Icon.png")
        else:
            open_file_photo = wx.Bitmap(self.cwd+"/_internal/Photos/File_Icon.png")
        image = wx.ImageFromBitmap(open_file_photo)
        image = image.Scale(bw, bh, wx.IMAGE_QUALITY_HIGH)
        open_file_photo = wx.BitmapFromImage(image)
        open_file = wx.BitmapButton(self.panel, -1, open_file_photo, pos=(bw, bh), style=wx.NO_BORDER)
        open_file.Bind(wx.EVT_BUTTON, self.open_file_button_pushed)
        open_file.SetBackgroundColour("#282a30")
        ##
        if os.path.exists(self.cwd+"/Photos/Help_Icon.png"):
            help_photo = wx.Bitmap(self.cwd+"/Photos/Help_Icon.png")
        else:
            help_photo = wx.Bitmap(self.cwd+"/_internal/Photos/Help_Icon.png")
        image = wx.ImageFromBitmap(help_photo)
        image = image.Scale(bw, bh, wx.IMAGE_QUALITY_HIGH)
        help_photo = wx.BitmapFromImage(image)
        help = wx.BitmapButton(self.panel, -1, help_photo, pos=(bw, bh), style=wx.NO_BORDER)
        help.Bind(wx.EVT_BUTTON, self.help_button_pushed)
        help.SetBackgroundColour("#282a30")
        ##

        ##
        if os.path.exists(self.cwd+"/Photos/Load_Icon.png"):
            load_photo = wx.Bitmap(self.cwd+"/Photos/Load_Icon.png")
        else:
            load_photo = wx.Bitmap(self.cwd+"/_internal/Photos/Load_Icon.png")
        image = wx.ImageFromBitmap(load_photo)
        image = image.Scale(bw, bh, wx.IMAGE_QUALITY_HIGH)
        load_photo = wx.BitmapFromImage(image)
        load = wx.BitmapButton(self.panel, -1, load_photo, pos=(bw, bh), style=wx.NO_BORDER)
        load.Bind(wx.EVT_BUTTON, self.load_button_pushed)
        load.SetBackgroundColour("#282a30")

        ########## Layouts
        l1 = wx.BoxSizer(wx.VERTICAL)
        l2_1 = wx.BoxSizer(wx.HORIZONTAL)
        self.l2_2 = wx.BoxSizer(wx.HORIZONTAL)
        l3_1 = wx.BoxSizer(wx.VERTICAL)
        self.l3_2 = wx.BoxSizer(wx.VERTICAL)
        l4_1 = wx.BoxSizer(wx.HORIZONTAL)
        l4_2 = wx.BoxSizer(wx.HORIZONTAL)

        l4_1.Add(dxdt_label,    proportion=1)
        l4_1.Add(self.dxdt_textbox,  proportion=11, flag=wx.EXPAND)

        l4_2.Add(dydt_label,    proportion=1)
        l4_2.Add(self.dydt_textbox,  proportion=11, flag=wx.EXPAND)

        space_between_buttons = 5
        l3_1.Add(settings_button)
        l3_1.AddSpacer(space_between_buttons)
        l3_1.Add(save_file)
        l3_1.AddSpacer(space_between_buttons)
        l3_1.Add(open_file)
        l3_1.AddSpacer(space_between_buttons)
        l3_1.Add(help)
        l3_1.AddSpacer(space_between_buttons)
        l3_1.Add(load)
        l3_1.AddSpacer(space_between_buttons)

        self.l3_2.Add(l4_1,          proportion=1, flag=wx.EXPAND)
        self.l3_2.AddSpacer(5)
        self.l3_2.Add(l4_2,          proportion=1, flag=wx.EXPAND)

        ba = 5 # border_adjustment
        l2_1.AddSpacer(ba)
        l2_1.Add(self.display,  proportion=40, flag=wx.EXPAND)
        l2_1.AddSpacer(ba)
        l2_1.Add(l3_1,          proportion=1, flag=wx.EXPAND)
        l2_1.AddSpacer(ba)

        self.l2_2.AddSpacer(ba)
        self.l2_2.Add(self.l3_2,          proportion=2)
        self.l2_2.AddSpacer(ba)
        self.l2_2.Add(self.variables_box, proportion=1, flag=wx.EXPAND)
        self.l2_2.AddSpacer(ba)

        l1.AddSpacer(ba)
        l1.Add(l2_1,            proportion=42, flag=wx.EXPAND)
        l1.AddSpacer(ba)
        l1.Add(self.l2_2,       proportion=10, flag=wx.EXPAND)

        self.panel.SetSizer(l1)

        self.Center() # makes it so that application appears in the middle of the screen
        self.Layout()
        self.display.display.SetSize(self.display.GetSize()) # window must be given a size to start or is made really small to start
        self.display.Bind(wx.EVT_SIZE, self.display_resize)
        self.Show()
        ############LAYOUT ENDS ##############

    ###### Functions for Buttons #########

    #NOTE: every function must be passed at least a eventnal since the buttons all recieve an event

    def dxdt_label_maker(self, evt):
        # similar code found in a few spots, one of is https://www.youtube.com/watch?v=C3VX74g75Kc&t=1s
        # Just put a screenshot of text on pannel
        dc = evt.GetDC()
                
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()

        if os.path.exists(self.cwd+"/Photos/dx__dt.png"):
            dxdt_label_file_photo = wx.Bitmap(self.cwd+"/Photos/dx__dt.png")
        else:
            dxdt_label_file_photo = wx.Bitmap(self.cwd+"/_internal/Photos/dx__dt.png")
        image = wx.ImageFromBitmap(dxdt_label_file_photo)
        image = image.Scale(30, 40, wx.IMAGE_QUALITY_HIGH)
        dxdt_label_file_photo = wx.BitmapFromImage(image)
        dc.DrawBitmap(dxdt_label_file_photo, 5, 0)
    
    
    def dydt_label_maker(self, evt):
        dc = evt.GetDC()
                
        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()

        if os.path.exists(self.cwd+"/Photos/dy__dt.png"):
            dydt_label_file_photo = wx.Bitmap(self.cwd+"/Photos/dy__dt.png")
        else:
            dydt_label_file_photo = wx.Bitmap(self.cwd+"/_internal/Photos/dy__dt.png")
        image = wx.ImageFromBitmap(dydt_label_file_photo)
        image = image.Scale(30, 40, wx.IMAGE_QUALITY_HIGH)
        dydt_label_file_photo = wx.BitmapFromImage(image)
        dc.DrawBitmap(dydt_label_file_photo, 5, 0)

    def variable_text_box_resize(self, evt=None):
        self.variables_box_text.SetSize(wx.Size(self.variables_box.GetSize()))

    def dxdt_text_box_resize(self, evt=None):
        self.dxdt_textbox_text.SetSize(wx.Size(self.dxdt_textbox.GetSize()))

    def dydt_text_box_resize(self, evt=None):
        self.dydt_textbox_text.SetSize(wx.Size(self.dydt_textbox.GetSize()))

    def display_resize(self, evt=None):
        self.display.display.SetSize(wx.Size(self.display.GetSize()))


    def settings_button_pushed(self, event):
        settings_window = popup_windows.popup_window(self)
        settings_window.Update_Self_for_Settings(settings=self.settings, load = self.load_button_pushed) #fills out information needed for Settings Window
        settings_window.Settings() #Makes settings window and then returns new setting (which are used) in settings_window.settings
        settings_window.Show()

    def save_file_button_pushed(self, event):
        ##### this is from https://www.blog.pythonlibrary.org/2010/06/26/the-dialogs-of-wxpython-part-1-of-2/
        # with very few modificarions
        dlg = wx.DirDialog(self, "Choose a directory:",
                           style=wx.DD_DEFAULT_STYLE,
                           #| wx.DD_DIR_MUST_EXIST
                           #| wx.DD_CHANGE_DIR
                           )
        if dlg.ShowModal() == wx.ID_OK:
            print("You chose %s" % dlg.GetPath()) #prints where the user selected (program will not work without this statement)
            save_location = dlg.GetPath()
        dlg.Destroy()
        ######
        try:
            with open(save_location+'/settings.json', "w") as f:
                f.write(json.dumps(self.settings))

            if os.path.exists(self.cwd+"/Graphs"):
                shutil.copyfile(self.settings["cwd"]+"/Graphs/Display_Plot.html", save_location+'/Display_Plot.html')
            else:
                shutil.copyfile(self.settings["cwd"]+"/_internal/Graphs/Display_Plot.html", save_location+'/Display_Plot.html')

            with open(save_location+'/Equations.txt', "w") as f:
                f.write(self.dxdt_textbox_text.GetValue()+",")
                f.write(self.dydt_textbox_text.GetValue()+",")
                f.write(self.variables_box_text.GetValue())
        except:
            save_error = popup_windows.popup_window(self)
            save_error.Error("ERROR: file not saved properly", cwd=self.settings["cwd"])
            save_error.Show()

    def open_file_button_pushed(self, event):
        dlg = wx.DirDialog(self, "Choose a directory:",
                    style=wx.DD_DEFAULT_STYLE,
                    #| wx.DD_DIR_MUST_EXIST
                    #| wx.DD_CHANGE_DIR
                    )
        if dlg.ShowModal() == wx.ID_OK:
            print("You chose %s" % dlg.GetPath()) #prints where the user selected (program will not work without this statement)
            file_location = dlg.GetPath()
        dlg.Destroy()

        try:
            #sets the settings
            with open(file_location+'/settings.json', "r") as f:
                self.settings = json.load(f)
            
            #makes directory
            #Need to fix this bit so old directory can be created
            if(os.path.exists(self.settings["cwd"]+self.settings["settings_file"]) != True):
                os.makedirs(self.settings["cwd"]+self.settings["settings_file"], exist_ok=True)
            #copies contents of loaded settings file
            with open(self.settings["cwd"]+self.settings["settings_file"], "w") as f:
                f.write(json.dumps(self.settings))

            #sets the display
            global filepath
            filepath = "file:///"+file_location+'/Display_Plot.html'
            self.display.display.LoadURL(filepath)
            
            #sets the equation boxes
            with open(file_location+'/Equations.txt', "r") as f:
                equation_stuff = f.readline()
                equation_stuff = equation_stuff.split(",")
            self.dxdt_textbox_text.SetValue(equation_stuff[0])
            self.dydt_textbox_text.SetValue(equation_stuff[1])
            self.variables_box_text.SetValue(equation_stuff[2])

            #This does not actually have to be copied back, since if the load button is pushed then everything is all reset
            #shutil.copyfile(file_location+'/Display_Plot.html', self.settings["cwd"]+"/Graphs/Display_Plot.html") # This is copied at the end to the display updates quicker

        except Exception as e:
            file_error = popup_windows.popup_window(self)
            file_error.Error("Error: something is wrong with the saved file " + file_location, cwd=self.settings["cwd"])
            file_error.Show()
            print("error: ", end="")
            print(e)

    def help_button_pushed(self, event):
        window = popup_windows.popup_window(self)
        window.Help("HELP:\n"
                    +"\tTo use this program enter the ODEs you would like to model in the dx/dt and dy/dt boxes\n"
                    +"\tand then press the play button (►).\n"
                    +"\t\tThe following functions may be used:\n"
                    +"\t\t\tsin, cos, tan, arcsin, arccos, arctan, sinh, cosh, tanh, log = ln, log10, log2\n"
                    +"\tIndicate any variables you would like to use in the variables box by typing them out\n"
                    +"\t\tex: a=5, β = 10, length = 7\n"
                    +"\t\t(WARNING: Do not use variables with a name more than 10 characters long, also)\n"
                    +"\t\tdo not use \".\" inside of variable names and do not use the vairbale named\n"
                    +"\t\t\"self\" or reserved words in python (ie True, False, if, ...) if unsure can\n"
                    +"\t\tview https://realpython.com/lessons/reserved-keywords/\n"
                    +"\t\t(all one letter variables will work and any variable including greek will work))\n"
                    +"Settings:\n"
                    +"\tGraph_Visual_Settings:\n"
                    +"\tx_axis_title:  : Controls the title of the x-axis\n"
                    +"\ty_axis_title:  : Controls the title of the y-axis\n"
                    +"\ttitle:         : Controls the title of the graph\n"
                    +"\txmin           : Sets the minimium value for the x axis \n"
                    +"\txmax           : Sets the maximium value for the x axis \n"
                    +"\tymin           : Sets the minimium value for the y axis \n"
                    +"\tymax           : Sets the maximium value for the y axis \n"
                    +"\tarrow_scale    : Sets the scale of the arrows used in the phase plot:\n"
                        +"\t\t\t 1 means arrows are the actual size, <1 means arrows will appear smaller than they \n"
                        +"\t\t\t really are, >1 means arrows appear bigger. If you set to 0 then the arrows will\n"
                        +"\t\t\t be made to be the same size"
                    +"\tstarting_points: This should be a list of tuple(s) which contain the starting points you\n"
                        +"\t\t\t would like the plot to start from, for example [(1,1)] would mean the plot will \n"
                        +"\t\t\t start from the coordinates (1,1), [(1,1),(1,2)] would mean the plot will draw 2 \n"
                        +"\t\t\t separate lines, (from (1,1) and the other from (2,1))\n"
                    +"\show_legend: True if you want a legend, False if you do not"
                    +"\n"
                    +"\tGraph_Background_Settings:\n"
                    +"\th              : This is the change value used in numarical integration\n"
                    +"\txdensity       : The number of arrows used along the x axis in the phase plot\n"
                    +"\tydensity       : The number of arrows used along the y axis in the phase plot\n"
                    +"\tspecify_time   : True or False, if true then the forward steps and backwards steps will\n"
                        +"\t\t\tbe dissabled and changed based on the forward_time and backward_time given.\n"
                    +"\tforward_steps  : Sets the number of iterations of the numarical integration technique\n"
                        +"\t\t\t chosen will use when going forward in time\n"
                    +"\tbackward_steps : Same as forward_steps but for going backwards in time\n"
                    +"\tforward_time   : If you would prefer you can give an amount of time you would like to go\n"
                        +"\t\t\tforward in time and then the step will be calculated automatically,\n"
                        +"\t\t\tWARNING specify_time must be set to True in order for this feature to work.\n"
                    +"\tbackward_time  : Same as forward_time, but for going backward in time\n"
                    +"\tmethod         : Choose the numerical method that you would like to use. Currently can\n"
                        +"\t\t\t choose between Euler (euler or e) and Runge Kutta (runge kutta, kutta, r, k)\n"
                        +"\t\t\t Huen is not yet implemented but will soon be on the way\n"
                    +"\n"
                    +"\tWarning_Settings:\n"
                    +"\tstop_all_warnings: If set to true the all warning popups will be shut off\n"
                    +"\tstop_variable_override_warning: Stops warning from being shown if you decide to overide a\n"
                        +"\t\t\tvariable that is preset, for example e=5 or π=10\n"
                    +"\tstop_termination_warning: This is triggered most times a plot is built, it just signals that\n"
                        +"\t\t\tthe plot stopped generating since it was leaving the viewing area, this stop is placed\n"
                        +"\t\t\tin to prevent numerical errors. It should be safe to turn this warning off it is more\n"
                        +"\t\t\tof an FYI.\n"
                    +"\tstop_numerical_termination_warning: Stop getting warnings when a plot stops plotting due to\n"
                        +"\t\t\tnumerical issues.\n"
                    +"\tstop_improper_power_phase_plot_warning: Stop getting warnings when making the phase plot when\n"
                        +"\t\t\tthere has been an inproper power usage, for example (-5)^0.5, since you cannot take\n"
                        +"\t\t\tthe square root of a negative number."
                    +"\tstop_improper_power_plotted_lines_warning: Stop getting warnings when making plots from the\n"
                        +"\t\t\tinitial conditions given there has been an inproper power usage, for example (-5)^0.5,\n"
                        +"\t\t\tsince you cannot take the square root of a negative."
                    +"\tstop_invalid_value_in_function_in_phase_plot_warning: Stop getting warning when making the\n"
                        +"\t\t\tphase plot and an invalid value has been attempted to be used in a function (ex \n"
                        +"\t\t\tarccos(2) or cos(inf)). This warning is fairly typical if plotting in a range a \n"
                        +"\t\t\tfunction is undefined\n"                    
                    +"\tstop_invalid_value_in_function_in_plotted_lines_warning: Stop getting warning when making a\n"
                        +"\t\t\tplot from initial point(s) and an invalid value has been attempted to be used in a\n"
                        +"\t\t\tfunction (ex arccos(2) or cos(inf)). This warning is fairly typical if plotting in a\n"
                        +"\t\t\trange a function is undefined\n"                     
                    +"\tstop_overflow_in_phase_plot_warning: Stop getting warning when making the phase plot and an\n"
                        +"\t\t\toverflow error occurs, this is an error where there is a number which is too big or a\n"
                        +"\t\t\treally big number is added to a really small number and so the computer must round \n"
                        +"\t\t\t(ex if the biggest number the computer can store is 10, but you have 9+3 then the \n"
                        +"\t\t\tcomputer would store 10).\n"                    
                    +"\tstop_overflow_in_plotted_lines_warning: Stop getting warning when making a plot from initial\n"
                        +"\t\t\tpoint(s) and an overflow error occurs, this is an error where there is a number which\n"
                        +"\t\t\tis too big or a really big number is added to a really small number and so the\n"
                        +"\t\t\tcomputer must round (ex if the biggest number the computer can store is 10, but you \n"
                        +"\t\t\thave 9+3 then the computer would store 10).\n"
                    +"\tstop_underflow_in_phase_plot_warning: Stop getting warning when making the phase plot and you\n"
                        +"\t\t\tget an underflow warning (ex smallest number you can store is 0.1, but you preform \n"
                        +"\t\t\t0.1*0.1=0.01 which the computer then rounds to 0)\n"                    
                    +"\tstop_underflow_in_plotted_lines_warning: Stop getting warning when making a plot from initial\n"
                        +"\t\t\tpoint(s) and you get an underflow warning (ex smallest number you can store is 0.1,\n"
                        +"\t\t\tbut you preform 0.1*0.1=0.01 which the computer then rounds to 0)\n"      
                    +"\tsettings_file  : You may select a new settings file or svae multiple settings files if \n"
                        +"\t\t\t you would like, but do not delete the origional settings file (if you do it will \n"
                        +"\t\t\t just be recreated later)\n"
                    +"\n"
                    +"\tFiles_Settings:\n"
                    +"\tsettings_file: stores the location of the settings file being used, an absolute path will work\n"
                    +"\ton Windows."
                    +"\tSettings Buttons:\n"
                    +"\t\tApply: Applies settings, but does not save them\n"
                    +"\t\tSave: Applies and saves settings in the indicated file\n"
                    +"\t\tReset: Resets all settings to the indicated file\n"
                    +"\t\tDefault: Resets all setting to default values if needed\n"
                    +"Save Button:\n"
                        +"\tThis button allows you to save a copy of the formulas, settings, and loaded html file\n"
                        +"\tto a folder for later use.\n"
                    +"File button:\n"
                        +"\tThis button allows ou to open a saved plot with saved settings and equations for easy\n"
                        +"\tmodification. WARNING: if you load a saved file, the settings file stored in the\n"
                        +"\tsettings_file section in settings will be overwritten with the saved file even if it\n"
                        +"\thas been modified in a different session when using this program"
                    +"\n\nNote: \n"
                        +"\tThis plotter program will stop plotting soon after a max or min value is reached \n"
                    +"\n\nFEEDBACK + BUG REPORT: \n"
                        +"\tIf you have feedback on this program I would be happy to hear it and would also be\n"
                        +"\tinterested in knowing what you are using the program for if you don't mind sharing,\n"
                        +"\tfeel free to reach out at samuelcstreet@gmail.com\n\n"
                        +"\tIf you happen to find a bug I would be happy to know about it so I can fix it, feel\n"
                        +"\tfree to let me know at samuelcstreet@gmail.com\n", self.settings["cwd"])

    def load_button_pushed(self, event=None, from_settings = False):
        #For this function all variables have been made longer than 10 characters long so that the user input does not inpact the program
        
        dxdt_text99 = self.dxdt_textbox_text.GetValue()
        dydt_text99 = self.dydt_textbox_text.GetValue()
        variable_text = self.variables_box_text.GetValue()
        
        if(from_settings==False):
            if(dxdt_text99 == ''):
                window66666 = popup_windows.popup_window(self)
                window66666.Info("load_button_pushed, no dxdt", cwd=self.settings["cwd"])
                window66666.Show()
                return
            if(dydt_text99==''):
                window66666 = popup_windows.popup_window(self)
                window66666.Info("load_button_pushed, no dydt", cwd=self.settings["cwd"])
                window66666.Show()
                return
        


        ####Processing Variables
        variables_text = "" # functions and variables
        
        print("Variables:")
        if(variable_text.strip() != ''):
            special_vars = ["e", "pi", "π"]
            vars4444444 = variable_text.split(",")
            var_names99 = []
            special_funcs = ["sin", "cos", "tan", "arcsin", "arccos", "arctan", "sinh", "cosh", "tanh", "log", "log10", "log2"]
            for v1111111111 in vars4444444:
                v1111111111 = v1111111111.strip()
                v_info66666 = v1111111111.split("=")
                name4444444 = v_info66666[0].strip()
                var_names99.append(name4444444)
                try:
                    exec(v1111111111) # used in the print statement, for log to ensure things are woking properly
                    # if variable is a variable name in this program then the program will fail, need to make error pop up
                except:
                    variable_error_window = popup_windows.popup_window(self)
                    variable_error_window.Error("ERROR, please check over your variables, especially "+str(v1111111111), cwd=self.settings["cwd"])
                    variable_error_window.Show()
                for w1111111111 in special_vars:
                    if(self.settings["stop_variable_override_warning"]==False):
                        if(w1111111111 == name4444444):
                            variable_override_warning = popup_windows.popup_window(self)
                            variable_override_warning.Warning("WARNING: VALUE IN VARIABLES " + w1111111111 + " WILL BE THE VALUE DEFINED BY THE USER", cwd=self.settings["cwd"])
                            variable_override_warning.Show()
                for w1111111111 in special_funcs:
                    if(self.settings["stop_variable_override_warning"]==False):
                        if(w1111111111 == name4444444):
                            variable_override_warning = popup_windows.popup_window(self)
                            variable_override_warning.Warning("WARNING: VALUE IN VARIABLES " + w1111111111 + " WILL BE THE VALUE DEFINED BY THE USER", cwd=self.settings["cwd"])
                            variable_override_warning.Show()
            for name4444444 in var_names99:
                var_text888 = name4444444 + " = " + str(eval(name4444444))
                print(var_text888)
                variables_text = variables_text+" global "+name4444444+"; "+var_text888+"; "
                
        else:
            print("NONE")
        #NOTE: Efficiency-could make counter -2 as no op at end (will not update now in case I am missing something -- need efficiency update)
        ####PROCESSING DXDT 
        counter=len(dxdt_text99)-1 #cannot put this in a for loop range is only evaluated one time
        i1111111111=0
        while i1111111111 < counter:
            point166666=i1111111111
            point266666=i1111111111+2
            if(point266666 == len(dxdt_text99)):
                text4444444 = dxdt_text99[point166666:]
            else:
                text4444444 = dxdt_text99[point166666:point266666]
            if(text4444444 == ")("):
                sub14444444 = dxdt_text99[:point166666+1]
                sub24444444 = dxdt_text99[point266666-1:]
                dxdt_text99 = sub14444444+"*"+sub24444444
            elif(text4444444[0]=="^"):
                sub14444444 = dxdt_text99[:point166666] # here I use the fact that the very last value cannot be an operation
                sub24444444 = dxdt_text99[point166666+1:]
                dxdt_text99 = sub14444444+"**"+sub24444444
            i1111111111+=1
            counter=len(dxdt_text99)-1
        ####PROCESSING DYDT
        i1111111111=0
        counter=len(dydt_text99)-1 #cannot put this in a for loop range is only evaluated one time
        while i1111111111 < counter:
            point166666=i1111111111
            point266666=i1111111111+2
            if(point266666 == len(dydt_text99)):
                text4444444 = dydt_text99[point166666:]
            else:
                text4444444 = dydt_text99[point166666:point266666]
            if(text4444444 == ")("):
                sub14444444 = dydt_text99[:point166666+1]
                sub24444444 = dydt_text99[point266666-1:]
                dydt_text99 = sub14444444+"*"+sub24444444
            elif(text4444444[0]=="^"):
                sub14444444 = dydt_text99[:point166666] # here I use the fact that the very last value cannot be an operation
                sub24444444 = dydt_text99[point166666+1:]
                dydt_text99 = sub14444444+"**"+sub24444444
            i1111111111+=1
            counter=len(dydt_text99)-1
        
        #var_text stors code to access all functions and variables from numpy and also the custom variables

        dxdt_text99 = "lambda x, y: (" + dxdt_text99 + ")"

        dydt_text99 = "lambda x, y: (" + dydt_text99 + ")"

        variables_text.strip() # takes extra white space off the ends

        make_figure(self,dxdt_text=dxdt_text99, dydt_text=dydt_text99, settings=self.settings, variables_text = variables_text, from_settings=from_settings)

        self.reset_display()
    
    def reset_display(self):
        global filepath
        if os.path.exists(self.cwd+"/Graphs"):
            filepath = "file:///"+self.settings["cwd"]+"/Graphs/Display_Plot.html"
        else:
            filepath = "file:///"+self.settings["cwd"]+"/_internal/Graphs/Display_Plot.html"
        #self.display.ClearBackground()
        self.display.display.LoadURL(filepath)


        

        
