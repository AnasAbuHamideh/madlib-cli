import re

def welcome():
    '''
    function returns welcome message
    '''
    print("Welcome to Madlib , Answer the Questions below and go ahead")

def user_input(path):
    """
    function returns the user inputs.
    """
    try:
        with open(path, "r") as f:
            content = f.read().strip().replace("\n","\n")
    except :
       raise FileNotFoundError("path not found")

    input_placeholders= parse_template(content)[0]

    inputs = []
    for i in input_placeholders:
        add_language_part = input(f"type in {i}:")
        inputs.append(add_language_part)

    return inputs

def read_template(path):
    '''
    function reads txt file from assets folder then return content.
    '''
    try:
        file = open(path)
        content = file.read().strip()
        file.close()
        return content
    except FileNotFoundError:
        print("FileNotFoundError")


def read_content(path):
    """
    function reads the content of the file that contains the template of the game.
    """
    try:
        with open(path, "r") as template:
            content = template.read().strip().replace("\n","\n")
    except FileNotFoundError:
        content = "Error: Sorry, file does not exist"
    else:
        return content

def parse_template(template):
    """
    A function that takes a string and returns a template without the language_parts and a list with the language parts
    """
    language_parts = re.findall(r"\{(.*?)\}", template_content)
    for language_part in language_parts:
        template_content = template_content.replace(language_part, "")
    return [language_parts, template_content] 


def merge(users_inputs,bare_template):
    """
    function takes the bare_template and the user_inputs as an input and return the final output which is a string with the language parts from the user included inside the bare_template
    """
    for input in users_inputs:
        user_output = bare_template[1].replace("{}", f"{input}")
    print(user_output)

if __name__ == "__main__":
    welcome()
    print(read_template('assets/dark_and_stormy_night_template.txt'))
    # user_input = user_input("assets/madlib_template.txt")
    # template_content = read_content("assets/madlib_template.txt")
    # bare_template = parse_template(template_content)
    # merge(bare_template, user_input)