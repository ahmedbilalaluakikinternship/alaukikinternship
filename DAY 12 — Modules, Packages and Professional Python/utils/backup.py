import shutil

from config import EMPLOYEE_FILE, TASK_FILE, DATA_DIR, BASE_DIR
from utils.logger import logger


BACKUP_DIR = BASE_DIR / "backup"


def create_backup():

    BACKUP_DIR.mkdir(exist_ok=True)

    files = [EMPLOYEE_FILE, TASK_FILE]

    for file in files:

        if file.exists():
            shutil.copy2(file, BACKUP_DIR / file.name)

    logger.info("Data backup created.")

    print("Backup created successfully!")


def restore_backup():

    if not BACKUP_DIR.exists():
        print("Backup folder not found.")
        return

    restored = False

    for file_name in ["employees.json", "tasks.json"]:

        backup_file = BACKUP_DIR / file_name
        original_file = DATA_DIR / file_name

        if backup_file.exists():
            shutil.copy2(backup_file, original_file)
            restored = True

    if restored:
        logger.info("Data restored from backup.")
        print("Backup restored successfully!")
    else:
        print("No backup files found.")