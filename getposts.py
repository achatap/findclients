import requests
from bs4 import BeautifulSoup

def extract_urls_from_page(url, output_file):
    try:
        # Define custom headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        
        # Send a GET request to the URL with custom headers
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the XML content of the webpage using lxml parser
            soup = BeautifulSoup(response.content, 'lxml')
            # Find all <loc> tags in the XML (URLs)
            urls = soup.find_all('loc')
            # Extract and write the URLs to the output file
            with open(output_file, 'a') as file:
                for url in urls:
                    file.write(url.text + '\n')
        else:
            print(f"Failed to retrieve content from {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Read URLs from output.txt and extract URLs from each page
output_file = 'posts.txt'
with open('output.txt', 'r') as file:
    urls = file.readlines()
    for url in urls:
        print(f"Extracting URLs from: {url.strip()}")
        extract_urls_from_page(url.strip(), output_file)
