from kaggle.api.kaggle_api_extended import KaggleApi
from pathlib import Path
import shutil
import os

delete_zip = True

api = KaggleApi()
competition = 'house-prices-advanced-regression-techniques'
path = Path(__file__).parent.parent / "data/raw"

path.mkdir(parents=True, exist_ok=True)


api.competition_download_files(competition, path=path, quiet=False)
print(f"Files successfully downloaded to {path}")


shutil.unpack_archive(path / f"{competition}.zip", path)
print(f"Files successfully extracted to {path}")

if delete_zip:
    os.remove(path / f"{competition}.zip")
    print("ZIP file deleted successfully")