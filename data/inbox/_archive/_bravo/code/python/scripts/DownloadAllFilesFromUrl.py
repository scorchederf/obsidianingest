import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def download_files(url, save_dir):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Create a directory if it doesn't exist
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Iterate through all links
    for link in soup.find_all('a'):
        href = link.get('href')
        if href:
            # Construct absolute URL
            absolute_url = urljoin(url, href)
            
            # Get filename from the URL
            filename = os.path.basename(urlparse(absolute_url).path)
            
            # If the link points to a file, download it
            if '.' in filename:
                filepath = os.path.join(save_dir, filename)
                print("Downloading", filename)
                with open(filepath, 'wb') as f:
                    f.write(requests.get(absolute_url).content)
            # If the link points to a directory, recursively download its contents
            else:
                subdir = os.path.join(save_dir, filename)
                download_files(absolute_url, subdir)

if __name__ == "__main__":
    url = "http://192.168.125.131:8000/"      # input("Enter the URL to download from: ")
    save_dir = "c:\\temp\\"                                 # input("Enter the directory to save files: ")
    download_files(url, save_dir)
    print("Download completed.")