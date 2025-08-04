"""
Day 10: Functions with outputs
"""
def format_name(f_name, l_name):
    """Take a first and last name and format it to return
    the title cased version of each name.

    :param f_name: The first name
    :type f_name: str

    :param l_name: The last name
    :type l_name: str

    :returns: string formed by concatenating the title-cased f_name and l_name
    :rtype: str
    """
    if f_name == "" and l_name == "":
        return "No first or last name provided"

    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"{formatted_f_name} {formatted_l_name}"
    # print("This is never printed")

print(format_name(input("What is your first name? "), input("What is your last name? ")))