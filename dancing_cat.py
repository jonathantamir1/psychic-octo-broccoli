import tkinter as tk
from PIL import Image, ImageTk, ImageSequence

cat_path = "dancing_cat.gif"

root = tk.Tk()
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "white")
root.configure(bg='white')

cat_gif = Image.open(cat_path)
frames = [ImageTk.PhotoImage(frame.copy().convert("RGBA")) for frame in ImageSequence.Iterator(cat_gif)]
label = tk.Label(root, bd=0, bg="white")
label.pack()

def animate(i=0):
    label.config(image=frames[i])
    root.after(100, animate, (i+1) % len(frames))

root.geometry("+300+200")
animate()
root.mainloop()
