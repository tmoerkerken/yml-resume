from playwright.sync_api import sync_playwright
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--theme", default="graytopia", help = "(default: %(default)s)")
parser.add_argument("--accent-color", default="#ffb300", help = "(default: %(default)s)")
parser.add_argument("--foreground-color", default="black", help = "(default: %(default)s)")
args = parser.parse_args()

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    html_file_url = Path('output/resume.html').absolute().as_uri()
    # Navigate to the local HTML file
    page.goto(html_file_url)
    page.pdf(path='output/resume.pdf', format='A4', print_background=True)
    browser.close()

