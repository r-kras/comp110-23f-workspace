"""The various functions used in ex06."""
__author__ = "730699792"


def invert(input_dict: dict[str, str]) -> dict[str, str]:
    """Inverting the keys and values of a dict."""
    output_dict: dict[str, str] = {}
    # iterate through input dictionary's keys
    for key in input_dict:
        # if value already a key raise key error
        if input_dict[key] in output_dict:
            raise KeyError("2 keys of the same value.")
        # add pair to output_dict
        output_dict[input_dict[key]] = key
    # return output dict
    return output_dict


def favorite_color(names_and_colors: dict[str, str]) -> str:
    """Determines the most frequent color."""
    color_scores: dict[str, int] = {}
    
    # find occurances of color by iterating through the names
    for name in names_and_colors:
        if names_and_colors[name] in color_scores:
            color_scores[names_and_colors[name]] += 1
        else: 
            color_scores[names_and_colors[name]] = 1
    # find the max by iterating through colors
    max_color: str = ""
    max_value: int = -1
    for color in color_scores:
        if color_scores[color] > max_value:
            max_color = color
            max_value = color_scores[color]
    return max_color


def count(input_list: list[str]) -> dict[str, int]:
    """Counts occurances of a value in a list."""
    # initialize empty dict
    output_dict: dict[str, int] = {}
    # iterate through values in input_list
    for key in input_list:
        # if value is present, increment
        if key in output_dict:
            output_dict[key] = output_dict[key] + 1
        # if value not present, initialize
        else:
            output_dict[key] = 1
    return output_dict


def alphabetizer(input_list: list[str]) -> dict[str, list[str]]:
    """Given a list of strings, sorts the strings based on their first letter."""
    # add each element to dict
    output_dict: dict[str, list[str]] = {}
    for element in input_list:
        tmp = element[0].lower()
        if tmp in output_dict:
            output_dict[tmp].append(element)
        else:
            output_dict[tmp] = [element]
    return output_dict


def update_attendance(input_dict: dict[str, list[str]], day: str, name: str) -> dict[str, list[str]]:
    """Adding or creating elements in an attendance sheet."""
    # if day started, add name to list
    if day in input_dict:
        input_dict[day].append(name)
    # if day not started, start with given name
    else:
        input_dict[day] = [name]
    return input_dict