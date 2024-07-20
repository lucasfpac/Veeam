# Folder Synchronization Project

This project is a solution for synchronizing two folders: `source` and `replica`. The goal is to maintain a full, identical copy of the `source` folder at the `replica` folder. This project was developed as part of an interview test for a Internal Development in QA (SDET) position.

## Features

- One-way synchronization from `source` to `replica`
- Periodic synchronization based on a specified interval
- Logging of file creation, copying, and removal operations
- Customizable folder paths, synchronization interval, and log file path via command-line arguments

## Project Structure

```
folder_sync_project/
├── data/
│ ├── source/
│ └── replica/
├── logs/
│ └── sync.log
├── src/
│ └── sync.py
├── tests/
│ └── test_sync.py
├── venv/
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.x
- Git

### Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/lucasfpac/Veeam.git
   cd Veeam
   ```

2. **Create and activate a virtual environment (optional but recommended):**

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

### Usage

To run the synchronization script, use the following command:

```sh
python src/sync.py data/source data/replica 30 logs/sync.log
```

**Arguments:**

- `data/source`: Path to the source folder
- `data/replica`: Path to the replica folder
- `30`: Synchronization interval in seconds (e.g., 30 seconds)
- `logs/sync.log`: Path to the log file

**Example:**

```sh
python src/sync.py data/source data/replica 30 logs/sync.log
```

This command will synchronize the contents of `data/source` to `data/replica` every 30 seconds and log the operations to `logs/sync.log`.

## Running Tests

To run the tests, use the following command:

```sh
pytest
```

**Test Coverage:**

- Test file creation: Ensures new files in the source folder are copied to the replica folder.
- Test file modification: Ensures modified files in the source folder are updated in the replica folder.
- Test file deletion: Ensures deleted files in the source folder are removed from the replica folder.
- Test directory creation: Ensures new directories in the source folder are created in the replica folder.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.