import math

def circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius ** 2

def rectangle_area(width, height):
    """Calculate the area of a rectangle."""
    return width * height

def triangle_area(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

if __name__ == "__main__":
    print(f"Circle (r=5): {circle_area(5):.2f}")
    print(f"Rectangle (4x6): {rectangle_area(4, 6):.2f}")
    print(f"Triangle (b=3, h=8): {triangle_area(3, 8):.2f}")
