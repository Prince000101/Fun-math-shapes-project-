import tkinter as tk
from tkinter import ttk
import math


# Function to rotate coordinates by a given angle
def rotate_point(x, y, angle, center_x, center_y):
    rad = math.radians(angle)
    x_rot = center_x + (x - center_x) * math.cos(rad) - (y - center_y) * math.sin(rad)
    y_rot = center_y + (x - center_x) * math.sin(rad) + (y - center_y) * math.cos(rad)
    return x_rot, y_rot


# Function to draw a Rectangle with rotation
def draw_rectangle(canvas, center_x, center_y, size, angle, show_dot):
    points = [
        (center_x - size, center_y - size // 2),
        (center_x + size, center_y - size // 2),
        (center_x + size, center_y + size // 2),
        (center_x - size, center_y + size // 2)
    ]
    rotated_points = [rotate_point(x, y, angle, center_x, center_y) for x, y in points]
    canvas.create_polygon(rotated_points, fill="#FF5C5C", outline="#333333", width=2)
    if show_dot:
        # Mark the center with a dot
        canvas.create_oval(center_x - 3, center_y - 3, center_x + 3, center_y + 3, fill="black")


# Function to draw a Square with rotation
def draw_square(canvas, center_x, center_y, size, angle, show_dot):
    points = [
        (center_x - size // 2, center_y - size // 2),
        (center_x + size // 2, center_y - size // 2),
        (center_x + size // 2, center_y + size // 2),
        (center_x - size // 2, center_y + size // 2)
    ]
    rotated_points = [rotate_point(x, y, angle, center_x, center_y) for x, y in points]
    canvas.create_polygon(rotated_points, fill="#5CFF5C", outline="#333333", width=2)
    if show_dot:
        # Mark the center with a dot
        canvas.create_oval(center_x - 3, center_y - 3, center_x + 3, center_y + 3, fill="black")


# Function to draw an Ellipse with rotation
def draw_ellipse(canvas, center_x, center_y, size, angle, show_dot):
    # Ellipse points (quarter-circle)
    points = []
    for i in range(0, 360, 15):  # Create points for ellipse
        x = center_x + size * math.cos(math.radians(i))
        y = center_y + size // 2 * math.sin(math.radians(i))
        points.append((x, y))

    # Rotate each point
    rotated_points = [rotate_point(x, y, angle, center_x, center_y) for x, y in points]
    canvas.create_polygon(rotated_points, fill="#FFFF5C", outline="#333333", width=2)
    if show_dot:
        # Mark the center with a dot
        canvas.create_oval(center_x - 3, center_y - 3, center_x + 3, center_y + 3, fill="black")


# Function to draw an Equilateral Triangle with rotation
def draw_triangle(canvas, center_x, center_y, size, angle, show_dot):# Calculate the height of the equilateral triangle
    height = math.sqrt(3) * size / 2
    # Define the three vertices of the equilateral triangle
    points = [
        (center_x, center_y - height / 2),  # top vertex
        (center_x + size / 2, center_y + height / 2),  # bottom right
        (center_x - size / 2, center_y + height / 2)  # bottom left
    ]

    # Rotate the points around the center of the triangle
    rotated_points = [rotate_point(x, y, angle, center_x, center_y) for x, y in points]
    canvas.create_polygon(rotated_points, fill="#5C5CFF", outline="#333333", width=2)
    if show_dot:
        # Mark the center with a dot
        canvas.create_oval(center_x - 3, center_y - 3, center_x + 3, center_y + 3, fill="black")


# Function to draw a Circle with rotation
def draw_circle(canvas, center_x, center_y, size, angle, show_dot):
    canvas.create_oval(center_x - size, center_y - size,
                       center_x + size, center_y + size,
                       fill="#FFFF5C", outline="#333333", width=2)
    if show_dot:
        # Mark the center with a dot
        canvas.create_oval(center_x - 3, center_y - 3, center_x + 3, center_y + 3, fill="black")


# Function to draw a Hexagon with rotation
def draw_hexagon(canvas, center_x, center_y, size, angle, show_dot):
    points = [(center_x + size * math.cos(math.radians(angle)), center_y + size * math.sin(math.radians(angle)))
              for angle in range(0, 360, 60)]
    rotated_points = [rotate_point(x, y, angle, center_x, center_y) for x, y in points]
    canvas.create_polygon(rotated_points, fill="#FF5CFF", outline="#333333", width=2)
    if show_dot:
        # Mark the center with a dot
        canvas.create_oval(center_x - 3, center_y - 3, center_x + 3, center_y + 3, fill="black")


# Function to draw a Pentagon with rotation
def draw_pentagon(canvas, center_x, center_y, size, angle, show_dot):
    points = [(center_x + size * math.cos(math.radians(angle)), center_y + size * math.sin(math.radians(angle)))
              for angle in range(0, 360, 72)]
    rotated_points = [rotate_point(x, y, angle, center_x, center_y) for x, y in points]
    canvas.create_polygon(rotated_points, fill="#FFDD5C", outline="#333333", width=2)
    if show_dot:
        # Mark the center with a dot
        canvas.create_oval(center_x - 3, center_y - 3, center_x + 3, center_y + 3, fill="black")


# Function to draw an Octagon with rotation
def draw_octagon(canvas, center_x, center_y, size, angle, show_dot):
    points = [(center_x + size * math.cos(math.radians(angle)), center_y + size * math.sin(math.radians(angle)))
              for angle in range(0, 360, 45)]
    rotated_points = [rotate_point(x, y, angle, center_x, center_y) for x, y in points]
    canvas.create_polygon(rotated_points, fill="#5C5CFF", outline="#333333", width=2)
    if show_dot:
        # Mark the center with a dot
        canvas.create_oval(center_x - 3, center_y - 3, center_x + 3, center_y + 3, fill="black")


# Function to draw a Star with rotation
def draw_star(canvas, center_x, center_y, size, angle, show_dot):
    points = []
    for i in range(5):
        angle_outer = i * 144
        angle_inner = angle_outer + 72
        points.append((center_x + size * math.cos(math.radians(angle_outer)),
                       center_y + size * math.sin(math.radians(angle_outer))))
        points.append((center_x + size * 0.4 * math.cos(math.radians(angle_inner)),
                       center_y + size * 0.4 * math.sin(math.radians(angle_inner))))
    rotated_points = [rotate_point(x, y, angle, center_x, center_y) for x, y in points]
    canvas.create_polygon(rotated_points, fill="#5CFF5C", outline="#333333", width=2)
    if show_dot:
        # Mark the center with a dot
        canvas.create_oval(center_x - 3, center_y - 3, center_x + 3, center_y + 3, fill="black")


# Function to draw the selected shape
def draw_shape(event=None):
    canvas.delete("all")  # Clear the canvas
    shape = shape_var.get()
    size = size_slider.get()
    angle = angle_slider.get()
    show_dot = show_dot_var.get()

    # Canvas dimensions
    canvas_width = canvas.winfo_width()
    canvas_height = canvas.winfo_height()

    # Center coordinates
    center_x = canvas_width // 2
    center_y = canvas_height // 2

    # Call the appropriate drawing function based on selected shape
    if shape == "Rectangle":
        draw_rectangle(canvas, center_x, center_y, size, angle, show_dot)
    elif shape == "Square":
        draw_square(canvas, center_x, center_y, size, angle, show_dot)
    elif shape == "Triangle":
        draw_triangle(canvas, center_x, center_y, size, angle, show_dot)
    elif shape == "Circle":
        draw_circle(canvas, center_x, center_y, size, angle, show_dot)
    elif shape == "Hexagon":
        draw_hexagon(canvas, center_x, center_y, size, angle, show_dot)
    elif shape == "Pentagon":
        draw_pentagon(canvas, center_x, center_y, size, angle, show_dot)
    elif shape == "Octagon":
        draw_octagon(canvas, center_x, center_y, size, angle, show_dot)
    elif shape == "Star":
        draw_star(canvas, center_x, center_y, size, angle, show_dot)
    elif shape == "Ellipse":
        draw_ellipse(canvas, center_x, center_y, size, angle, show_dot)


# Main application window
root = tk.Tk()
root.title("Shape Drawer with Rotation and Center Marker")
root.geometry("500x600")

# Canvas
canvas = tk.Canvas(root, width=400, height=400, bg="#F5F5DC", highlightthickness=0)
canvas.pack(expand=True, fill="both", side="top", pady=(10, 5))

# Controls frame (for dropdown and sliders)
controls_frame = tk.Frame(root)
controls_frame.pack(side="bottom", fill="x", pady=10)

# Dropdown to select shape
shape_var = tk.StringVar(value="Rectangle")
shapes = ["Rectangle", "Square", "Triangle", "Circle", "Hexagon", "Pentagon", "Octagon", "Star", "Ellipse"]
ttk.Label(controls_frame, text="Select Shape:").grid(row=0, column=0, padx=0, pady=0)
shape_menu = ttk.OptionMenu(controls_frame, shape_var, *shapes, command=draw_shape)
shape_menu.grid(row=0, column=1, padx=0, pady=0)

# Checkbox to toggle center dot visibility (moved to the same column as the dropdown)
show_dot_var = tk.BooleanVar(value=False)
show_dot_checkbox = tk.Checkbutton(controls_frame, text="Dot", variable=show_dot_var, command=draw_shape)
show_dot_checkbox.grid(row=0, column=2, padx=0, pady=0)

# Slider to adjust size
ttk.Label(controls_frame, text="Adjust Size:").grid(row=1, column=0, padx=10, pady=5)
size_slider = ttk.Scale(controls_frame, from_=20, to=200, orient="horizontal", command=draw_shape, length=300)
size_slider.grid(row=1, column=1, padx=10, pady=5)

# Slider to adjust rotation angle
ttk.Label(controls_frame, text="Rotate Angle:").grid(row=2, column=0, padx=10, pady=5)
angle_slider = ttk.Scale(controls_frame, from_=0, to=360, orient="horizontal", command=draw_shape, length=300)
angle_slider.grid(row=2, column=1, padx=10, pady=5)

# Ensure the canvas size updates dynamically
canvas.bind("<Configure>", draw_shape)

# Initial drawing
draw_shape()

root.mainloop()
