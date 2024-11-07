import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse
import re
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def print_banner():
    # Corrected raw string for banner
    banner = r"""
{0}                       /$$$$$$$          
                      | $$__  $$         
              /$$$$$$ | $$  \ $$ /$$$$$$ 
             /$$__  $$| $$$$$$$//$$__  $$
            | $$  \ $$| $$____/| $$  \ $$
            | $$  | $$| $$     | $$  | $$
            |  $$$$$$/| $$     |  $$$$$$/
             \______/ |__/      \______/ 

    {1}https://github.com/briocheeee
    """.format(Fore.BLUE, Fore.WHITE)
    print(banner)

def download_file(file_url, folder):
    filename = file_url.split('/')[-1]
    filepath = os.path.join(folder, filename)
    try:
        file_response = requests.get(file_url)
        if file_response.status_code == 200:
            with open(filepath, 'wb') as f:
                f.write(file_response.content)
            print(f"{Fore.BLUE}Downloaded: {filename}")
            return filepath
        else:
            print(f"{Fore.RED}Unable to download {file_url} - Error code {file_response.status_code}")
        return None
    except Exception as e:
        print(f"{Fore.RED}Error downloading {file_url}: {e}")
        return None

def download_html(url, folder):
    response = requests.get(url)
    if response.status_code == 200:
        html_path = os.path.join(folder, 'index.html')
        with open(html_path, 'w', encoding='utf-8') as file:
            file.write(response.text)
        return response.text
    else:
        print(f"{Fore.RED}Error downloading {url} - Error code {response.status_code}")
        return None

def download_all_links(soup, base_url, folder):
    all_links = set()
    for a_tag in soup.find_all('a', href=True):
        link = urljoin(base_url, a_tag['href'])
        if link not in all_links and base_url in link:
            all_links.add(link)
            download_html(link, folder)

# Print the banner
print_banner()

# Custom intro with website URL
url = input(f"{Fore.BLUE}╔═══[Website URL] \n╚══> {Fore.WHITE}")

base_folder = r"C:\you folder

domain_name = urlparse(url).netloc
clean_name = re.sub(r'[^\w\-_\. ]', '_', domain_name)
destination_folder = os.path.join(base_folder, clean_name)
os.makedirs(destination_folder, exist_ok=True)

try:
    html_content = download_html(url, destination_folder)
    
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')

        for link in soup.find_all('link', {'rel': 'stylesheet'}):
            css_url = urljoin(url, link['href'])
            download_file(css_url, destination_folder)

        for script in soup.find_all('script', src=True):
            js_url = urljoin(url, script['src'])
            download_file(js_url, destination_folder)

        for img in soup.find_all('img', src=True):
            img_url = urljoin(url, img['src'])
            download_file(img_url, destination_folder)

        for form in soup.find_all('form', action=True):
            action_url = urljoin(url, form['action'])
            if action_url.endswith(".php") or action_url.endswith(".pdf") or urlparse(action_url).path:
                download_file(action_url, destination_folder)

        download_all_links(soup, url, destination_folder)

        for a_tag in soup.find_all('a', href=True):
            file_url = urljoin(url, a_tag['href'])
            new_link = os.path.join(destination_folder, file_url.split('/')[-1])
            a_tag['href'] = new_link.replace("\\", "/")

        for form in soup.find_all('form', action=True):
            form_url = urljoin(url, form['action'])
            new_action = os.path.join(destination_folder, form_url.split('/')[-1])
            form['action'] = new_action.replace("\\", "/")

        updated_html_path = os.path.join(destination_folder, 'index.html')
        with open(updated_html_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))

        print(f"{Fore.GREEN}Download complete. The files are in the folder: {destination_folder}")
    else:
        print(f"{Fore.RED}Error downloading the HTML page.")
except requests.exceptions.RequestException as e:
    print(f"{Fore.RED}Error accessing the URL: {e}")
