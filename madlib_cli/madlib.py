import re


def welcome_message():
    """
    Prints a welcome message to the user.
    """
    print("**********************************************")
    print("**    Welcome to our CLI MadLib Generator!  **")
    print("**    Our tool can help you create your     **")
    print("**    own fun word games or play one of     **")
    print("**    our existing stories.                 **")
    print("**********************************************")



def read_template(template):
    """
    Reads in a template file and returns its content as a string.

    Args:
        template (str): The path to the template file.

    Raises:
        FileNotFoundError: If the file path is invalid.

    Returns:
        str: The content of the template file.
    """
    try:
        with open(template) as file_data:
            content = file_data.read()
            return content
    except FileNotFoundError:
        raise FileNotFoundError(f"\n \n*** Invalid file path: {template} ***\n")


def parse_template(template):
    template_parts = re.findall(r'\{([a-zA-Z 1-50 \' \-]+)\}', template)
    template_parts_tup = tuple(template_parts)
    template_stripped = re.sub(r'\{([a-zA-Z 1-50 \' \-]+)\}', '{}', template)
    return template_stripped, template_parts_tup


def parse_full_template(template):
    """
    Prompts the user to input values for all placeholders in a template and returns a completed template string.

    Args:
        template (str): The template string to fill in.

    Returns:
        str: The completed template string.
    """

    template_parts = re.findall(r'\{([a-zA-Z 1-50 \' \-]+)\}', template)
    template_parts_tup = tuple(template_parts)
    template_stripped = re.sub(r'\{([a-zA-Z 1-50 \' \-]+)\}', '{}', template)

    # template_stripped = template.format(Adjective="{}", Noun="{}")
    # template_parts = []

    # for i in range(template.count("{")):
    #     parts = template.split("{")[i+1].split("}")[0]
    #     template_parts.append(parts)
    # template_parts_tup = tuple(template_parts)

    inputs = []
    for part in template_parts_tup:
        question = "Enter {} ".format(part)
        res = input(question)
        inputs.append(res)

    return template_stripped, inputs


# def parse_template(template):
#     # template = "It was a {Adjective} and {Adjective} {Noun}."
#     template_stripped = template.format(Adjective="{}",Noun="{}")
#     template_parts =[]
#     for i in range(template.count("{")):
#         parts = template.split("{")[i+1].split("}")[0]
#         template_parts.append(parts)

#     template_parts_tup = tuple(template_parts)

#     print(template_stripped ,template_parts_tup)
#     return template_stripped ,template_parts_tup


# def parse_template(template):
#     template_stripped = template.format(Adjective="{}", Noun="{}")
#     template_parts = []
#     for part in template_stripped.split():
#         if "{" in part and "}" in part:
#             template_parts.append(part.strip("{}"))

#     template_parts_tup = tuple(template_parts)
#     return template_stripped, template_parts_tup


def merge(template_stripped, inputs):
    """
    Fills in a stripped template string with the provided input values and returns the completed template.

    Args:
        template_stripped (str): The stripped template string to fill in.
        inputs (tuple): A tuple containing the input values to fill in the template.

    Returns:
        str: The completed template string.
    """

    result = template_stripped.format(*inputs)
    print("\n"+result)
    return result


if __name__ == '__main__':
    welcome_message()

    template = read_template('assets/full_dark_and_stormy_night_template.txt')

    template_stripped, inputs = parse_full_template(template)

    completed_template = merge(template_stripped, inputs)

    with open('assets/completed_template.txt', 'w') as file:
        file.write(completed_template)

    print('\n Completed template written to file!')

