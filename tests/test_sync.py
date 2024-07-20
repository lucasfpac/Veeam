import sys
import os

# Add the src directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import pytest
from sync import sync_folders

# Fixture to set up a temporary test environment
@pytest.fixture
def setup_test_environment(tmp_path):
    # Create temporary source and replica directories
    source = tmp_path / "source"
    replica = tmp_path / "replica"
    os.makedirs(source)
    os.makedirs(replica)
    return source, replica

# Test case to check if new files are created in the replica folder
def test_create_new_files(setup_test_environment):
    # Set up test environment
    source, replica = setup_test_environment
    test_file = source / "test_file.txt"

    # Create a new file in the source folder
    with open(test_file, "w") as f:
        f.write("Hello, World!")

    # Synchronize the folders
    sync_folders(source, replica, enable_logging=False)

    # Check if the file was created in the replica folder
    assert os.path.exists(replica / "test_file.txt")

# Test case to check if modified files are copied to the replica folder
def test_copy_modified_files(setup_test_environment):
    # Set up test environment
    source, replica = setup_test_environment
    test_file = source / "test_file.txt"
    replica_file = replica / "test_file.txt"

    # Create a file in the source folder
    with open(test_file, "w") as f:
        f.write("Hello, World!")

    # Synchronize the folders
    sync_folders(source, replica, enable_logging=False)

    # Modify the file in the source folder
    with open(test_file, "w") as f:
        f.write("Hello, Python!")

    # Synchronize the folders again
    sync_folders(source, replica, enable_logging=False)

    # Check if the modification is reflected in the replica folder
    with open(replica_file, "r") as f:
        content = f.read()

    assert content == "Hello, Python!"

# Test case to check if deleted files are removed from the replica folder
def test_remove_deleted_files(setup_test_environment):
    # Set up test environment
    source, replica = setup_test_environment
    test_file = source / "test_file.txt"

    # Create a file in the source folder
    with open(test_file, "w") as f:
        f.write("Hello, World!")

    # Synchronize the folders
    sync_folders(source, replica, enable_logging=False)

    # Delete the file in the source folder
    os.remove(test_file)

    # Synchronize the folders again
    sync_folders(source, replica, enable_logging=False)

    # Check if the file is removed from the replica folder
    assert not os.path.exists(replica / "test_file.txt")

# Test case to check if new directories are created in the replica folder
def test_create_new_directories(setup_test_environment):
    # Set up test environment
    source, replica = setup_test_environment
    new_dir = source / "new_dir"

    # Create a new directory in the source folder
    os.makedirs(new_dir)

    # Synchronize the folders
    sync_folders(source, replica, enable_logging=False)

    # Check if the directory was created in the replica folder
    assert os.path.exists(replica / "new_dir")
