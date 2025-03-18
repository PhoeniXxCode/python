import math

# Function to calculate the area of a circle
def area_of_circle(radius):
    return math.pi * radius ** 2

# Function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    return length * width

# Function to calculate the area of a triangle
def area_of_triangle(base, height):
    return 0.5 * base * height

# Main program
def main():
    print("Choose the geometric figure to calculate the area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    
    choice = int(input("Enter the number corresponding to your choice: "))
    
    if choice == 1:
        radius = float(input("Enter the radius of the circle: "))
        area = area_of_circle(radius)
        print(f"The area of the circle is: {area:.2f} square units.")
    
    elif choice == 2:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = area_of_rectangle(length, width)
        print(f"The area of the rectangle is: {area:.2f} square units.")
    
    elif choice == 3:
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = area_of_triangle(base, height)
        print(f"The area of the triangle is: {area:.2f} square units.")
    
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()