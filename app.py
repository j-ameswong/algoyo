import main
import PySimpleGUI as sg
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use("TkAgg")

def return_figure(date, data):
    fig = matplotlib.figure.Figure(figsize=(5, 4), dpi=100)
    t = np.arange(0, 3, .01)
    fig.add_subplot(111).plot(t, t)
    return fig

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side="top", fill="both", expand=1)
    return figure_canvas_agg

# Define the window layout
layout = [
    [sg.Text("AlgoYo")],
    [sg.Canvas(key="-CANVAS-")],
    [sg.Button("Ok")],
]

# Create the form and show it without the plot
window = sg.Window(
    layout,
    location=(0, 0),
    finalize=True,
    element_justification="center",
    font="Helvetica 18",
)

# Add the plot to the window
draw_figure(window["-CANVAS-"].TKCanvas, return_figure(0,0))

event, values = window.read()

window.close()