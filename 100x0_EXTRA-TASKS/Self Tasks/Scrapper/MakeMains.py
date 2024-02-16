#!/usr/bin/python3

import requests
import re
import os
from bs4 import BeautifulSoup

# Function to replace common HTML entities with characters
def replace_html_entities(text):
    html_entities = {
        '&quot;': '"',
        '&amp;': '&',
        '&lt;': '<',
        '&gt;': '>',
    }
    for entity, char in html_entities.items():
        text = text.replace(entity, char)
    return text

def login_and_scrape():
    base_url = "https://intranet.hbtn.io"
    login_url = f"{base_url}/auth/sign_in"
    # Put the number of the project u want the main files of.
    dashboard_url = f"{base_url}/projects/2211"

    # Create a session to handle the cookies
    session = requests.Session()

    # Send a GET request to the login page to obtain CSRF token and cookies
    login_page = session.get(login_url)
    soup = BeautifulSoup(login_page.content, 'html.parser')
    csrf_token = soup.find('meta', attrs={'name': 'csrf-token'})['content']

    # Set the headers and data for the POST request
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'X-CSRF-Token': csrf_token,
    }

    login_data = {
        # Put your own email here
        'user[login]': '6838@holbertonstudents.com',
        # Put your own password
        'user[password]': 'pS!2zB&y8Bw4',
        'commit': 'Log in',
    }

    # Send a POST request to the login page
    login_response = session.post(login_url, headers=headers, data=login_data)

    if login_response.status_code == 200:
        # You are now logged in, and the session cookies are stored in the 'session' object

        # You can access protected pages by using the same session
        dashboard_page = session.get(dashboard_url)
        if dashboard_page.status_code == 200:
            # Process the dashboard page content
            html_content = dashboard_page.text
            makefile(html_content)
        else:
            print("Failed to access the dashboard page.")
    else:
        print("Login failed.")

def makefile(html_content):
    # Use a regular expression to find instances of "-main.py" and the code following it
    code_coordination = re.findall(r'-main.py([\s\S]*?)guillaume@ubuntu:~/\$', html_content)

    # Create a directory named "mains"
    os.makedirs("mains", exist_ok=True)

    for i, code_match in enumerate(code_coordination, start=1):
        # Save odd code snippets to separate files
        if i % 2 == 1:
            code_match = code_match.strip()

            # Replace instances of &quot;&quot;&quot; with three double quotations
            code_match = code_match.replace('&quot;&quot;&quot;', '"""')

            # Extract the filename based on "-main" and the number before it
            filename_match = re.search(r'(\d+)-main', code_match)
            if filename_match:
                filename = f"mains/{filename_match.group(1)}-main.py"  # Set the filename
                with open(filename, 'w') as file:
                    # Replace common HTML entities with characters
                    cleaned_code = replace_html_entities(code_match)
                    file.write(cleaned_code)
                print(f"Code snippet {i} saved to {filename}")
            else:
                print(f"Filename not found in code snippet {i}, skipping.")
        else:
            # You can skip even code snippets by not processing them
            print(f"Skipping code snippet {i}")


if __name__ == "__main__":
    login_and_scrape()
