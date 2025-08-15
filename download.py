import requests

def download_image(image_url, save_path):
    """
    Downloads an image from a given URL and saves it to a specified path.
    Args:
        image_url (str): The URL of the image to download.
        save_path (str): The local path where the image will be saved.
    """
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        print(f"Image successfully downloaded to: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")