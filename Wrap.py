def wrap(string, max_width):
    final_string = ""

    for i in range(len(string)):
        if i % max_width == 0 and i != 0:
            final_string += "\n"
        final_string += string[i]
    return final_string
