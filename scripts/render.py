from playwright.sync_api import sync_playwright
from pathlib import Path

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    html_file_url = Path('output/resume.html').absolute().as_uri()
    # Navigate to the local HTML file
    page.goto(html_file_url)
    page.pdf(path='output/resume.pdf', format='A4', print_background=True)
    browser.close()

