import requests
import re
from urllib.parse import urljoin, urlparse
import os

def download_html_css(url):
    # Ensure the URL starts with http:// or https://
    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    # Create a session
    session = requests.Session()

    # Download the HTML content
    response = session.get(url)
    response.raise_for_status()
    html_content = response.text

    # Save the HTML content
    parsed_url = urlparse(url)
    domain_name = parsed_url.netloc
    os.makedirs(domain_name, exist_ok=True)
    html_file = os.path.join(domain_name, "index.html")
    with open(html_file, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"HTML content saved to {html_file}")

    # Find and download all CSS files
    css_files = re.findall(r'<link.*?href="(.*?\.css)".*?>', html_content)
    for css_file in css_files:
        css_url = urljoin(url, css_file)
        css_response = session.get(css_url)
        css_response.raise_for_status()
        css_filename = os.path.basename(css_file)
        css_file_path = os.path.join(domain_name, css_filename)
        with open(css_file_path, "w", encoding="utf-8") as file:
            file.write(css_response.text)
        print(f"CSS file saved to {css_file_path}")

if __name__ == "__main__":
    website_url = input("Enter the website URL: ")
    download_html_css(website_url)