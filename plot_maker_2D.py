import plotly.graph_objects as go
import numpy as np
import popup_windows
from numpy import sin, cos, tan, arcsin, arccos, arctan, sinh, cosh, tanh, log, log10, log2, e, pi
π = pi
ln = lambda x: log(x)
def get_points_for_forward_trace_Eurler(start, steps, h, dxdt, dydt, main_frame, xmin, xmax, ymin, ymax, xpad, ypad, settings):
    x_points_forwards = [start[0]]
    y_points_forwards = [start[1]]
    np.ceil(steps)
    for i in range(steps):
        stop = False
        prev_x = x_points_forwards[-1]
        prev_y = y_points_forwards[-1]
        try: # adds lots of time to figuring out the graph
            next_x = prev_x + h*dxdt(prev_x, prev_y)
            next_y = prev_y + h*dydt(prev_x, prev_y)
        except OverflowError as e:
            print("")
            termination_warning  = popup_windows.popup_window(main_frame)
            termination_warning.Warning("WARNING, process haulted due to numerical error\nwhen going forwards in time.", cwd=settings["cwd"])
            termination_warning.Show()
            return x_points_forwards, y_points_forwards
            
        x_points_forwards.append(next_x)
        y_points_forwards.append(next_y)
        if(next_x>xmax+xpad or next_x<xmin-xpad):
            stop = True
            if(stop == True):
                termination_warning  = popup_windows.popup_window(main_frame)
                termination_warning.Warning("WARNING, Terminated on step " + str(i+1)+ "\nwhen going forwards in time.", cwd=settings["cwd"])
                termination_warning.Show()
                return x_points_forwards, y_points_forwards
                # if it can be done without error then proceed 1 step farthure than the boundry of the chosen region
        if(next_y>ymax+ypad or next_y<ymin-ypad):
            stop = True
            if(stop == True):
                termination_warning = popup_windows.popup_window(main_frame)
                termination_warning.Warning("WARNING, Terminated on step " + str(i+1)+ "\nwhen going forwards in time.", cwd=settings["cwd"])
                termination_warning.Show()
                return x_points_forwards, y_points_forwards
                # if it can be done without error then proceed 1 step farthure than the boundry of the chosen region
    pass
    return x_points_forwards, y_points_forwards

def get_points_for_backwards_trace_Eurler(start, steps, h, dxdt, dydt, main_frame, xmin, xmax, ymin, ymax, xpad, ypad, settings):
    x_points_backwards = [start[0]]
    y_points_backwards = [start[1]]
    np.ceil(steps)
    for i in range(steps):
        stop = False
        prev_x = x_points_backwards[-1]
        prev_y = y_points_backwards[-1]
        try: # adds lots of time to figuring out the graph
            next_x = prev_x - h*dxdt(prev_x, prev_y)
            next_y = prev_y - h*dydt(prev_x, prev_y)
        except OverflowError as e:
            print("")
            termination_warning  = popup_windows.popup_window(main_frame)
            termination_warning.Warning("WARNING, process haulted due to numerical error\nwhen going backwards in time.", cwd=settings["cwd"])
            termination_warning.Show()
            return x_points_backwards, y_points_backwards
            
        x_points_backwards.append(next_x)
        y_points_backwards.append(next_y)
        if(next_x>xmax+xpad or next_x<xmin-xpad):
            stop = True
            if(stop == True):
                termination_warning  = popup_windows.popup_window(main_frame)
                termination_warning.Warning("WARNING, Terminated on step " + str(i+1)+"\nwhen going backwards in time.", cwd=settings["cwd"])
                termination_warning.Show()
                return x_points_backwards, y_points_backwards
                # if it can be done without error then proceed 1 step farthure than the boundry of the chosen region
        if(next_y>ymax+ypad or next_y<ymin-ypad):
            stop = True
            if(stop == True):
                termination_warning = popup_windows.popup_window(main_frame)
                termination_warning.Warning("WARNING, Terminated on step " + str(i+1)+"\nwhen going backwards in time.", cwd=settings["cwd"])
                termination_warning.Show()
                return x_points_backwards, y_points_backwards
                # if it can be done without error then proceed 1 step farthure than the boundry of the chosen region
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
    steps = settings["steps"]
    method = settings["method"]
    arrow_scale = settings["arrow_scale"]

    #### Setup
    fig = go.Figure()
    xmin = settings["xmin"]
    xmax = settings["xmax"]
    ymin = settings["ymin"]
    ymax = settings["ymax"]
    
    main_frame.display.display.SetSize(main_frame.display.GetSize())

    fig.update_layout(
        width = main_frame.display.display.GetSize().Width-20,
        height = main_frame.display.display.GetSize().Height-20,
    )

    #### phase plot
    if(from_settings==False or (dxdt_text.strip() !='lambda x, y: ()' and dydt_text.strip() !='lambda x, y: ()')):
        if(xdensity !=0 and ydensity !=0):
            xdif = (xmax-xmin)/xdensity
            xbases = np.arange(xmin, xmax+xdif, xdif)
            ydif = (ymax-ymin)/ydensity
            ybases = np.arange(ymin, ymax+ydif, ydif)
            for x_temp in (xbases):
                for y_temp in (ybases):
                    fig.add_trace(
                        go.Scatter(
                            visible = True,
                            marker = dict(size=4,symbol= "arrow-bar-up", angleref="previous"),
                            line=dict(color="#000000", width=1),
                            x=[x_temp, x_temp + dxdt(x_temp, y_temp)*xdif*arrow_scale],
                            y=[y_temp, y_temp + dydt(x_temp, y_temp)*xdif*arrow_scale],
                            showlegend=False))

    xpad = (xmax-xmin)/20
    ypad = (ymax-ymin)/20

    if(from_settings==False or (dxdt_text.strip() !='lambda x, y: ()' and dydt_text.strip() !='lambda x, y: ()')):
        ### plot line ### Need to upgrade from Eulur
        num_of_start = len(starting_points)
        if(num_of_start != 0):
            if(method == "Euler"):
                for start in starting_points:
                    x_points_forwards, y_points_forwards = get_points_for_forward_trace_Eurler(start, steps, h, dxdt, dydt, main_frame, xmin, xmax, ymin, ymax, xpad, ypad, settings)
                    
                    fig.add_trace(
                    go.Scatter(
                        visible=True,
                        marker = dict(size=12,symbol= "arrow-bar-up", angleref="previous"),
                        line=dict(color="#0763e9", width=1),
                        x=x_points_forwards,
                        y=y_points_forwards,
                        name = str(start) + " backwards time"))

        num_of_start = len(starting_points)
        if(num_of_start != 0):
            if(method == "Euler"):
                for start in starting_points:
                    x_points_backwards, y_points_backwards = get_points_for_backwards_trace_Eurler(start, steps, h, dxdt, dydt, main_frame, xmin, xmax, ymin, ymax, xpad, ypad, settings)

                    fig.add_trace(
                    go.Scatter(
                        visible=True,
                        marker = dict(size=12,symbol= "arrow-bar-up", angleref="previous"),
                        line=dict(color="#076309", width=1),
                        x=x_points_backwards,
                        y=y_points_backwards,
                        name = str(start) + " forward time"))

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
    dxdt_text = 'lambda x,y: a'
    dydt_text = 'lambda x,y: a'
    settings = {
        "xmin": -5.0,
        "xmax": 5.0,
        "ymin": -5.0,
        "ymax": 5.0,
        "arrow_scale": 1,
        "starting_points": [(1,1)],
        "h": 0.001,
        "xdensity": 10,
        "ydensity": 10,
        "steps": 10000,
        "method": "Euler",
        "cwd": "blablabla"
    }
    #f_and_v = 'ln = lambda x: log(x);         e = np.e;         π = np.pi;         pi = np.pi;a = 5; '
    f_and_v = 'a = 5'
    make_figure(dxdt_text=dxdt_text, dydt_text=dydt_text, settings=settings, stuff=f_and_v)