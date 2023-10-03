from src.area_rectangle import area_rectangule

if __name__ == "__main__":

    base_input = input("Provide the base of the rectangle: \n")
    base: float = float(base_input)
    height_input = input("Inform the height of the rectangle: \n")
    height: float = float(height_input)

    area: float = area_rectangule(base, height)
    print(f"Area of rectangle with base and height provided is: Area = {area}")
