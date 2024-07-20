import argparse
import os
import shutil
import logging
import time

# Function to parse command line arguments
def parse_arguments():
    parser = argparse.ArgumentParser(description="Synchronize two folders.")
    parser.add_argument('source', type=str, help='Path to the source folder')
    parser.add_argument('replica', type=str, help='Path to the replica folder')
    parser.add_argument('interval', type=int, help='Synchronization interval in seconds')
    parser.add_argument('log_file', type=str, help='Path to the log file')
    return parser.parse_args()

# Function to synchronize the source and replica folders
def sync_folders(source, replica, enable_logging=True):
    # Loop through items in the source folder
    for item in os.listdir(source):
        source_item = os.path.join(source, item)
        replica_item = os.path.join(replica, item)

        if os.path.isdir(source_item):
            # If the item is a directory and doesn't exist in the replica, create it
            if not os.path.exists(replica_item):
                os.makedirs(replica_item)
                logging.info(f'Created directory: {replica_item}')
            # Recursively sync the sub-directory
            sync_folders(source_item, replica_item, enable_logging)
        else:
            # If the item is a file and it's new or modified, copy it
            if not os.path.exists(replica_item) or os.path.getmtime(source_item) > os.path.getmtime(replica_item):
                shutil.copy2(source_item, replica_item) # Using copy2 to preserve all file metadata from the original
                logging.info(f'Copied file: {source_item} to {replica_item}')

    # Loop through items in the replica folder to remove deleted items
    for item in os.listdir(replica):
        replica_item = os.path.join(replica, item)
        source_item = os.path.join(source, item)

        if not os.path.exists(source_item):
            # Remove directories and files that are no longer in the source
            if os.path.isdir(replica_item):
                shutil.rmtree(replica_item)
                logging.info(f'Removed directory: {replica_item}')
            else:
                os.remove(replica_item)
                logging.info(f'Removed file: {replica_item}')

# Main function to set up logging and start the synchronization process
def main():
    args = parse_arguments()

    # Ensure the replica directory exists
    if not os.path.exists(args.replica):
        os.makedirs(args.replica)

    # Set up logging to file and console
    logging.basicConfig(filename=args.log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logging.getLogger().addHandler(console)

    while True:
        try:
            sync_folders(args.source, args.replica)
        except Exception as e:
            logging.error(f'Error during synchronization: {e}')
        time.sleep(args.interval)

# Ensure the main function runs when the script is executed directly
if __name__ == "__main__":
    main()
