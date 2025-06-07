import wx
import wx.html2
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
        self.display=wx.html2.WebView.New(self)
        global filepath
        self.display.LoadURL(filepath)

#This is the main class for the application, settings stored here when running
class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title = "S Phase Plane Plotter")
        
        self.cwd = os.getcwd()

        if not os.path.exists(self.cwd+'\\photos'):
            os.makedirs(self.cwd+'\\photos')
        
        icon = wx.Icon(self.cwd+'\\photos\\PPP Logo.png')
        self.SetIcon(icon)
        self.SetBackgroundColour("#282a30") # dark blue grey for the time being
        self.SetMinSize((600,400))
        self.SetSize((850, 600))

        self.panel = wx.Panel(self) # for holding things (things should not be held just by the window)

        # Sets up the settings allow allowing for multiple files. 
        if not os.path.exists(self.cwd+'\\settings.json'):
            default_class_instance = Default()
            self.settings = default_class_instance.settings
            with open(self.cwd+'\\settings.json', "w") as f:
                f.write(json.dumps(default_class_instance.settings))
        else:
            with open(self.cwd+'\\settings.json', "r") as json_file:
                self.settings = json.load(json_file)
            if not os.path.exists(self.cwd+self.settings["settings_file"]):
                variable_override_warning = popup_windows.popup_window(self)
                variable_override_warning.Warning("WARNING: settings file specified "+ self.settings["settings_file"][1:] + " is missing so I have reverted to default settings", cwd=self.settings["cwd"])
                variable_override_warning.Show()
                default_class_instance = Default()
                self.settings = default_class_instance.settings
            else:
                with open(self.cwd+self.settings["settings_file"], "r") as json_file:
                    self.settings = json.load(json_file)


        self.settings["cwd"] = self.cwd

        ## BUTTONS, pannels, textboxes, ...
        dxdt_label =wx.Panel(self.panel, size = (80, 40))
        wx.StaticText(parent=dxdt_label, id=-1, label="dx/dt", style=wx.ALIGN_CENTER, size=dxdt_label.GetSize())
        dxdt_label.SetBackgroundColour("#ffffff") # #ffffff = white

        dydt_label = wx.Panel(self.panel, size = (80, 40))
        wx.StaticText(parent=dydt_label, id=-1, label="dy/dt", style=wx.ALIGN_CENTER, size=dydt_label.GetSize())
        dydt_label.SetBackgroundColour("#ffffff") # #ffffff = white

        dxdt_textbox = wx.Panel(self.panel)
        self.dxdt_textbox_text = wx.TextCtrl(dxdt_textbox, -1, style=wx.ALIGN_LEFT, size = (450, 40))
        self.dxdt_textbox_text.SetHint("(a)(b) or a*b for multiplication, a/b for division, ** or a^b for exponents")
        dxdt_textbox.SetBackgroundColour("#ffffff") # #ffffff = white
        dxdt_textbox.SetMaxSize((1000, 40))

        dydt_textbox = wx.Panel(self.panel)
        self.dydt_textbox_text = wx.TextCtrl(dydt_textbox, -1, style=wx.ALIGN_LEFT, size = (450, 40))
        self.dydt_textbox_text.SetHint("ln or log for natural log, log10 = base 10, log2 = base 2, for trig radians used")
        dydt_textbox.SetBackgroundColour("#ffffff") # #ffffff = white
        dydt_textbox.SetMaxSize((1000, 40))

        variables_box = wx.Panel(self.panel, size = (200, 85))
        self.variables_box_text = wx.TextCtrl(parent=variables_box, id=-1, style=wx.ALIGN_LEFT|wx.TE_MULTILINE, size=variables_box.GetSize())
        self.variables_box_text.SetHint("comma separated variables here (ex. a = 5, b=7, ...)")
        variables_box.SetBackgroundColour("#ffffff") # #ffffff = white

        bh = 40 # button height
        bw = 40 # button width
        global filepath
        filepath = "file:///"+self.cwd+"/Display_Plot_Clear.html"
        self.display = Display_Window(self.panel)
        self.display.SetBackgroundColour("#ffffff")


        settings_button = wx.Button(self.panel, label="")
        settings_button.SetMinSize((bw, bh))
        settings_button.SetMaxSize((bw, bh))
        settings_button.SetBackgroundColour("#ffffff")
        ##
        settings_photo = wx.Bitmap(self.cwd+"\photos\Settings Icon.png")
        image = wx.ImageFromBitmap(settings_photo)
        image = image.Scale(bw, bh, wx.IMAGE_QUALITY_HIGH)
        settings_photo = wx.BitmapFromImage(image)
        settings_button.SetBitmap(settings_photo)
        ##
        settings_button.Bind(wx.EVT_BUTTON, self.settings_button_pushed)


        save_file = wx.Button(self.panel, label="")
        save_file.SetBackgroundColour("#ffffff")
        save_file.SetMaxSize((bw, bh))
        save_file.SetMinSize((bw, bh))
        ##
        save_file_photo = wx.Bitmap(self.cwd+"\\photos\\Save Icon.png")
        image = wx.ImageFromBitmap(save_file_photo)
        image = image.Scale(bw, bh, wx.IMAGE_QUALITY_HIGH)
        save_file_photo = wx.BitmapFromImage(image)
        save_file.SetBitmap(save_file_photo)
        ##
        save_file.Bind(wx.EVT_BUTTON, self.save_file_button_pushed)

        open_file = wx.Button(self.panel, label="")
        open_file.SetBackgroundColour("#ffffff")
        open_file.SetMaxSize((bw, bh))
        ##
        open_file_photo = wx.Bitmap(self.cwd+"\\photos\\File Icon.png")
        image = wx.ImageFromBitmap(open_file_photo)
        image = image.Scale(bw, bh, wx.IMAGE_QUALITY_HIGH)
        open_file_photo = wx.BitmapFromImage(image)
        open_file.SetBitmap(open_file_photo)
        ##
        open_file.Bind(wx.EVT_BUTTON, self.open_file_button_pushed)

        help = wx.Button(self.panel, label="")
        help.SetBackgroundColour("#ffffff")
        help.SetMaxSize((bw, bh))
        ##
        help_photo = wx.Bitmap(self.cwd+"\\photos\\Help Icon.png")
        image = wx.ImageFromBitmap(help_photo)
        image = image.Scale(bw, bh, wx.IMAGE_QUALITY_HIGH)
        help_photo = wx.BitmapFromImage(image)
        help.SetBitmap(help_photo)
        ##
        help.Bind(wx.EVT_BUTTON, self.help_button_pushed)

        load = wx.Button(self.panel, label="")
        load.SetBackgroundColour("#ffffff")
        load.SetMaxSize((bw, bh))
        ##
        load_photo = wx.Bitmap(self.cwd+"\\photos\\Load Icon.png")
        image = wx.ImageFromBitmap(load_photo)
        image = image.Scale(bw, bh, wx.IMAGE_QUALITY_HIGH)
        load_photo = wx.BitmapFromImage(image)
        load.SetBitmap(load_photo)
        ##
        load.Bind(wx.EVT_BUTTON, self.load_button_pushed)

        ########## Layouts
        l1 = wx.BoxSizer(wx.VERTICAL)
        l2_1 = wx.BoxSizer(wx.HORIZONTAL)
        l2_2 = wx.BoxSizer(wx.HORIZONTAL)
        l3_1 = wx.BoxSizer(wx.VERTICAL)
        l3_2 = wx.BoxSizer(wx.VERTICAL)
        l4_1 = wx.BoxSizer(wx.HORIZONTAL)
        l4_2 = wx.BoxSizer(wx.HORIZONTAL)

        l4_1.Add(dxdt_label,    proportion=1, flag=wx.EXPAND)
        l4_1.Add(dxdt_textbox,  proportion=6, flag=wx.EXPAND)

        l4_2.Add(dydt_label,    proportion=1)
        l4_2.Add(dydt_textbox,  proportion=6, flag=wx.EXPAND)

        space_between_buttons = 5
        l3_1.Add(settings_button,      proportion=1, flag=wx.EXPAND)
        l3_1.AddSpacer(space_between_buttons)
        l3_1.Add(save_file,     proportion=1, flag=wx.EXPAND)
        l3_1.AddSpacer(space_between_buttons)
        l3_1.Add(open_file,     proportion=1, flag=wx.EXPAND)
        l3_1.AddSpacer(space_between_buttons)
        l3_1.Add(help,          proportion=1, flag=wx.EXPAND)
        l3_1.AddSpacer(space_between_buttons)
        l3_1.Add(load,          proportion=1, flag=wx.EXPAND)

        l3_2.Add(l4_1,          proportion=1, flag=wx.EXPAND)
        l3_2.Add(l4_2,          proportion=1, flag=wx.EXPAND)

        ba = 5 # border_adjustment
        l2_1.AddSpacer(ba)
        l2_1.Add(self.display,       proportion=20, flag=wx.EXPAND)
        l2_1.AddSpacer(ba)
        l2_1.Add(l3_1,          proportion=1, flag=wx.EXPAND)
        l2_1.AddSpacer(ba)

        l2_2.AddSpacer(ba)
        l2_2.Add(l3_2,          proportion=1, flag=wx.EXPAND)
        l2_2.AddSpacer(ba)
        l2_2.Add(variables_box, proportion=1, flag=wx.EXPAND)
        l2_2.AddSpacer(ba)

        l1.AddSpacer(ba)
        l1.Add(l2_1,            proportion=4, flag=wx.EXPAND)
        l1.AddSpacer(ba)
        l1.Add(l2_2,            proportion=1, flag=wx.EXPAND)
        l1.AddSpacer(ba)

        self.panel.SetSizer(l1)
        ############LAYOUT ENDS ##############

        ###### Functions for Buttons #########

        self.Center() # makes it so that application appears in the middle of the screen
        self.Layout()
        self.display.display.SetSize(self.display.GetSize())
        self.Show()

    #NOTE: every function must be passed at least a signal since the buttons all send a signal
    #from Phase_Plot_App import frame

    def settings_button_pushed(self, sig):
        settings_window = popup_windows.popup_window(self)
        settings_window.Update_Self_for_Settings(settings=self.settings, load = self.load_button_pushed) #fills out information needed for Settings Window
        settings_window.Settings() #Makes settings window and then returns new setting (which are used) in settings_window.settings
        settings_window.Show()

    def save_file_button_pushed(self, sig):
        save_window = popup_windows.popup_window(self)
        save_window.Save(cwd=self.settings["cwd"])
        save_window.Show()

    def open_file_button_pushed(self, sig):
        file_window = popup_windows.popup_window(self)
        file_window.File(cwd=self.settings["cwd"])
        file_window.Show()

    def help_button_pushed(self, sig):
        window = popup_windows.popup_window(self)
        window.Help("HELP\n \
        Functions which have been implemented: sin, cos, tan, arcsin, arccos, arctan, sinh, cosh, tanh, log = ln, log10, log2\n \
        To use the Variables box just type in your variables in a comma separated formate, please do not use variables that have \
        the smae name as implemented functions\n\n"
        +"TO USE:\n \
        Type formula for dx/dy and dydt, type out variables and then press the load button in order to get the plot to load. \
        Use settings in order to modify how the plot is made. To save your formulas and variables press the save button  \
        + ICON HERE +, to load a previously saved formula and variables press the open file button + ICON HERE + NOTE:  \
        THESE FEATURES ARE NOT YET ACTIVE. If you would like you make also upgrade to the plus version of this program  \
        which has all the same features as this program, but also plots 3D functions -- Also not yet implemented. \n\n\
        SETTINGS:\n \
        xmin           : Sets the minimium value for the x axis \n \
        xmax           : Sets the maximium value for the x axis \n \
        ymin           : Sets the minimium value for the y axis \n \
        ymax           : Sets the maximium value for the y axis \n \
        arrow_scale    : Sets the scale of the arrows used in the phase plot, less than 1 means arrows will appear smaller than they really are \n \
        starting_points: this should be a list of tuple(s) which contain the starting points you would like the plot to start \
        from, for example [(1,1)] would mean the plot will start from the coordinates (1,1), [(1,1),(1,2)] would mean the plot will \
        draw 2 separate lines, 1 from (1,1) and the other from (2,1) \n \
        h              : This is the change value used in numarical integration \n \
        xdensity       : This number coresponds to the number of arrows that will be used along the x axis in the phase plot \
        larger means more arrows \n \
        ydensity       : This number coresponds to the number of arrows that will be used along the y axis in the phase plot \
        larger means more arrows \n \
        steps          : Sets the number of iterations the numarical integration technique chosen will use \n \
        method         : Chose the numerical method that you would like to use. Currently can only select Euler, \
        more will be added with updates\n\n \
        Note: \n \
        This plotter program will stop plotting soon after a max or min value is reached \n \
        Do NOT DELETE settings.json, will revert to default settings even if other file was specified, can re-specify new file", self.settings["cwd"])


    def load_button_pushed(self, sig=None, from_settings = False):
        dxdt_text = self.dxdt_textbox_text.GetValue()
        dydt_text = self.dydt_textbox_text.GetValue()
        variable_text = self.variables_box_text.GetValue()
        
        if(from_settings==False):
            if(dxdt_text == ''):
                window = popup_windows.popup_window(self)
                window.Info("load_button_pushed, no dxdt", cwd=self.settings["cwd"])
                window.Show()
                return
            if(dydt_text==''):
                window = popup_windows.popup_window(self)
                window.Info("load_button_pushed, no dydt", cwd=self.settings["cwd"])
                window.Show()
                return
        


        ####Processing Variables
        variables_text = "" # functions and variables
        
        print("Variables:")
        if(variable_text.strip() != ''):
            special_vars = ["e", "pi", "π"]
            vars = variable_text.split(",")
            var_names = []
            special_funcs = ["sin", "cos", "tan", "arcsin", "arccos", "arctan", "sinh", "cosh", "tanh", "log", "log10", "log2"]
            for vvvvv in vars:
                vvvvv = vvvvv.strip()
                v_info = vvvvv.split("=")
                name = v_info[0].strip()
                var_names.append(name)
                try:
                    exec(vvvvv) # used in the print statement, for log to ensure things are woking properly
                    # if variable is a variable name in this program then the program will fail, need to make error pop up
                except:
                    variable_error_window = popup_windows.popup_window(self)
                    variable_error_window.Error("ERROR, please check over your variables", self.settings["cwd"])
                    variable_error_window.Show()
                for wwwww in special_vars:
                    if(wwwww == name):
                        variable_override_warning = popup_windows.popup_window(self)
                        variable_override_warning.Warning("WARNING: VALUE IN VARIABLES " + wwwww + " WILL BE THE VALUE DEFINED BY THE USER", cwd=self.settings["cwd"])
                        variable_override_warning.Show()
                for wwwww in special_funcs:
                    if(wwwww == name):
                        variable_override_warning = popup_windows.popup_window(self)
                        variable_override_warning.Warning("WARNING: VALUE IN VARIABLES " + wwwww + " WILL BE THE VALUE DEFINED BY THE USER", cwd=self.settings["cwd"])
                        variable_override_warning.Show()
            for name in var_names:
                var_text = name + " = " + str(eval(name))
                print(var_text)
                variables_text = variables_text+" global "+name+"; "+var_text+"; "
                
        else:
            print("NONE")
        ####PROCESSING DXDT
        for iiiii in range(len(dxdt_text)-1):
            point1=iiiii
            point2=iiiii+2
            if(point2 == len(dxdt_text)):
                text = dxdt_text[point1:]
            else:
                text = dxdt_text[point1:point2]
            if(text == ")("):
                sub1 = dxdt_text[:point1+1]
                sub2 = dxdt_text[point2:]
                dxdt_text = sub1+"*"+sub2
            elif(text[0]=="^"):
                sub1 = dxdt_text[:point1] # here I use the fact that the very last value cannot be an operation
                sub2 = dxdt_text[point1+1:]
                dxdt_text = sub1+"**"+sub2
        ####PROCESSING DYDT
        for iiiii in range(len(dydt_text)-1):
            point1=iiiii
            point2=iiiii+2
            if(point2 == len(dydt_text)):
                text = dydt_text[point1:]
            else:
                text = dydt_text[point1:point2]
            if(text == ")("):
                sub1 = dydt_text[:point1+1]
                sub2 = dydt_text[point2:]
                dydt_text = sub1+"*"+sub2
            elif(text[0]=="^"):
                sub1 = dydt_text[:point1] # here I use the fact that the very last value cannot be an operation
                sub2 = dydt_text[point1+1:]
                dydt_text = sub1+"**"+sub2
        
        #var_text stors code to access all functions and variables from numpy and also the custom variables

        dxdt_text = "lambda x, y: (" + dxdt_text + ")"

        dydt_text = "lambda x, y: (" + dydt_text + ")"

        variables_text.strip() # takes extra white space off the ends

        make_figure(self,dxdt_text=dxdt_text, dydt_text=dydt_text, settings=self.settings, variables_text = variables_text, from_settings=from_settings)

        self.reset_display()
    
    def reset_display(self):
        global filepath
        filepath = "file:///"+self.settings["cwd"]+"/Display_Plot.html"
        
        #self.display.ClearBackground()
        self.display.display.LoadURL(filepath)


        

        
