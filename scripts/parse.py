from jinja2 import Environment, FileSystemLoader
import yaml
import shutil
from pathlib import Path

import argparse
from datetime import datetime
import configparser

parser = argparse.ArgumentParser()
parser.add_argument("--theme", default="graytopia", help = "(default: %(default)s)")

args = parser.parse_args()

theme_folder = Path('templates') / args.theme
config = configparser.ConfigParser()
config.read(theme_folder / 'defaults.cfg')

with open('resume.yml', 'r') as file:
  resume = yaml.safe_load(file)

resume["theme"] = {}
resume["theme"] = config["colors"]


# inject computed
current_year = datetime.now().year
birth_date_str = resume["profile"]["birth_date"]  # day-month-year format
birth_date = datetime.strptime(birth_date_str, '%d-%m-%Y')
current_date = datetime.now()
age = current_date.year - birth_date.year

# adjust age if the birth date has not yet occurred this year
if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
    age -= 1

resume["profile"]["age"] = age

# load templates folder to environment (security measure)
env = Environment(loader=FileSystemLoader(theme_folder))

# load the `index.jinja` template
template = env.get_template('template.jinja.html')
output_from_parsed_template = template.render(resume=resume)

# write the parsed template
with open(Path("output") / "resume.html", "w") as chap_page:
  chap_page.write(output_from_parsed_template)

shutil.copy2(theme_folder / "template.css", Path("output") / "_template.css")
shutil.copytree(theme_folder / "images", Path("output") / "images", dirs_exist_ok=True)