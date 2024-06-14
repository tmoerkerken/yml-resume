from playwright.sync_api import sync_playwright
from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input-dir", default="input", help="(default: %(default)s)")
args = parser.parse_args()

input_dir = Path(args.input_dir)
output_dir = input_dir / "build"
output_dir.mkdir(exist_ok=True)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    html_file_url = Path(output_dir / "resume.html").absolute().as_uri()
    # Navigate to the local HTML file
    page.goto(html_file_url)
    page.pdf(path=output_dir / "resume.pdf", format="A4", print_background=True)
    browser.close()
