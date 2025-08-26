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
        if os.path.exists(cwd+"/Photos/Help_Icon.png"):
            icon = wx.Icon(cwd+"/Photos/Help_Icon.png")
        else:
            icon = wx.Icon(cwd+"/_internal/Photos/Help_Icon.png")
        self.SetIcon(icon)
        size = (1150, 500)

        '''#Alternate method of displaying help, may need to implement this method to prevent 
        #slow scrolling 
        self.panel = wx.Panel(self)
        self.l1 = wx.BoxSizer(wx.VERTICAL)
        self.l2 = wx.BoxSizer(wx.HORIZONTAL)

        self.help_scroller_panel = wx.lib.scrolledpanel.ScrolledPanel(self.panel,-1,size=size, style=wx.SIMPLE_BORDER|wx.EXPAND)
        self.help_scroller_panel.SetupScrolling(scroll_x=False, scroll_y=True)
        self.help_scroller_panel.SetBackgroundColour('#FFFFFF')

        self.help_text_panel = wx.Panel(self.help_scroller_panel)
        font = wx.Font(12, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        help_textbox = wx.StaticText(parent=self.help_text_panel, id=-1, label = text, style=wx.ALIGN_LEFT, size=(size[0]-40, 2200), pos=(10,10))
        help_textbox.SetFont(font)
        self.l2.Add(self.help_text_panel, proportion=1)

        self.help_scroller_panel.SetSizer(self.l2)
        self.l1.Add(self.help_scroller_panel, proportion=1, flag=wx.EXPAND)

        self.panel.SetSizer(self.l1)
        self.Layout()'''

        self.panel = wx.lib.scrolledpanel.ScrolledPanel(self, -1, pos=(0,0), size=size, style=wx.SIMPLE_BORDER)
        self.panel.SetupScrolling(scroll_x=False, scroll_y=True)
        # self.panel.SetScrollPos(wx.VERTICAL, wx.EVT_SCROLL,True)
        # need to add something that changes the position of the scrollbar on scrolling
        self.SetSize(size)
        font = wx.Font(12, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        textbox_sizer = wx.BoxSizer(wx.VERTICAL) 
        textbox = wx.StaticText(parent=self.panel, id=-1, label=text, style=wx.ALIGN_LEFT|wx.TE_MULTILINE, size=(size[0]-40, 2200), pos=(10,10))
        textbox.SetFont(font)
        textbox_sizer.Add(textbox)
        self.panel.SetSizer(textbox_sizer)
        self.Show()

    def Info(self, text, size = (400, 250), cwd=""):
        if os.path.exists(cwd+"/Photos/Info_Icon.png"):
            icon = wx.Icon(cwd+"/Photos/Info_Icon.png")
        else:
            icon = wx.Icon(cwd+"/_internal/Photos/Info_Icon.png")
        self.SetIcon(icon)
        self.SetSize(size)
        self.SetMinSize(size)
        self.SetMaxSize(size)
        self.panel = wx.Panel(self)
        textbox = wx.TextCtrl(parent=self.panel, id=-1, style=wx.ALIGN_LEFT|wx.TE_MULTILINE, size=(size[0]-30, size[1]-50), pos=(10,10))
        textbox.SetLabelText(text)
        textbox.SetEditable(False)
        font = wx.Font(12, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        textbox.SetFont(font)

    def Warning(self, text, size = (400, 250), cwd=""):
        if os.path.exists(cwd+"/Photos/Warning_Icon.png"):
            icon = wx.Icon(cwd+"/Photos/Warning_Icon.png")
        else:
            icon = wx.Icon(cwd+"/_internal/Photos/Warning_Icon.png")
        self.SetIcon(icon)
        self.SetSize(size)
        self.SetMinSize(size)
        self.SetMaxSize(size)
        self.panel = wx.Panel(self)
        textbox=wx.TextCtrl(parent=self.panel, id=-1, style=wx.ALIGN_LEFT|wx.TE_MULTILINE, size=(size[0]-30, size[1]-50), pos=(10,10))
        textbox.SetLabelText(text)
        textbox.SetEditable(False)
        font = wx.Font(12, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        textbox.SetFont(font)

    def Error(self, text, size = (400, 250), cwd=""):
        if os.path.exists(cwd+"/Photos/Error_Icon.png"):
            icon = wx.Icon(cwd+"/Photos/Error_Icon.png")
        else:
            icon = wx.Icon(cwd+"/_internal/Photos/Error_Icon.png")
        self.SetIcon(icon)
        self.SetSize(size)
        self.SetMinSize(size)
        self.SetMaxSize(size)
        self.panel = wx.Panel(self)
        textbox = wx.TextCtrl(parent=self.panel, id=-1, style=wx.ALIGN_LEFT|wx.TE_MULTILINE, size=(size[0]-30, size[1]-50), pos=(10,10))
        textbox.SetLabelText(text)
        textbox.SetEditable(False)
        font = wx.Font(12, wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        textbox.SetFont(font)

    def Update_Self_for_Settings(self, settings, load, size = (500, 500)):
        self.load = load
        self.settings = settings
        if os.path.exists(settings["cwd"]+"/Photos/Settings_Icon.png"):
            icon = wx.Icon(settings["cwd"]+"/Photos/Settings_Icon.png")
        else:
            icon = wx.Icon(settings["cwd"]+"/_internal/Photos/Settings_Icon.png")
        self.SetIcon(icon)
        self.SetSize(size); self.SetMinSize(size); self.SetMaxSize(size)
        self.panel = wx.Panel(self)

        sw = 200 #setting box width
        sh = 20 #setting box height
        slw = 300 #setting label box width
        slh = 20 #setting label box height
        
        #Graph_Visual_Settings
        self.l3_Graph_Visual_Settings = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_title = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_x_axis_title = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_y_axis_title = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_xmin = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_xmax = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_ymin = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_ymax = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_arrow_scale = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_starting_points = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_show_legend =wx.BoxSizer(wx.HORIZONTAL)

        #Graph_Background_Settings
        self.l3_Graph_Background_Settings = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_Graph_Background_Settings_blank = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_h = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_xdensity = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_ydensity = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_use_time = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_forward_steps = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_backward_steps = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_forward_time = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_backward_time = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_method = wx.BoxSizer(wx.HORIZONTAL)

        #Warning_Settings
        self.l3_Warning_Settings = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_Warning_Settings_blank = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_stop_all_warnings = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_stop_variable_override_warning = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_stop_termination_warning = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_stop_numerical_termination_warning = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_stop_improper_power_phase_plot_warning = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_stop_improper_power_plotted_lines_warning = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_stop_invalid_value_in_function_in_phase_plot_warning =wx.BoxSizer(wx.HORIZONTAL)
        self.l3_stop_invalid_value_in_function_in_plotted_lines_warning =wx.BoxSizer(wx.HORIZONTAL)
        self.l3_stop_overflow_in_phase_plot_warning =wx.BoxSizer(wx.HORIZONTAL)
        self.l3_stop_overflow_in_plotted_lines_warning =wx.BoxSizer(wx.HORIZONTAL)
        self.l3_stop_underflow_in_phase_plot_warning =wx.BoxSizer(wx.HORIZONTAL)
        self.l3_stop_underflow_in_plotted_lines_warning =wx.BoxSizer(wx.HORIZONTAL)

        #Files_Settings
        self.l3_Files_Settings = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_Files_Settings_blank = wx.BoxSizer(wx.HORIZONTAL)
        self.l3_settings_file = wx.BoxSizer(wx.HORIZONTAL)
        
        # self.l3_cwd = wx.BoxSizer(wx.HORIZONTAL)
        # cwd should not be editable by the user

        #This is a panel
        self.setting_scroller_panel = wx.lib.scrolledpanel.ScrolledPanel(self.panel,-1,size=(440,400), style=wx.SIMPLE_BORDER|wx.EXPAND)
        self.setting_scroller_panel.SetupScrolling(scroll_x=False, scroll_y=True)
        self.setting_scroller_panel.SetBackgroundColour('#FFFFFF')

        def display_settings(setting):
            setting_string = "" \
            "self."+setting+"_panel_1 = wx.Panel(self.setting_scroller_panel)\n" \
            "wx.StaticText(parent=self."+setting+"_panel_1, id=-1, label=\""+setting+": \", style=wx.ALIGN_LEFT, size=(slw, slh), pos=(10,5))\n" \
            "#\n" \
            "self."+setting+"_panel_2 = wx.Panel(self.setting_scroller_panel)\n" \
            "self."+setting+"_setting_box = wx.TextCtrl(self."+setting+"_panel_2, -1, style=wx.ALIGN_LEFT|wx.EXPAND, size = (sw, sh), pos=(0,5))\n" \
            "self."+setting+"_setting_box.SetValue(str(self.settings[\""+setting+"\"]))\n" \
            "#\n" \
            "self.l3_"+setting+".Add(self."+setting+"_panel_1, proportion=3)\n" \
            "self.l3_"+setting+".Add(self."+setting+"_panel_2, proportion=2)\n"

            return(setting_string)

        def display_setting_head(setting):
            setting_string = "" \
            "self."+setting+"_panel_1 = wx.Panel(self.setting_scroller_panel)\n" \
            "wx.StaticText(parent=self."+setting+"_panel_1, id=-1, label=\""+setting+": \", style=wx.ALIGN_LEFT, size=(slw, slh), pos=(10,5))\n" \
            "#\n" \
            "self.l3_"+setting+".Add(self."+setting+"_panel_1, proportion=6)"
            return(setting_string)
        
        def display_setting_blank(setting):
            setting_string = "" \
            "self."+setting+"_blank_panel_1 = wx.Panel(self.setting_scroller_panel)\n" \
            "wx.StaticText(parent=self."+setting+"_blank_panel_1, id=-1, label=\" \", style=wx.ALIGN_LEFT, size=(slw, slh), pos=(10,5))\n" \
            "#\n" \
            "self.l3_"+setting+"_blank.Add(self."+setting+"_blank_panel_1, proportion=6)"
            return(setting_string)

        for key in self.settings.keys():
            if(key != "cwd" and key != "Graph_Visual_Settings" and key != "Graph_Background_Settings" and key != "Warning_Settings" and key != "Files_Settings"): # cwd should not be edited by the user
                setting_display_string = display_settings(key)
                exec(setting_display_string)
            elif(key == "Graph_Visual_Settings" or key == "Graph_Background_Settings" or key == "Warning_Settings" or key == "Files_Settings"):
                if(key!="Graph_Visual_Settings"):
                    setting_display_string = display_setting_blank(key)
                    exec(setting_display_string)
                setting_display_string = display_setting_head(key)
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
                if(key == "Graph_Background_Settings" or key == "Warning_Settings" or key == "Files_Settings"):
                    exec('self.l2_2.Add(self.l3_'+key+'_blank, proportion=1, flag=wx.EXPAND)')
                exec('self.l2_2.Add(self.l3_'+key+', proportion=1, flag=wx.EXPAND)')
        
        self.setting_scroller_panel.SetSizer(self.l2_2)

        self.l1.Add(self.l2_1, proportion=1, flag=wx.EXPAND)
        self.l1.Add(self.setting_scroller_panel, proportion=15, flag=wx.EXPAND)

        self.panel.SetSizer(self.l1)
        self.Layout()

    def apply_settings_button_pushed(self, sig=None):      
        self.settings["Graph_Visual_Settings"]= ""
        self.settings["title"] = self.title_setting_box.GetValue()
        self.settings["x_axis_title"] = self.x_axis_title_setting_box.GetValue()
        self.settings["y_axis_title"] = self.y_axis_title_setting_box.GetValue()
        self.settings["xmin"] = float(self.xmin_setting_box.GetValue())
        self.settings["xmax"] = float(self.xmax_setting_box.GetValue())
        self.settings["ymin"] = float(self.ymin_setting_box.GetValue())
        self.settings["ymax"] = float(self.ymax_setting_box.GetValue())
        self.settings["arrow_scale"] = float(self.arrow_scale_setting_box.GetValue())
        self.settings["starting_points"] = eval(self.starting_points_setting_box.GetValue())
        self.settings["show_legend"] = eval(self.show_legend_setting_box.GetValue())


        self.settings["Graph_Background_Settings"]= ""
        self.settings["h"] = float(self.h_setting_box.GetValue())
        self.settings["xdensity"] = float(self.xdensity_setting_box.GetValue())
        self.settings["ydensity"] = float(self.ydensity_setting_box.GetValue())
        self.settings["use_time"] = True if (self.use_time_setting_box.GetValue() == "True") else False
        if(self.settings["use_time"]==False):
            self.settings["forward_steps"] = int(self.forward_steps_setting_box.GetValue())
            self.settings["backward_steps"] = int(self.backward_steps_setting_box.GetValue())
            forward_time = self.settings["forward_steps"]*self.settings["h"]
            backward_time = self.settings["backward_steps"]*self.settings["h"]
            self.settings["forward_time"] = forward_time
            self.settings["backward_time"] = backward_time
            self.forward_time_setting_box.SetValue(str(self.settings["forward_time"]))
            self.backward_time_setting_box.SetValue(str(self.settings["backward_time"]))
        else:
            self.settings["forward_time"] = float(self.forward_time_setting_box.GetValue())
            self.settings["backward_time"] = float(self.backward_time_setting_box.GetValue())
            forward_steps = round(self.settings["forward_time"]/self.settings["h"])
            backward_steps = round(self.settings["backward_time"]/self.settings["h"])
            self.settings["forward_steps"]= forward_steps
            self.settings["backward_steps"]= backward_steps
            self.forward_steps_setting_box.SetValue(str(self.settings["forward_steps"]))
            self.backward_steps_setting_box.SetValue(str(self.settings["backward_steps"]))
        self.settings["method"] = self.method_setting_box.GetValue()

        self.settings["Warning_Settings"]= ""
        self.settings["stop_all_warnings"] = True if (self.stop_all_warnings_setting_box.GetValue() == "True") else False
        if(self.settings["stop_all_warnings"]==True):
            self.settings["stop_variable_override_warning"] = True
            self.settings["stop_termination_warning"] = True
            self.settings["stop_numerical_termination_warning"] = True
            self.settings["stop_improper_power_phase_plot_warning"] = True
            self.settings["stop_improper_power_plotted_lines_warning"] = True
            self.settings["stop_invalid_value_in_function_in_phase_plot_warning"] = True
            self.settings["stop_invalid_value_in_function_in_plotted_lines_warning"] = True
            self.settings["stop_overflow_in_phase_plot_warning"] = True
            self.settings["stop_overflow_in_plotted_lines_warning"] = True
            self.settings["stop_underflow_in_phase_plot_warning"] = True
            self.settings["stop_underflow_in_plotted_lines_warning"] = True
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
        else:
            self.settings["stop_variable_override_warning"] = True if (self.stop_variable_override_warning_setting_box.GetValue()  == "True") else False
            self.settings["stop_termination_warning"] = True if (self.stop_termination_warning_setting_box.GetValue()  == "True") else False
            self.settings["stop_numerical_termination_warning"] = True if (self.stop_numerical_termination_warning_setting_box.GetValue()  == "True") else False
            self.settings["stop_improper_power_phase_plot_warning"] = True if (self.stop_improper_power_phase_plot_warning_setting_box.GetValue()  == "True") else False
            self.settings["stop_improper_power_plotted_lines_warning"] = True if (self.stop_improper_power_plotted_lines_warning_setting_box.GetValue()  == "True") else False
            self.settings["stop_invalid_value_in_function_in_phase_plot_warning"] = True if (self.stop_invalid_value_in_function_in_phase_plot_warning_setting_box.GetValue()  == "True") else False
            self.settings["stop_invalid_value_in_function_in_plotted_lines_warning"] = True if (self.stop_invalid_value_in_function_in_plotted_lines_warning_setting_box.GetValue()  == "True") else False
            self.settings["stop_overflow_in_phase_plot_warning"] = True if (self.stop_overflow_in_phase_plot_warning_setting_box.GetValue()  == "True") else False
            self.settings["stop_overflow_in_plotted_lines_warning"] = True if (self.stop_overflow_in_plotted_lines_warning_setting_box.GetValue()  == "True") else False
            self.settings["stop_underflow_in_phase_plot_warning"] = True if (self.stop_underflow_in_phase_plot_warning_setting_box.GetValue()  == "True") else False
            self.settings["stop_underflow_in_plotted_lines_warning"] = True if (self.stop_underflow_in_plotted_lines_warning_setting_box.GetValue()  == "True") else False

        self.settings["Files_Settings"]= ""
        self.settings["settings_file"] = self.settings_file_setting_box.GetValue()
        
        if(self.settings["settings_file"][0]!="/" and self.settings["settings_file"][0:1]!="\\"):
            self.settings["settings_file"] = "/"+self.settings["settings_file"]
        elif(self.settings["settings_file"][0:1]=="\\"):#windows allows \\ and / in path names, Linux allows /, this prevents user errors
            self.settings["settings_file"] = "/"+self.settings["settings_file"][1:]
        # self.settings["cwd"] = self.cwd_setting_box.GetValue()
        # cwd should not be edited
        self.load(from_settings=True)

    def save_settings_button_pushed(self, sig):
        self.apply_settings_button_pushed()
        if(self.settings["settings_file"]==""):
            cwd = self.settings["cwd"]
            variable_override_warning = popup_window(self).Error("Error: settings_file is unspecified so unfortunatly I don't know where to get settings", cwd=cwd)
            variable_override_warning.Show()
        elif(self.settings["settings_file"][0]!="/" and self.settings["settings_file"][0:1]!="\\"):
            self.settings["settings_file"] = "/"+self.settings["settings_file"]
        elif(self.settings["settings_file"][0:1]=="\\"):#windows allows \\ and / in path names, Linux allows /, this prevents user errors
            self.settings["settings_file"] = "/"+self.settings["settings_file"][1:]
        if not os.path.exists(self.settings["cwd"]+"/".join(self.settings["settings_file"].split("/")[:-1])):
            # "/".join(self.settings["settings_file"].split("/")[:-1]) 
            # self.settings["settings_file"] = custome settings file
            # .split("/") = makes list sperarating all different directories in custome settings file
            # [:-1] take all but the actual file name
            # "/".join put everything back together again with "/" between every item in the list
            cwd = self.settings["cwd"]
            settings_error = popup_window(self).Error("Error: settings file specified "+ self.settings["settings_file"] + " is missing so I don't know where to go", cwd=cwd)
            settings_error.Show()
        else:
            try:
                with open(self.settings["cwd"]+self.settings["settings_file"], "w") as f:
                    f.write(json.dumps(self.settings))
            except:
                settings_error = popup_window(self).Error("Error: settings not save propperly", cwd=cwd)
                settings_error.Show()

            if not os.path.exists(self.settings["cwd"]+'/settings.json'):
                default_class_instance = Default()
                settings = default_class_instance.settings
                settings["settings_file"] = self.settings["settings_file"]

                with open(self.settings["cwd"]+'/settings.json', "w") as f:
                    f.write(json.dumps(settings))
            else:
                with open(self.settings["cwd"]+'/settings.json', "r") as json_file:
                    temp_settings = json.load(json_file)
                temp_settings["settings_file"] = self.settings["settings_file"]
                with open(self.settings["cwd"]+'/settings.json', "w") as f:
                    f.write(json.dumps(temp_settings))

    def reset_settings_button_pushed(self, sig=None):
        #Wrong Self
        if(self.settings["settings_file"][0]!="/" and self.settings["settings_file"][0:1]!="\\"):
            self.settings["settings_file"] = "/"+self.settings["settings_file"]
        elif(self.settings["settings_file"][0:1]=="\\"):#windows allows \\ and / in path names, Linux allows /, this prevents user errors
            self.settings["settings_file"] = "/"+self.settings["settings_file"][1:]
        if(self.settings["settings_file"]==""):
            cwd = self.settings["cwd"]
            variable_override_warning = popup_window(self).Error("Error: settings_file is unspecified so unfortunatly I don't know where to get settings", cwd=cwd)
            variable_override_warning.Show()
        elif not os.path.exists(self.settings["cwd"]+self.settings["settings_file"]):
            cwd = self.settings["cwd"]
            variable_override_warning = popup_window(self).Error("Error: settings file specified "+ self.settings["settings_file"][1:] + " is missing so I don't know where to go", cwd=cwd)
            variable_override_warning.Show()
        else:
            #NOTE: DO NOT USE "self.settings = json.load(json_file)", it will make it so things do not work properly 
            with open(self.settings["cwd"]+self.settings["settings_file"], "r") as json_file:
                temp_settings = json.load(json_file)
            for key in self.settings.keys():
                self.settings[key] = temp_settings[key]

            # Graph_Visual:
            self.title_setting_box.SetValue(str(self.settings["title"]))
            self.x_axis_title_setting_box.SetValue(str(self.settings["x_axis_title"]))
            self.x_axis_title_setting_box.SetValue(str(self.settings["y_axis_title"]))
            self.xmin_setting_box.SetValue(str(self.settings["xmin"]))
            self.xmax_setting_box.SetValue(str(self.settings["xmax"]))
            self.ymin_setting_box.SetValue(str(self.settings["ymin"]))
            self.ymax_setting_box.SetValue(str(self.settings["ymax"]))
            self.arrow_scale_setting_box.SetValue(str(self.settings["arrow_scale"]))
            self.starting_points_setting_box.SetValue(str(self.settings["starting_points"]))
            self.show_legend_setting_box.SetValue(str(self.settings["show_legend"]))

            # Graph_Background:
            self.h_setting_box.SetValue(str(self.settings["h"]))
            self.xdensity_setting_box.SetValue(str(self.settings["xdensity"]))
            self.ydensity_setting_box.SetValue(str(self.settings["ydensity"]))
            self.use_time_setting_box.SetValue(str(self.settings["use_time"]))
            if(self.settings["use_time"]==False):
                self.forward_steps_setting_box.SetValue(str(self.settings["forward_steps"]))
                self.backward_steps_setting_box.SetValue(str(self.settings["backward_steps"]))

                forward_time = self.settings["forward_steps"]*self.settings["h"]
                backward_time = self.settings["backward_steps"]*self.settings["h"]
                self.settings["forward_time"] = forward_time
                self.settings["backward_time"] = backward_time

                self.forward_time_setting_box.SetValue(str(self.settings["forward_time"]))
                self.backward_time_setting_box.SetValue(str(self.settings["backward_time"]))
            else:
                self.forward_time_setting_box.SetValue(str(self.settings["forward_time"]))
                self.backward_time_setting_box.SetValue(str(self.settings["backward_time"]))
                
                forward_steps = round(self.settings["forward_time"]/self.settings["h"])
                backward_steps = round(self.settings["backward_time"]/self.settings["h"])
                self.settings["forward_steps"]= forward_steps
                self.settings["backward_steps"]= backward_steps

                self.forward_steps_setting_box.SetValue(str(self.settings["forward_steps"]))
                self.backward_steps_setting_box.SetValue(str(self.settings["backward_steps"]))
            self.method_setting_box.SetValue(str(self.settings["method"]))

            #Warnings:
            self.stop_all_warnings_setting_box.SetValue(str(self.settings["stop_all_warnings"]))
            if(self.settings["stop_all_warnings"]==True):
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
            else:
                self.stop_variable_override_warning_setting_box.SetValue(str(self.settings["stop_variable_override_warning"]))
                self.stop_termination_warning_setting_box.SetValue(str(self.settings["stop_termination_warning"]))
                self.stop_numerical_termination_warning_setting_box.SetValue(str(self.settings["stop_numerical_termination_warning"]))
                self.stop_improper_power_phase_plot_warning_setting_box.SetValue(str(self.settings["stop_improper_power_phase_plot_warning"]))
                self.stop_improper_power_plotted_lines_warning_setting_box.SetValue(str(self.settings["stop_improper_power_plotted_lines_warning"]))
                self.stop_invalid_value_in_function_in_phase_plot_warning_setting_box.SetValue(str(self.settings["stop_invalid_value_in_function_in_phase_plot_warning"]))
                self.stop_invalid_value_in_function_in_plotted_lines_warning_setting_box.SetValue(str(self.settings["stop_invalid_value_in_function_in_plotted_lines_warning"]))
                self.stop_overflow_in_phase_plot_warning_setting_box.SetValue(str(self.settings["stop_overflow_in_phase_plot_warning"]))
                self.stop_overflow_in_plotted_lines_warning_setting_box.SetValue(str(self.settings["stop_overflow_in_plotted_lines_warning"]))
                self.stop_underflow_in_phase_plot_warning_setting_box.SetValue(str(self.settings["stop_underflow_in_phase_plot_warning"]))
                self.stop_underflow_in_plotted_lines_warning_setting_box.SetValue(str(self.settings["stop_underflow_in_plotted_lines_warning"]))

            #Files:
            self.settings_file_setting_box.SetValue(str(self.settings["settings_file"]))
            # self.cwd_setting_box.SetValue(str(self.settings["cwd"]))
            # cwd should not be edited
            self.load(from_settings=True)


    def default_settings_button_pushed(self, s):
        default_class_instance = Default()
        
        # have to set settings individually or else pointer will just move, could also have used for loop or other method,
        # but this is what I went with

        self.settings["Graph_Visual_Settings"]= default_class_instance.settings["Graph_Visual_Settings:"]
        self.settings["title"] = default_class_instance.settings["title"]
        self.settings["x_axis_title"] = default_class_instance.settings["x_axis_title"]
        self.settings["y_axis_title"] = default_class_instance.settings["y_axis_title"]
        self.settings["xmin"] = default_class_instance.settings["xmin"]
        self.settings["xmax"] = default_class_instance.settings["xmax"]
        self.settings["ymin"] = default_class_instance.settings["ymin"]
        self.settings["ymax"] = default_class_instance.settings["ymax"]
        self.settings["arrow_scale"] = default_class_instance.settings["arrow_scale"]
        self.settings["starting_points"] = default_class_instance.settings["starting_points"]
        self.settings["show_legend"] = default_class_instance.settings["show_legend"]

        self.settings["Graph_Background_Settings"]= default_class_instance.settings["Graph_Background_Settings"]
        self.settings["h"] = default_class_instance.settings["h"]
        self.settings["xdensity"] = default_class_instance.settings["xdensity"]
        self.settings["ydensity"] = default_class_instance.settings["ydensity"]
        self.settings["use_time"] = default_class_instance.settings["use_time"] # No if statement needed since the Default setting have no contradiction
        self.settings["forward_steps"] = default_class_instance.settings["forward_steps"]
        self.settings["backward_steps"] = default_class_instance.settings["backward_steps"]
        self.settings["method"] = default_class_instance.settings["method"]

        self.settings["Warning_Settings"]= default_class_instance.settings["Warning_Settings"] # No if statement needed for the same reason
        self.settings["stop_all_warnings"] = default_class_instance.settings["stop_all_warnings"]
        self.settings["stop_variable_override_warning"] = default_class_instance.settings["stop_variable_override_warning"]
        self.settings["stop_termination_warning"] = default_class_instance.settings["stop_termination_warning"]
        self.settings["stop_numerical_termination_warning"] = default_class_instance.settings["stop_numerical_termination_warning"]
        self.settings["stop_improper_power_phase_plot_warning"] = default_class_instance.settings["stop_improper_power_phase_plot_warning"]
        self.settings["stop_improper_power_plotted_lines_warning"] = default_class_instance.settings["stop_improper_power_plotted_lines_warning"]
        self.settings["stop_invalid_value_in_function_in_phase_plot_warning"] = default_class_instance.settings["stop_invalid_value_in_function_in_phase_plot_warning"]
        self.settings["stop_invalid_value_in_function_in_plotted_lines_warning"] = default_class_instance.settings["stop_invalid_value_in_function_in_plotted_lines_warning"]
        self.settings["stop_overflow_in_phase_plot_warning"] = default_class_instance.settings["stop_overflow_in_phase_plot_warning"]
        self.settings["stop_overflow_in_plotted_lines_warning"] = default_class_instance.settings["stop_overflow_in_plotted_lines_warning"]
        self.settings["stop_underflow_in_phase_plot_warning"] = default_class_instance.settings["stop_underflow_in_phase_plot_warning"]
        self.settings["stop_underflow_in_plotted_lines_warning"] = default_class_instance.settings["stop_underflow_in_plotted_lines_warning"]

        self.settings["Files_Settings"]= default_class_instance.settings["Files_Settings"]
        self.settings["settings_file"] = default_class_instance.settings["settings_file"]
        #self.settings["cwd"] = default_class_instance.settings["cwd"]
        #cwd should not be edited

        # Graph_Visual:
        self.title_setting_box.SetValue(str(self.settings["title"]))
        self.x_axis_title_setting_box.SetValue(str(self.settings["x_axis_title"]))
        self.x_axis_title_setting_box.SetValue(str(self.settings["y_axis_title"]))
        self.xmin_setting_box.SetValue(str(self.settings["xmin"]))
        self.xmax_setting_box.SetValue(str(self.settings["xmax"]))
        self.ymin_setting_box.SetValue(str(self.settings["ymin"]))
        self.ymax_setting_box.SetValue(str(self.settings["ymax"]))

        # Graph_Background:
        self.arrow_scale_setting_box.SetValue(str(self.settings["arrow_scale"]))
        self.starting_points_setting_box.SetValue(str(self.settings["starting_points"]))
        self.show_legend_setting_box.SetValue(str(self.settings["show_legend"]))
        self.h_setting_box.SetValue(str(self.settings["h"]))
        self.xdensity_setting_box.SetValue(str(self.settings["xdensity"]))
        self.ydensity_setting_box.SetValue(str(self.settings["ydensity"]))
        self.use_time_setting_box.SetValue(str(self.settings["use_time"]))
        self.forward_steps_setting_box.SetValue(int(self.settings["forward_steps"]))
        self.backward_steps_setting_box.SetValue(int(self.settings["backward_steps"]))
        self.forward_time_setting_box.SetValue(float(self.settings["forward_time"]))
        self.backward_time_setting_box.SetValue(float(self.settings["backward_time"]))
        self.method_setting_box.SetValue(str(self.settings["method"]))

        #Warnings:
        self.stop_all_warnings_setting_box.SetValue(str(self.settings["stop_all_warnings"]))
        self.stop_variable_override_warning_setting_box.SetValue(str(self.settings["stop_variable_override_warning"]))
        self.stop_termination_warning_setting_box.SetValue(str(self.settings["stop_termination_warning"]))
        self.stop_numerical_termination_warning_setting_box.SetValue(str(self.settings["stop_numerical_termination_warning"]))
        self.stop_improper_power_phase_plot_warning_setting_box.SetValue(str(self.settings["stop_improper_power_phase_plot_warning"]))
        self.stop_improper_power_plotted_lines_warning_setting_box.SetValue(str(self.settings["stop_improper_power_plotted_lines_warning"]))
        self.stop_invalid_value_in_function_in_phase_plot_warning_setting_box.SetValue(str(self.settings["stop_invalid_value_in_function_in_phase_plot_warning"]))
        self.stop_invalid_value_in_function_in_plotted_lines_warning_setting_box.SetValue(str(self.settings["stop_invalid_value_in_function_in_plotted_lines_warning"]))
        self.stop_overflow_in_phase_plot_warning_setting_box.SetValue(str(self.settings["stop_overflow_in_phase_plot_warning"]))
        self.stop_overflow_in_plotted_lines_warning_setting_box.SetValue(str(self.settings["stop_overflow_in_plotted_lines_warning"]))
        self.stop_underflow_in_phase_plot_warning_setting_box.SetValue(str(self.settings["stop_underflow_in_phase_plot_warning"]))
        self.stop_underflow_in_plotted_lines_warning_setting_box.SetValue(str(self.settings["stop_underflow_in_plotted_lines_warning"]))

        #Files:
        self.settings_file_setting_box.SetValue(str(self.settings["settings_file"]))
        
        #self.cwd_setting_box.SetValue(str(self.settings["cwd"]))
        #cwd should not be edited
        self.apply_settings_button_pushed()

        # just need to make sure this is sent back properly


    def File(self, text="", size = (250, 150), cwd=""):
        if os.path.exists(cwd+"/Photos/File_Icon.png"):
            icon = wx.Icon(cwd+"/Photos/File_Icon.png")
        else:
            icon = wx.Icon(cwd+"/_internal/Photos/File_Icon.png")
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
