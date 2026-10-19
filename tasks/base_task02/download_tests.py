import gdown
import zipfile
import os


def download(url: str, compressed_pth: str):
    if os.path.exists(compressed_pth):
        ans = input(f"File {compressed_pth} already exists. Download it again? [y\\n]").strip().lower()
        if ans != 'y':
            return
    
    gdown.download(url, output=compressed_pth, fuzzy=True)


def extract(compressed_pth: str, extracted_pth: str):
    print(f"Extracting to {extracted_pth}")
    with zipfile.ZipFile(compressed_pth, 'r') as zf:
        zf.extractall(extracted_pth)


def delete_compressed(compressed_pth: str):
    os.remove(compressed_pth)


def main():
    url = 'https://drive.google.com/file/d/17XbVfqIw20sKtXVvfXI2NI6KH438knQJ/view?usp=drive_link'
    compressed_pth = './public_tests.zip'
    extracted_pth = './'
    
    download(url, compressed_pth)
    extract(compressed_pth, extracted_pth)
    delete_compressed(compressed_pth)


if __name__ == '__main__':
    main()
