import plotly.graph_objects as go
import numpy as np
import popup_windows
from numpy import sin, cos, tan, arcsin, arccos, arctan, sinh, cosh, tanh, log, log10, log2, e, pi
from warnings import catch_warnings
π = pi
ln = lambda x: log(x)
def check_warnings_plotted_lines(main_frame, settings, w):
    # dx/dt = (cos(3**x^y))(x)+log(x) and dydt=(y) is a good test system 
    for warning in w:
        if(warning.message.args[0][:23]=="invalid escape sequence"):
            pass # this warning can be caused by certian file locations being used
        elif(warning.message.args[0]=="divide by zero encountered in scalar divide"):
            Zero_Error = popup_windows.popup_window(main_frame)
            Zero_Error.Error("Error, had to divide by zero somewhere when ploting lines from initial points. Program may have been able to proceed, but there may be large numarical errors.", cwd=settings["cwd"])
            Zero_Error.Show()
        elif(warning.message.args[0]=="invalid value encountered in scalar power"):
            if(settings["stop_improper_power_phase_plot_warning"]==False):
                improper_power_in_phase_plot_warning = popup_windows.popup_window(main_frame)
                improper_power_in_phase_plot_warning.Warning("Warning: When ploting lines from initial points there was an invalid value encountered in scalar power (e.g. (-2)^(0.5) does not exist). This may be fixed by making h smaller", cwd=settings["cwd"])
                improper_power_in_phase_plot_warning.Show()
        elif(warning.message.args[0][:28]=="invalid value encountered in"):
            #if(settings["stop_invalid_value_in_function_in_phase_plot_warning"]==False):
                invalid_value_in_function_in_phase_plot_warning = popup_windows.popup_window(main_frame)
                invalid_value_in_function_in_phase_plot_warning.Warning("Warning: When ploting lines from initial points an invalid value was entered into the function" + warning.message.args[0][28:] + " (for example cos(inf), arccos(2), etc). This may be fixed by making h smaller", cwd=settings["cwd"])
                invalid_value_in_function_in_phase_plot_warning.Show()
        elif(warning.message.args[0][:8]=="overflow"):
            #if(settings["stop_overflow_in_phase_plot_warning"]==False):
                overflow_in_phase_plot_warning = popup_windows.popup_window(main_frame)
                overflow_in_phase_plot_warning.Warning("Warning: When ploting lines from initial points there was an overflow warning, this can be caused by a really large number or a small number being added to a small number", cwd=settings["cwd"])
                overflow_in_phase_plot_warning.Show()
        elif(warning.message.args[0][:9]=="underflow"):
            #if(settings["stop_underflow_in_phase_plot_warning"]==False):
                overflow_in_phase_plot_warning = popup_windows.popup_window(main_frame)
                overflow_in_phase_plot_warning.Warning("Warning: When ploting lines from initial points there was an underflow warning, this can be caused by numbers that are too small", cwd=settings["cwd"])
                overflow_in_phase_plot_warning.Show()
        elif(warning): #cannot simply raise excpetion or some issues may be missed
            Unknown_Error = popup_windows.popup_window(main_frame)
            Unknown_Error.Warning("Warning, "+warning.message.args[0]+"\nNOTE: I have not seen this message during testing. Please email samuelcstreet@gmail.com with details about what you are trying to do and I will add a new warning setting to shut this warning off if you would like, otherwise this message cannot be silenced", cwd=settings["cwd"])
            Unknown_Error.Show()

def get_points_for_forward_trace_Eurler(start, forward_steps, h, dxdt, dydt, main_frame, xmin, xmax, ymin, ymax, xpad, ypad, settings):
    x_points_forwards = [start[0]]
    y_points_forwards = [start[1]]
    with catch_warnings(record=True) as w:
        for i in range(forward_steps):
            stop = False
            prev_x = x_points_forwards[-1]
            prev_y = y_points_forwards[-1]
            try: # adds lots of time to figuring out the graph
                next_x = prev_x + h*dxdt(prev_x, prev_y)
                next_y = prev_y + h*dydt(prev_x, prev_y)
            except OverflowError as ex:
                print("")
                if(settings["stop_numerical_termination_warning"]==False):
                    termination_warning  = popup_windows.popup_window(main_frame)
                    termination_warning.Warning("WARNING, process haulted due to numerical error\nwhen going forwards in time.", cwd=settings["cwd"])
                    termination_warning.Show()
                    check_warnings_plotted_lines(main_frame, settings, w)
                return x_points_forwards, y_points_forwards
            except ZeroDivisionError as ex:
                Zero_Error = popup_windows.popup_window(main_frame)
                Zero_Error.Error("Error, had to divide by zero somewhere when plotting forward curve(s). Program may have been able to proceed, but note there may be large numarical errors when making a curve in your plot.", cwd=settings["cwd"])
                Zero_Error.Show()
                return x_points_forwards, y_points_forwards
            except Exception as ex:
                Zero_Error = popup_windows.popup_window(main_frame)
                Zero_Error.Error("Error, somewhere when plotting your forward curve(s). I do not know what is wrong. feel free to read out at samuelcstreet@gmail.com and I can try and help you", cwd=settings["cwd"])
                Zero_Error.Show()
                return x_points_forwards, y_points_forwards
        
            x_points_forwards.append(next_x)
            y_points_forwards.append(next_y)
            if(next_x>xmax+xpad or next_x<xmin-xpad):
                stop = True
                if(stop == True):
                    if(settings["stop_termination_warning"]==False):
                        termination_warning  = popup_windows.popup_window(main_frame)
                        termination_warning.Warning("WARNING, Terminated on step " + str(i+1)+ "\nwhen going forwards in time.", cwd=settings["cwd"])
                        termination_warning.Show()
                        check_warnings_plotted_lines(main_frame, settings, w)
                    return x_points_forwards, y_points_forwards
                    # if it can be done without error then proceed 1 step farthure than the boundry of the chosen region
            if(next_y>ymax+ypad or next_y<ymin-ypad):
                stop = True
                if(stop == True):
                    if(settings["stop_termination_warning"]==False):
                        termination_warning = popup_windows.popup_window(main_frame)
                        termination_warning.Warning("WARNING, Terminated on step " + str(i+1)+ "\nwhen going forwards in time.", cwd=settings["cwd"])
                        termination_warning.Show()
                        check_warnings_plotted_lines(main_frame, settings, w)
                    return x_points_forwards, y_points_forwards
                    # if it can be done without error then proceed 1 step farthure than the boundry of the chosen region
    check_warnings_plotted_lines(main_frame, settings, w)
    return x_points_forwards, y_points_forwards

def get_points_for_backwards_trace_Eurler(start, backward_steps, h, dxdt, dydt, main_frame, xmin, xmax, ymin, ymax, xpad, ypad, settings):
    x_points_backwards = [start[0]]
    y_points_backwards = [start[1]]
    with catch_warnings(record=True) as w:
        for i in range(backward_steps):
            stop = False
            prev_x = x_points_backwards[-1]
            prev_y = y_points_backwards[-1]
            try: # adds lots of time to figuring out the graph
                next_x = prev_x - h*dxdt(prev_x, prev_y)
                next_y = prev_y - h*dydt(prev_x, prev_y)
            except OverflowError as ex:
                print("")
                if(settings["stop_numerical_termination_warning"]==False):
                    termination_warning  = popup_windows.popup_window(main_frame)
                    termination_warning.Warning("WARNING, process haulted due to numerical error\nwhen going backwards in time.", cwd=settings["cwd"])
                    termination_warning.Show()
                check_warnings_plotted_lines(main_frame, settings, w)
                return x_points_backwards, y_points_backwards
            except ZeroDivisionError as ex:
                Zero_Error = popup_windows.popup_window(main_frame)
                Zero_Error.Error("Error, had to divide by zero somewhere when plotting curve(s) going backward in time. Program may have been able to proceed, but note there may be large numarical errors when making a curve in your plot.", cwd=settings["cwd"])
                Zero_Error.Show()
                return x_points_backwards, y_points_backwards
            except Exception as ex:
                Zero_Error = popup_windows.popup_window(main_frame)
                Zero_Error.Error("Error, somewhere when plotting curve(s) going backward in time. I do not know what is wrong. feel free to read out at samuelcstreet@gmail.com and I can try and help you", cwd=settings["cwd"])
                Zero_Error.Show()
                return x_points_backwards, y_points_backwards
                
            x_points_backwards.append(next_x)
            y_points_backwards.append(next_y)
            if(next_x>xmax+xpad or next_x<xmin-xpad):
                stop = True
                if(stop == True):
                    if(settings["stop_termination_warning"]==False):
                        termination_warning  = popup_windows.popup_window(main_frame)
                        termination_warning.Warning("WARNING, Terminated on step " + str(i+1)+"\nwhen going backwards in time.", cwd=settings["cwd"])
                        termination_warning.Show()
                    check_warnings_plotted_lines(main_frame, settings, w)
                    return x_points_backwards, y_points_backwards
                    # if it can be done without error then proceed 1 step farthure than the boundry of the chosen region
            if(next_y>ymax+ypad or next_y<ymin-ypad):
                stop = True
                if(stop == True):
                    if(settings["stop_termination_warning"]==False):
                        termination_warning = popup_windows.popup_window(main_frame)
                        termination_warning.Warning("WARNING, Terminated on step " + str(i+1)+"\nwhen going backwards in time.", cwd=settings["cwd"])
                        termination_warning.Show()
                    check_warnings_plotted_lines(main_frame, settings, w)
                    return x_points_backwards, y_points_backwards
                    # if it can be done without error then proceed 1 step farthure than the boundry of the chosen region
    check_warnings_plotted_lines(main_frame, settings, w)
    return x_points_backwards, y_points_backwards

#File for making the phase plot
def make_figure(main_frame, dxdt_text, dydt_text, settings, variables_text, from_settings=False):    
    try:
        exec(variables_text.strip())
    except:
        variable_error_window = popup_windows.popup_window(main_frame)
        variable_error_window.Error("ERROR, please check over your variables", cwd=settings["cwd"])
        variable_error_window.Show()
    
    try:
        dxdt = eval(dxdt_text)
    except:
        dxdt_error_window = popup_windows.popup_window(main_frame)
        dxdt_error_window.Error("ERROR, I think there might be something wrong with your dx/dt statement, are all your variables defined?", cwd=settings["cwd"])
        dxdt_error_window.Show()
    
    try:
        dydt = eval(dydt_text)
    except:
        dydt_error_window = popup_windows.popup_window(main_frame)
        dydt_error_window.Error("ERROR, I think there might be something wrong with your dy/dt statement, are all your variables defined?", cwd=settings["cwd"])
        dydt_error_window.Show()

    starting_points = settings["starting_points"]
    xdensity = settings["xdensity"]
    ydensity = settings["ydensity"]
    h = settings["h"]
    forward_steps = settings["forward_steps"]
    backward_steps = settings["backward_steps"]
    method = settings["method"]
    arrow_scale = settings["arrow_scale"]

    #### Setup
    fig = go.Figure()
    xmin = settings["xmin"]
    xmax = settings["xmax"]
    ymin = settings["ymin"]
    ymax = settings["ymax"]
    
    if main_frame != None:
        main_frame.display.display.SetSize(main_frame.display.GetSize())
        fig.update_layout(
            width = main_frame.display.display.GetSize().Width-20,
            height = main_frame.display.display.GetSize().Height-20,
        )
    else: #This is used if making an image manually for initial plot 
        #(if making initial image comment out everything below this else statement)
        fig.update_layout(
            width = 629-20,
            height = 385-20,

        )
        xpad = (xmax-xmin)/20
        ypad = (ymax-ymin)/20
        fig.update_layout(xaxis=dict(range=[xmin-xpad,xmax+xpad]))
        fig.update_layout(yaxis=dict(range=[ymin-ypad,ymax+ypad]))
        fig.update_layout(
        title=dict(
            text= settings["title"]
        ),
        xaxis=dict(
            title=dict(
                text=settings["x_axis_title"]
            )
        ),
        yaxis=dict(
            title=dict(
                text=settings["y_axis_title"]
            )
        )
        )
        fig.write_html(settings["cwd"]+"/Graphs/Display_Plot_Clear.html")

    #### phase plot
    if(from_settings==False or (dxdt_text.strip() !='lambda x, y: ()' and dydt_text.strip() !='lambda x, y: ()')):
        if(xdensity !=0 and ydensity !=0):
            xdif = (xmax-xmin)/(xdensity+1)
            xbases = np.arange(xmin+xdif, xmax, xdif)
            ydif = (ymax-ymin)/(ydensity+1)
            ybases = np.arange(ymin+ydif, ymax, ydif)
            try:
                with catch_warnings(record=True) as w:
                    for x_temp in (xbases):
                        for y_temp in (ybases):
                            fig.add_trace(
                                go.Scatter(
                                    visible = True,
                                    marker = dict(size=4,symbol= "arrow-bar-up", angleref="previous"),
                                    line=dict(color="#000000", width=1),
                                    
                                    #NOTE: May get a dividing by zero warning here which will not effect the program, but of course dividing by zero may result in inacuracy of the phase plot
                                    x=[x_temp, x_temp + dxdt(x_temp, y_temp)*xdif*arrow_scale],
                                    y=[y_temp, y_temp + dydt(x_temp, y_temp)*xdif*arrow_scale],
                                    showlegend=False))
                    for warning in w:
                        if(warning.message.args[0][:23]=="invalid escape sequence"):
                            pass # this warning can be caused by certian file locations being used
                        elif(warning.message.args[0]=="divide by zero encountered in scalar divide"):
                            Zero_Error = popup_windows.popup_window(main_frame)
                            Zero_Error.Error("Error, had to divide by zero somewhere when making phase plot. Program may have been able to proceed, but note there may be large numarical errors when making the small arrows for the phase plot.", cwd=settings["cwd"])
                            Zero_Error.Show()
                        elif(warning.message.args[0]=="invalid value encountered in scalar power"):
                            if(settings["stop_improper_power_phase_plot_warning"]==False):
                                improper_power_in_phase_plot_warning = popup_windows.popup_window(main_frame)
                                improper_power_in_phase_plot_warning.Warning("Warning: In the phase plot there were some points that had an issue showing due to an invalid value encountered in scalar power (e.g. (-2)^(0.5) does not exist). (Can likely ignore this warning)", cwd=settings["cwd"])
                                improper_power_in_phase_plot_warning.Show()
                        elif(warning.message.args[0][:28]=="invalid value encountered in"):
                            if(settings["stop_invalid_value_in_function_in_phase_plot_warning"]==False):
                                invalid_value_in_function_in_phase_plot_warning = popup_windows.popup_window(main_frame)
                                invalid_value_in_function_in_phase_plot_warning.Warning("Warning: In the phase plot there were some points that had an issue showing due to an invalid value encountered in the function" + warning.message.args[0][28:] + " (for example cos(inf), arccos(2), etc)", cwd=settings["cwd"])
                                invalid_value_in_function_in_phase_plot_warning.Show()
                        elif(warning.message.args[0][:8]=="overflow"):
                            if(settings["stop_overflow_in_phase_plot_warning"]==False):
                                overflow_in_phase_plot_warning = popup_windows.popup_window(main_frame)
                                overflow_in_phase_plot_warning.Warning("Warning: overflow warning when constructing phase plot, this can be caused by a really large number or a small number being added to a small number", cwd=settings["cwd"])
                                overflow_in_phase_plot_warning.Show()
                        elif(warning.message.args[0][:9]=="underflow"):
                            if(settings["stop_underflow_in_phase_plot_warning"]==False):
                                overflow_in_phase_plot_warning = popup_windows.popup_window(main_frame)
                                overflow_in_phase_plot_warning.Warning("Warning: underflow warning when constructing phase plot, this can be caused by numbers that are too small", cwd=settings["cwd"])
                                overflow_in_phase_plot_warning.Show()
                        elif(warning): #cannot simply raise excpetion or some issues may be missed
                            Unknown_Error = popup_windows.popup_window(main_frame)
                            Unknown_Error.Warning("Warning, "+warning.message.args[0]+"\nNOTE: I have not seen this message during testing. Please email samuelcstreet@gmail.com with details about what you are trying to do and I will add a new warning setting to shut this warning off if you would like, otherwise this message cannot be silenced", cwd=settings["cwd"])
                            Unknown_Error.Show()
            except ZeroDivisionError as ex:
                Zero_Error = popup_windows.popup_window(main_frame)
                Zero_Error.Error("Error, had to divide by zero somewhere when making phase plot. Program may have been able to proceed, but note there may be large numarical errors when making the small arrows for the phase plot.", cwd=settings["cwd"])
                Zero_Error.Show()
            except Exception as ex:
                Unknown_Error = popup_windows.popup_window(main_frame)
                Unknown_Error.Error("I do not know how this happened, if you are seeing this please email samuelcstreet@gmail.com with details about what you are trying to do with the program and he will try and assist.\n\nError Code: " + ex.__str__(), cwd=settings["cwd"])
                Unknown_Error.Show()

    xpad = (xmax-xmin)/20
    ypad = (ymax-ymin)/20

    if(from_settings==False or (dxdt_text.strip() !='lambda x, y: ()' and dydt_text.strip() !='lambda x, y: ()')):
        ### plot line ### Need to upgrade from Eulur
        num_of_start = len(starting_points)
        if(num_of_start != 0):
            if(method == "Euler"):
                for start in starting_points:
                    x_points_forwards, y_points_forwards = get_points_for_forward_trace_Eurler(start, forward_steps, h, dxdt, dydt, main_frame, xmin, xmax, ymin, ymax, xpad, ypad, settings)
                    if(settings["show_legend"]==True):
                        fig.add_trace(
                        go.Scatter(
                            visible=True,
                            marker = dict(size=15,symbol= "arrow-bar-up", angleref="previous"),
                            line=dict(color="#0763e9", width=1),
                            x=x_points_forwards,
                            y=y_points_forwards,
                            name = str(start) + " time forwards"))
                    else:
                        fig.add_trace(
                        go.Scatter(
                            visible=True,
                            marker = dict(size=15,symbol= "arrow-bar-up", angleref="previous"),
                            line=dict(color="#0763e9", width=1),
                            x=x_points_forwards,
                            y=y_points_forwards,
                            name = str(start) + " time forwards",
                            showlegend=False))
        num_of_start = len(starting_points)
        if(num_of_start != 0):
            if(method == "Euler"):
                for start in starting_points:
                    x_points_backwards, y_points_backwards = get_points_for_backwards_trace_Eurler(start, backward_steps, h, dxdt, dydt, main_frame, xmin, xmax, ymin, ymax, xpad, ypad, settings)

                    if(settings["show_legend"]==True):
                        fig.add_trace(
                        go.Scatter(
                            visible=True,
                            marker = dict(size=15,symbol= "arrow-bar-up", angleref="previous"),
                            line=dict(color="#076309", width=1),
                            x=x_points_backwards,
                            y=y_points_backwards,
                            name = str(start) + " time backwards"))
                    else:
                        fig.add_trace(
                        go.Scatter(
                            visible=True,
                            marker = dict(size=15,symbol= "arrow-bar-up", angleref="previous"),
                            line=dict(color="#076309", width=1),
                            x=x_points_backwards,
                            y=y_points_backwards,
                            name = str(start) + " time backwards",
                            showlegend=False))
                        
                fig.update_layout(legend=dict(
                    yanchor="top",
                    y=1,
                    xanchor="right",
                    x=1
                ))
            elif(method != ""):
                variable_error_window = popup_windows.popup_window(main_frame)
                variable_error_window.Info("Sorry, this numarical method has not yet been added; however, if you email: samuelcstreet@gmail.com he would be happy to add it", cwd = settings["cwd"])
                variable_error_window.Show()
            else:
                variable_error_window = popup_windows.popup_window(main_frame)
                variable_error_window.Error("Sorry, no numerical method added", cwd = settings["cwd"])
                variable_error_window.Show() 
    if(num_of_start!=0):
        for start in starting_points:
            fig.add_trace(go.Scatter(
                        x=[start[0]],
                        y=[start[1]],
                        marker=dict(color="black", size=5),
                        mode="markers",
                        name="",
                        showlegend=False
                    ))
    fig.update_layout(xaxis=dict(range=[xmin-xpad,xmax+xpad]))
    fig.update_layout(yaxis=dict(range=[ymin-ypad,ymax+ypad]))
    fig.update_layout(
    title=dict(
        text= settings["title"]
    ),
    xaxis=dict(
        title=dict(
            text=settings["x_axis_title"]
        )
    ),
    yaxis=dict(
        title=dict(
            text=settings["y_axis_title"]
        )
    )
    )

    fig.write_html(settings["cwd"]+"/Graphs/Display_Plot.html")
    #fig.show()


##TEST
if __name__ == "__main__":
    dxdt_text = 'lambda x,y: 5'
    dydt_text = 'lambda x,y: 5'
    settings = {
        "xmin": -5.0,
        "xmax": 5.0,
        "ymin": -5.0,
        "ymax": 5.0,
        "arrow_scale": 0.5,
        "starting_points": [[1,1],],
        "h": 0.01,
        "xdensity": 20,
        "ydensity": 20,
        "steps": 1000,
        "method": "Euler",
        "stop_variable_override_warning": False,
        "stop_termination_warning": False,
        "settings_file": "/settings.json",
        "cwd": "C:/Users/Samuel/Downloads/Programming related/Python/PPP",
        "x_axis_title": "x_axis title",
        "y_axis_title": "y_axis title",
        "title": "Graph Title"
    }
    make_figure(main_frame=None, dxdt_text=dxdt_text, dydt_text=dydt_text, settings=settings, variables_text="")