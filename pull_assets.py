import requests
import zipfile
import os
import shutil

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'OAuth y0_AgAAAABmPWC4AAuz6gAAAAEDVKwNAABrfytHFFhFM6f6Mw-7rPfJDVvBjw'
}

res = requests.get(requests.get('https://cloud-api.yandex.net/v1/disk/resources/download?path=00000',
                                headers=headers).json()['href'], stream=True)
if res.ok:
    shutil.rmtree('Content/Assets/', True)

    os.makedirs('Temp/')

    with open('Temp/00000.zip', 'wb') as f:
        for chunk in res.iter_content(chunk_size=1024 * 8):
            if chunk:
                f.write(chunk)
                f.flush()
                os.fsync(f.fileno())

    with zipfile.ZipFile('Temp/00000.zip', 'r') as zip_ref:
        zip_ref.extractall('Temp/')

    shutil.move('Temp/00000/', 'Content/Assets/')

    shutil.rmtree('Temp/')