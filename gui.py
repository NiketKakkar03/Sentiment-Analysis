import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from main import process_text, get_graph
import os

def browse_file():
    filepath = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])
    if filepath:
        w = process_text(filepath)
        fig = get_graph(w)
        if os.path.exists('graph.png'):
            os.remove('graph.png')
        fig.savefig('graph.png')
        display_graph(fig)

def display_graph(fig):
    # Clear the previous canvas if it exists
    for widget in root.winfo_children():
        if isinstance(widget, tk.Canvas):
            widget.destroy()
    
    # Create a canvas to display the plot
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=3, columnspan=2)

root = ttk.Window(themename='morph')
root.title('Sentiment Analysis')
root.geometry("800x800")
root.columnconfigure(0, minsize=400)
root.columnconfigure(1, minsize=400)

# Title
title = ttk.Label(root, text="Sentiment Analysis", font=("Helvetica", 32, "bold"))
title.grid(column=0, row=0, columnspan=2, padx=2, pady=2, sticky="ew")
title.configure(anchor="center")

# Select File Button
csvButton = ttk.Button(root, text="Select Word File", command=browse_file)
csvButton.grid(column=0, row=1, sticky="w", padx=5)

# Create a label to display the selected file
selected_file_label = tk.Label(root, text="")
selected_file_label.grid(column=0, row=2)

root.mainloop()
