from pathlib import Path

# Main project directory
BASE_DIR = Path(__file__).parent

# Data and log directories
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

# JSON files
EMPLOYEE_FILE = DATA_DIR / "employees.json"
TASK_FILE = DATA_DIR / "tasks.json"

# Log file
LOG_FILE = LOG_DIR / "app.log"

# Create folders automatically
DATA_DIR.mkdir(exist_ok=True)
LOG_DIR.mkdir(exist_ok=True)

# Application details
APP_NAME = "Employee & Task Management System"
APP_VERSION = "1.0.0"