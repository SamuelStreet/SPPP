import wx
import wx.lib.scrolledpanel
import os
import json
from Default_Settings import Default

class popup_window(wx.Frame):
    def __init__(self,parent):
        self.frame = wx.Frame.__init__(self, parent, size=(400,700), title="")
        self.SetBackgroundColour("#ffffff") # dark blue grey for the time being
        self.SetSize((460, 200))

    def Help(self, text, cwd):
        icon = wx.Icon(cwd+"\\photos\\Help Icon.png")
        self.SetIcon(icon)
        size = (1150, 500)
        self.panel = wx.lib.scrolledpanel.ScrolledPanel(self, -1, pos=(0,0), size=size, style=wx.SIMPLE_BORDER)
        self.panel.SetupScrolling()
        # self.panel.SetScrollPos(wx.VERTICAL, wx.EVT_SCROLL,True)
        # need to add something that changes the position of the scrollbar on scrolling
        self.SetSize(size)
        font = wx.Font(12, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        textbox_sizer = wx.BoxSizer(wx.VERTICAL) 
        textbox = wx.StaticText(parent=self.panel, id=-1, label=text, style=wx.ALIGN_LEFT|wx.TE_MULTILINE, size=(size[0]-40, 1000), pos=(10,10))
        textbox.SetFont(font)
        textbox_sizer.Add(textbox)
        self.panel.SetSizer(textbox_sizer)
        self.Show()

    def Info(self, text, size = (400, 250), cwd=""):
        icon = wx.Icon(cwd+"\\photos\\Info Icon.png")
        self.SetIcon(icon)
        self.SetSize(size)
        self.SetMinSize(size)
        self.SetMaxSize(size)
        self.panel = wx.Panel(self)
        textbox=wx.StaticText(parent=self.panel, id=-1, label=text, style=wx.ALIGN_LEFT|wx.TE_MULTILINE, size=(size[0]-30, size[1]-35), pos=(10,10))
        font = wx.Font(12, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        textbox.SetFont(font)

    def Warning(self, text, size = (400, 250), cwd=""):
        icon = wx.Icon(cwd+"\\photos\\Warning Icon.png")
        self.SetIcon(icon)
        self.SetSize(size)
        self.SetMinSize(size)
        self.SetMaxSize(size)
        self.panel = wx.Panel(self)
        textbox=wx.StaticText(parent=self.panel, id=-1, label=text, style=wx.ALIGN_LEFT|wx.TE_MULTILINE, size=(size[0]-30, size[1]-50), pos=(10,10))
        font = wx.Font(12, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        textbox.SetFont(font)

    def Error(self, text, size = (400, 250), cwd=""):
        icon = wx.Icon(cwd+"\\photos\\Error Icon.png")
        self.SetIcon(icon)
        self.SetSize(size)
        self.SetMinSize(size)
        self.SetMaxSize(size)
        self.panel = wx.Panel(self)
        textbox = wx.StaticText(parent=self.panel, id=-1, label=text, style=wx.ALIGN_LEFT|wx.TE_MULTILINE, size=(size[0]-30, size[1]-50), pos=(10,10))
        font = wx.Font(12, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        textbox.SetFont(font)

    def Update_Self_for_Settings(self, settings, load, size = (400, 550)):
        self.load = load
        self.settings = settings
        icon = wx.Icon(settings["cwd"]+"\\photos\\Settings Icon.png")
        self.SetIcon(icon)
        self.SetSize(size); self.SetMinSize(size); self.SetMaxSize(size)
        self.panel = wx.Panel(self)

        sw = 200 #setting box width
        sh = 20 #setting box height
        slw = 170 #setting label box width
        slh = 20 #setting label box height
        
        self.l3_xmin = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_xmax = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_ymin = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_ymax = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_arrow_scale = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_starting_points = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_h = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_xdensity = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_ydensity = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_steps = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_method = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_stop_variable_override_warning = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_termination_warning = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_settings_file = wx.BoxSizer(wx.HORIZONTAL)
        # self.l3_cwd = wx.BoxSizer(wx.HORIZONTAL)
        # cwd should not be editable by the user

        def display_settings(setting):
            setting_string = "" \
            "self."+setting+"_panel_1 = wx.Panel(self.panel)\n" \
            "wx.StaticText(parent=self."+setting+"_panel_1, id=-1, label=\""+setting+": \", style=wx.ALIGN_LEFT, size=(slw, slh), pos=(10,5))\n" \
            "#\n" \
            "self."+setting+"_panel_2 = wx.Panel(self.panel)\n" \
            "self."+setting+"_setting_box = wx.TextCtrl(self."+setting+"_panel_2, -1, style=wx.ALIGN_LEFT, size = (sw, sh), pos=(0,5))\n" \
            "self."+setting+"_setting_box.SetValue(str(self.settings[\""+setting+"\"]))\n" \
            "#\n" \
            "self.l3_"+setting+".Add(self."+setting+"_panel_1, proportion=6)\n" \
            "self.l3_"+setting+".Add(self."+setting+"_panel_2, proportion=5)\n"

            return(setting_string)

        for key in self.settings.keys():
            if(key != "cwd"): # cwd should not be edited by the user
                setting_display_string = display_settings(key)
                exec(setting_display_string)
    
    def Settings(self):
        self.panel.save_settings_button = wx.Button(self.panel, label="Save")
        self.panel.save_settings_button.Bind(wx.EVT_BUTTON, self.save_settings_button_pushed)
        self.panel.apply_settings_button = wx.Button(self.panel, label="Apply")
        self.panel.apply_settings_button.Bind(wx.EVT_BUTTON, self.apply_settings_button_pushed)
        self.panel.reset_settings_button = wx.Button(self.panel, label="Reset") # reset setting to saved settings
        self.panel.reset_settings_button.Bind(wx.EVT_BUTTON, self.reset_settings_button_pushed)
        self.panel.default_settings_button = wx.Button(self.panel, label="Default") # reset settings to defealt settings
        self.panel.default_settings_button.Bind(wx.EVT_BUTTON, self.default_settings_button_pushed)

        self.l1 = wx.BoxSizer(wx.VERTICAL)
        self.l2_1 = wx.BoxSizer(wx.HORIZONTAL)
        self.l2_2 = wx.BoxSizer(wx.VERTICAL)

        self.l2_1.Add(self.panel.apply_settings_button,  proportion=1, flag=wx.EXPAND)
        self.l2_1.Add(self.panel.save_settings_button, proportion=1, flag=wx.EXPAND)
        self.l2_1.Add(self.panel.reset_settings_button,  proportion=1, flag=wx.EXPAND)
        self.l2_1.Add(self.panel.default_settings_button,  proportion=1, flag=wx.EXPAND)

        for key in self.settings.keys():
            if key != "cwd": # CWD should not be edited by user
                exec('self.l2_2.Add(self.l3_'+key+', proportion=1, flag=wx.EXPAND)')
        
        self.l1.Add(self.l2_1, proportion=1, flag=wx.EXPAND)
        self.l1.Add(self.l2_2, proportion=15, flag=wx.EXPAND)

        self.panel.SetSizer(self.l1)
        self.Layout()

    def apply_settings_button_pushed(self, sig=None):        
        self.settings["xmin"] = float(self.xmin_setting_box.GetValue())
        self.settings["xmax"] = float(self.xmax_setting_box.GetValue())
        self.settings["ymin"] = float(self.ymin_setting_box.GetValue())
        self.settings["ymax"] = float(self.ymax_setting_box.GetValue())
        self.settings["arrow_scale"] = float(self.arrow_scale_setting_box.GetValue())
        self.settings["starting_points"] = eval(self.starting_points_setting_box.GetValue())
        self.settings["h"] = float(self.h_setting_box.GetValue())
        self.settings["xdensity"] = float(self.xdensity_setting_box.GetValue())
        self.settings["ydensity"] = float(self.ydensity_setting_box.GetValue())
        self.settings["steps"] = int(self.steps_setting_box.GetValue())
        self.settings["method"] = self.method_setting_box.GetValue()
        self.settings["stop_variable_override_warning"] = bool(self.stop_variable_override_warning_setting_box.GetValue())
        self.settings["termination_warning"] = bool(self.termination_warning_setting_box.GetValue())
        self.settings["settings_file"] = self.settings_file_setting_box.GetValue()
        # self.settings["cwd"] = self.cwd_setting_box.GetValue()
        # cwd should not be edited
        self.load(from_settings=True)

    def save_settings_button_pushed(self, sig):
        self.apply_settings_button_pushed()
        if(self.settings["settings_file"][0]!="\\"):
            self.settings["settings_file"] = "\\"+self.settings["cwd"]
        if(self.settings["settings_file"]==""):
            cwd = self.settings["cwd"]
            variable_override_warning = popup_window(self).Error("Error: settings_file is unspecified so unfortunatly I don't know where to get settings", cwd=cwd)
            variable_override_warning.Show()
        elif not os.path.exists(self.settings["cwd"]+"\\".join(self.settings["settings_file"].split("\\")[:-1])):
            # "\\".join(self.settings["settings_file"].split("\\")[:-1]) 
            # self.settings["settings_file"] = custome settings file
            # .split("\\") = makes list sperarating all different directories in custome settings file
            # [:-1] take all but the actual file name
            # "\\".join put everything back together again with "\\" between every item in the list
            cwd = self.settings["cwd"]
            variable_override_warning = popup_window(self).Error("Error: settings file specified "+ self.settings["settings_file"][1:] + " is missing so I don't know where to go", cwd=cwd)
            variable_override_warning.Show()
        else:
            try:
                with open(self.settings["cwd"]+self.settings["settings_file"], "w") as f:
                    f.write(json.dumps(self.settings))
            except:
                pass #Warning here: make sure file system for specified file exists

            if not os.path.exists(self.settings["cwd"]+'\\settings.json'):
                default_class_instance = Default()
                settings = default_class_instance.settings
                settings["settings_file"] = self.settings["settings_file"]

                with open(self.settings["cwd"]+'\\settings.json', "w") as f:
                    f.write(json.dumps(settings))
            else:
                with open(self.settings["cwd"]+'\\settings.json', "r") as json_file:
                    temp_settings = json.load(json_file)
                temp_settings["settings_file"] = self.settings["settings_file"]
                with open(self.settings["cwd"]+'\\settings.json', "w") as f:
                    f.write(json.dumps(temp_settings))

    def reset_settings_button_pushed(self, sig=None):
        if(self.settings["settings_file"][0]!="\\"):
            self.settings["settings_file"] = "\\"+self.settings["cwd"]
        if(self.settings["settings_file"]==""):
            cwd = self.settings["cwd"]
            variable_override_warning = popup_window(self).Error("Error: settings_file is unspecified so unfortunatly I don't know where to get settings", cwd=cwd)
            variable_override_warning.Show()
        elif not os.path.exists(self.settings["cwd"]+self.settings["settings_file"]):
            cwd = self.settings["cwd"]
            variable_override_warning = popup_window(self).Error("Error: settings file specified "+ self.settings["settings_file"][1:] + " is missing so I don't know where to go", cwd=cwd)
            variable_override_warning.Show()
        else:
            with open(self.settings["cwd"]+self.settings["settings_file"], "r") as json_file:
                self.settings = json.load(json_file)
            self.xmin_setting_box.SetValue(str(self.settings["xmin"]))
            self.xmax_setting_box.SetValue(str(self.settings["xmax"]))
            self.ymin_setting_box.SetValue(str(self.settings["ymin"]))
            self.ymax_setting_box.SetValue(str(self.settings["ymax"]))
            self.arrow_scale_setting_box.SetValue(str(self.settings["arrow_scale"]))
            self.starting_points_setting_box.SetValue(str(self.settings["starting_points"]))
            self.h_setting_box.SetValue(str(self.settings["h"]))
            self.xdensity_setting_box.SetValue(str(self.settings["xdensity"]))
            self.ydensity_setting_box.SetValue(str(self.settings["ydensity"]))
            self.steps_setting_box.SetValue(str(self.settings["steps"]))
            self.method_setting_box.SetValue(str(self.settings["method"]))
            self.stop_variable_override_warning_setting_box.SetValue(str(self.settings["stop_variable_override_warning"]))
            self.termination_warning_setting_box.SetValue(str(self.settings["termination_warning"]))
            self.settings_file_setting_box.SetValue(str(self.settings["settings_file"]))
            # self.cwd_setting_box.SetValue(str(self.settings["cwd"]))
            # cwd should not be edited
            self.load(from_settings=True)


    def default_settings_button_pushed(self, s):
        default_class_instance = Default()
        
        # have to set settings individually or else pointer will just move, could also have used for loop or other method,
        # but this is what I went with
        
        self.settings["xmin"] = default_class_instance.settings["xmin"]
        self.settings["xmax"] = default_class_instance.settings["xmax"]
        self.settings["ymin"] = default_class_instance.settings["ymin"]
        self.settings["ymax"] = default_class_instance.settings["ymax"]
        self.settings["arrow_scale"] = default_class_instance.settings["arrow_scale"]
        self.settings["starting_points"] = default_class_instance.settings["starting_points"]
        self.settings["h"] = default_class_instance.settings["h"]
        self.settings["xdensity"] = default_class_instance.settings["xdensity"]
        self.settings["ydensity"] = default_class_instance.settings["ydensity"]
        self.settings["steps"] = default_class_instance.settings["steps"]
        self.settings["method"] = default_class_instance.settings["method"]
        self.settings["stop_variable_override_warning"] = default_class_instance.settings["stop_variable_override_warning"]
        self.settings["termination_warning"] = default_class_instance.settings["termination_warning"]
        self.settings["settings_file"] = default_class_instance.settings["settings_file"]
        #self.settings["cwd"] = default_class_instance.settings["cwd"]
        #cwd should not be edited

        self.xmin_setting_box.SetValue(str(self.settings["xmin"]))
        self.xmax_setting_box.SetValue(str(self.settings["xmax"]))
        self.ymin_setting_box.SetValue(str(self.settings["ymin"]))
        self.ymax_setting_box.SetValue(str(self.settings["ymax"]))
        self.arrow_scale_setting_box.SetValue(str(self.settings["arrow_scale"]))
        self.starting_points_setting_box.SetValue(str(self.settings["starting_points"]))
        self.h_setting_box.SetValue(str(self.settings["h"]))
        self.xdensity_setting_box.SetValue(str(self.settings["xdensity"]))
        self.ydensity_setting_box.SetValue(str(self.settings["ydensity"]))
        self.steps_setting_box.SetValue(str(self.settings["steps"]))
        self.method_setting_box.SetValue(str(self.settings["method"]))
        self.stop_variable_override_warning_setting_box.SetValue(str(self.settings["stop_variable_override_warning"]))
        self.termination_warning_setting_box.SetValue(str(self.settings["termination_warning"]))
        self.settings_file_setting_box.SetValue(str(self.settings["settings_file"]))
        #self.cwd_setting_box.SetValue(str(self.settings["cwd"]))
        #cwd should not be edited
        self.apply_settings_button_pushed()

        # just need to make sure this is sent back properly

    def Save(self, text="", size = (250, 150), cwd=""):
        icon = wx.Icon(cwd+"\\photos\\Save Icon.png")
        self.SetIcon(icon)
        self.SetSize(size)
        self.SetMinSize(size)
        self.SetMaxSize(size)
        self.panel = wx.Panel(self)
        wx.StaticText(parent=self.panel, id=-1, label=text, style=wx.ALIGN_LEFT|wx.TE_MULTILINE, size=(size[0]-30, size[1]-50), pos=(10,10))

    def File(self, text="", size = (250, 150), cwd=""):
        icon = wx.Icon(cwd+"\\photos\\File Icon.png")
        self.SetIcon(icon)
        self.SetSize(size)
        self.SetMinSize(size)
        self.SetMaxSize(size)
        self.panel = wx.Panel(self)
        wx.StaticText(parent=self.panel, id=-1, label=text, style=wx.ALIGN_LEFT|wx.TE_MULTILINE, size=(size[0]-30, size[1]-50), pos=(10,10))

if __name__ == "__main__":
    app = wx.App()
    window = popup_window(parent=None)
    window.Help("yo, you need help? Here is some: yata yata  yata yata  yata yata  yata yata  yata yata  yata yata  yata yata ")
    window.Show()
    window = popup_window(parent=None)
    window.Info("Info Info Info Info Info Info Info Info Info Info Info Info Info Info Info Info Info")
    window.Show()
    window = popup_window(parent=None)
    window.Warning("Warning Warning Warning Warning Warning Warning Warning Warning Warning Warning Warning Warning Warning ")
    window.Show()
    window = popup_window(parent=None)
    window.Error("Error Error Error Error Error Error Error Error Error Error Error Error Error Error Error Error Error Error ")
    window.Show()
    app.MainLoop()
