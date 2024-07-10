import os
import zipfile

def create_dummy_files(directory):
    os.makedirs(directory, exist_ok=True)
    for i in range(5):
        with open(os.path.join(directory, f'dummy_file_{i}.txt'), 'w') as f:
            f.write('This is a dummy file...\n')

def zip_directory(directory, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                zipf.write(os.path.join(root, file), 
                           os.path.relpath(os.path.join(root, file), 
                           os.path.join(directory, '...')))

if __name__ == "__main__":
    dummy_dir = 'dummy_files'
    zip_file = 'dummy_files.zip'
    create_dummy_files(dummy_dir)
    zip_directory(dummy_dir, zip_file)

