# Python

# This will calculate the shapes' areas. 

def main():
    print('This is our shapes program.')
    rectangle_area = calculate_rectangle_area(10, 20)
    print(f'The area of rectange one is {rectangle_area} ')

def calculate_rectangle_area(w, h):
    area = w * h
    return area


if __name__ == "__main__":
    main()