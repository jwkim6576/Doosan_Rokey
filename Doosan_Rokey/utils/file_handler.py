# utils/file_handler.py
import os
import shutil
from datetime import datetime

SAVE_DIR = "./uploads"
os.makedirs(SAVE_DIR, exist_ok=True)

def save_image(original_path: str) -> str:
    """
    사용자가 업로드한 이미지를 uploads 폴더로 복사하고 경로 반환
    """
    filename = os.path.basename(original_path)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    new_filename = f"{timestamp}_{filename}"
    new_path = os.path.join(SAVE_DIR, new_filename)
    shutil.copyfile(original_path, new_path)
    return new_path
