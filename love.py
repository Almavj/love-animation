import tkinter as tk
import random

# List of colors for mixing
colors = ["#FF0000", "#FFA500", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#EE82EE"]

# Function to mix colors randomly
def mix_colors():
    return random.choice(colors)

# Function to update the text color and position
def animate_text():
    global x_position
    current_color = mix_colors()  # Get a random color
    label.config(fg=current_color)  # Update the label's color

    # Update the position of the label
    x_position += 5  # Move right by 5 pixels
    if x_position > root.winfo_width():  # If the text goes completely out on the right
        x_position = -label.winfo_width()  # Start again from the left edge

    label.place(x=x_position, y=100)  # Update label's position
    root.after(100, animate_text)  # Call this function again after 100 ms

# Create the main window
root = tk.Tk()
root.title("I LOVE YOU Animation")
root.geometry("600x200")

# Create a label to display the text
label = tk.Label(root, text="I LOVE YOU", font=("Helvetica", 48))
label.pack(expand=True)

# Initialize starting position to start from the left
x_position = -label.winfo_width()

# Start the animation
root.after(100, animate_text)  # Initial delay to ensure window size is set
animate_text()

# Start the Tkinter event loop
root.mainloop()
