import colors

def print_rectangle_properties(rectangle):
    print(
        colors.ANSI_PURPLE + "Printing properties of Rectangle:" + colors.ANSI_RESET
    )

    # width
    print(
        colors.ANSI_CYAN
        + "Width"
        + colors.ANSI_RESET
        + ": "
        + colors.ANSI_YELLOW
        + str(rectangle.get_width())
        + colors.ANSI_RESET
    )

    # height
    print(
        colors.ANSI_CYAN
        + "Height"
        + colors.ANSI_RESET
        + ": "
        + colors.ANSI_YELLOW
        + str(rectangle.get_height())
        + colors.ANSI_RESET
    )

    # area
    print(
        colors.ANSI_CYAN
        + "Area"
        + colors.ANSI_RESET
        + ": "
        + colors.ANSI_YELLOW
        + str(rectangle.get_area())
        + colors.ANSI_RESET
    )

    # perimeter
    print(
        colors.ANSI_CYAN
        + "Perimeter"
        + colors.ANSI_RESET
        + ": "
        + colors.ANSI_YELLOW
        + str(rectangle.get_perimeter())
        + colors.ANSI_RESET
    )

    # diagonal
    print(
        colors.ANSI_CYAN
        + "Diagonal"
        + colors.ANSI_RESET
        + ": "
        + colors.ANSI_YELLOW
        + str(rectangle.get_diagonal())
        + colors.ANSI_RESET
    )

    print(
        colors.ANSI_BLACK + "==================================" + colors.ANSI_RESET
    )
