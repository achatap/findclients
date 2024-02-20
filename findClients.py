import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def extract_external_links(url, output_file):
    try:
        # Define custom headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        
        # Send a GET request to the URL with custom headers
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the webpage
            soup = BeautifulSoup(response.content, 'html.parser')
            # Find all <a> tags (links) in the HTML
            links = soup.find_all('a')
            # Extract and write the external URLs to the output file
            with open(output_file, 'a') as file:
                for link in links:
                    href = link.get('href')
                    if href and not href.startswith('#'):
                        parsed_url = urlparse(href)
                        if parsed_url.netloc and parsed_url.netloc != urlparse(url).netloc:
                            file.write(href + '\n')
        else:
            print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Read URLs from posts.txt and extract external links from each article
output_file = 'links.txt'
with open('posts.txt', 'r') as file:
    urls = file.readlines()
    for url in urls:
        print(f"Extracting external links from: {url.strip()}")
        extract_external_links(url.strip(), output_file)
