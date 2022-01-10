PI = 3.14

def areaofcircle(radius):

    try:

        result = PI * radius * radius

        print("Area of circle with radius", radius, "is", result, "unit")

    except OSError as err:

        print("Radius can't be zero{0}".format(err))