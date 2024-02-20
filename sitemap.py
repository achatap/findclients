import requests
from bs4 import BeautifulSoup
import sys

def extract_urls_from_sitemap(sitemap_url):
    try:
        # Define custom headers
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        
        # Send a GET request to the sitemap URL with custom headers
        response = requests.get(sitemap_url, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the XML content of the sitemap
            soup = BeautifulSoup(response.content, 'xml')
            # Find all <loc> tags in the XML (URLs)
            urls = soup.find_all('loc')
            # Extract and store the URLs in a list
            url_list = [url.text for url in urls]
            # Write the URLs to a text file
            with open('output.txt', 'w') as file:
                for url in url_list:
                    file.write(url + '\n')
            print("URLs extracted and stored in output.txt")
        else:
            print(f"Failed to retrieve content from {sitemap_url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 sitemap.py <sitemap_url>")
        sys.exit(1)
    sitemap_url = sys.argv[1]
    extract_urls_from_sitemap(sitemap_url)
