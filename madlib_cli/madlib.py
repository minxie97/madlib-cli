import re

MAIN_TEMPLATE_PATH = '../assets/main_template.txt'
DEV_TEMPLATE_PATH = '../assets/dark_and_stormy_night_template.txt'
OUTPUT_PATH = '../assets/output.txt'

#function that takes in a path to text file and returns a stripped string of the file’s contents. raises FileNotFoundError if path is no good
def read_template(path):
    try:
        with open(path, 'r') as file:
            return file.read().strip()
    except:
        raise FileNotFoundError

#function that takes in a template string and returns a string with language parts removed and a separate list of those language parts.
#So A {Adjective} and {Adjective} {Noun} => A {} and {} {}, (Adjective, Adjective, Noun)
def parse_template(string):
# thank u regex101.com
    regex = r"{([\w\s\-']*)}"
    removed = re.sub(regex, '{}', string)
    language_parts = tuple(re.findall(regex, string))
    return removed, language_parts

#function that writes completed text in a new file. If no file exists create it and if it does rewrite it.
def write_output(path, string):
    try:
        with open(path, 'x') as file:
            file.write(string)
    except:
        with open(path, 'w') as file:
            file.write(string)

# function that takes in a “bare” template and a list of user entered language parts, and returns a string with the language parts inserted into the template. shout out regex101.com
def merge(template, words):
    regex = r"{([\w\s\-']*)}"
    for word in words:
        template = re.sub(regex, word, template, 1)
    return template

#print welcome statement + instructions
print('''Hi Welcome to Min\'s MadLib Game! When prompted please enter a word that matches what is asked. At the end you'll get your wacky story!''')

#change DEV_TEMPLATE_PATH to MAIN_TEMPLATE_PATH if you want to change the madlib story
template = read_template(DEV_TEMPLATE_PATH)
bare_template, language_parts = parse_template(template)

user_inputs = []

#putting the user inputs into a list
for part in language_parts:
    user_inputs.append(input(f'Enter {part}: '))

#creating the user story
user_story = merge(bare_template, user_inputs)

#provide the completed story back to the user in the command line
print(f'''All Done! Here is your story:
{user_story}''')

#writing the new file with the completed story
write_output(OUTPUT_PATH, user_story)
