from .datasets.raw_data import load_raw_data
from .datasets.processed_data import load_processed_data
from .datasets.obfuscated_data import load_obfuscated_data
import os
import shutil
import urllib.request
import zipfile

__all__ = ['download_and_extract_data']


def download_and_extract_data():
    # URL of GitHub release zip file
    url = "https://github.com/Blood-Glucose-Control/t1d-change-point-detection-benchmark/archive/refs/tags/v0.1.0.zip"

    # Get the package installation directory
    package_dir = os.path.dirname(__file__)

    zip_path = os.path.join(package_dir, 'temp.zip')
    try:
        print("Downloading data files... May take a while...")
        urllib.request.urlretrieve(url, zip_path)

        print("Extracting data files...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            # Extract to a temporary directory first
            temp_dir = os.path.join(package_dir, 'temp_extract')
            os.makedirs(temp_dir, exist_ok=True)
            zip_ref.extractall(temp_dir)

            source_data_dir = os.path.join(
                temp_dir, 't1d-change-point-detection-benchmark-0.1.0', 't1d_cpd_benchmark', 'data')

            data_dir = os.path.join(package_dir, 'data')
            if os.path.exists(data_dir):
                shutil.rmtree(data_dir)

            shutil.move(source_data_dir, package_dir)
            shutil.rmtree(temp_dir)

        # Clean up
        os.remove(zip_path)
        print("Data files successfully downloaded and extracted!")
        return True
    except Exception as e:
        print(f"Error downloading data: {e}")
        return False


# Check if data directory exists, if not, try to download it
data_dir = os.path.join(os.path.dirname(__file__), 'data')
if not os.path.exists(data_dir):
    download_and_extract_data()
