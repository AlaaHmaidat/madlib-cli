import re

def welcome_message():
    print("**********************************************")
    print("**    Welcome to our CLI MadLib Generator!  **")
    print("**    Our tool can help you create your     **")
    print("**    own fun word games or play one of     **")
    print("**    our existing stories.                 **")
    print("**********************************************")


welcome_message()


def read_template(file):
    with open(file) as file_data:
        content = file_data.read()
        return content


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

def merge(template, tuple):

    template = template.format(*tuple)

    return template


def parse_template():
    # template = "It was a {Adjective} and {Adjective} {Noun}."
    with open("assets/full_dark_and_stormy_night_template.txt") as file:
        template = file.read()

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

    result = template_stripped.format(*inputs)
    print(result)
    return template_stripped, template_parts_tup


# print(read_template("assets/dark_and_stormy_night_template.txt"))
parse_template()
# merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
