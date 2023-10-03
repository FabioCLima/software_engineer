from src.point_class import Point


if __name__ == "__main__":

    x_input = input("Type the x coordinate, \n")
    y_input = input("Type the y coordinate, \n")

    x = float(x_input)
    y = float(y_input)

    p1 = Point(x, y)
    print(f"The point create is: {p1}")

    print("Calculating the distance between the p1 to the origin...")
    distance_origin = p1.distance_to_origin()
    print(f"Distance from p1 to origin is: {distance_origin}\n")
    print("Reflecting the point to x axis:...")
    axis = "x"
    reflect_x = p1.reflect(axis)
    print(f"p1 reflect from x axis is: {reflect_x}")
    print("Reflecting the point to y axis:...")
    axis = "y"
    print(f"p1 reflect from x axis is: {p1.reflect(axis)}")
