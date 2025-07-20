import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

# Path to your GIF
cat_path = "cat-piano.gif"

# Load the GIF
cat_gif = Image.open(cat_path)

# Create the fullscreen window
root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg='black')
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "black")

# Resize each frame to fill the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

frames = [
    ImageTk.PhotoImage(
        frame.copy().convert("RGBA").resize((screen_width, screen_height))
    )
    for frame in ImageSequence.Iterator(cat_gif)
]

# Create and place label
label = tk.Label(root, bd=0, bg='black')
label.pack(fill="both", expand=True)

# Animate
def animate(i=0):
    label.config(image=frames[i])
    root.after(100, animate, (i + 1) % len(frames))

animate()
root.mainloop()
