# Python

# This will calculate the shapes' areas. 
import math

def main():
    print('This is our shapes program.')
    rectangle_area = calculate_rectangle_area(10, 20)
    print(f'The area of rectange one is {rectangle_area:.2f} ')
    triangle_area = calc_tri_area(10,20)
    print(f'The area of triangle one is {triangle_area:.2f}')
    circle_area = calc_circle_area(4)
    print(f'The area of circle one is {circle_area:.2f}')

def calculate_rectangle_area(w, h):
    area = w * h
    return area

def calc_tri_area(h,b):
    area = b * h / b
    return area

def calc_circle_area (r):
    area = math.pi * r ** 2
    return area

if __name__ == "__main__":
    main()