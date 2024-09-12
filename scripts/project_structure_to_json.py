import os
import json

def folder_to_dict(path):
    folder_dict = {"name": os.path.basename(path), "type": "folder", "children": []}
    
    try:
        for entry in os.scandir(path):
            if entry.is_dir():
                folder_dict["children"].append(folder_to_dict(entry.path))
            else:
                folder_dict["children"].append({"name": entry.name, "type": "file"})
    except PermissionError:
        # If the folder cannot be accessed due to permission issues
        pass
    
    return folder_dict

def export_folder_structure_to_json(root_folder, output_file):
    folder_structure = folder_to_dict(root_folder)
    
    with open(output_file, 'w') as f:
        json.dump(folder_structure, f, indent=4)

if __name__ == "__main__":
    root_folder = input("Enter the root folder path: ")
    output_file = input("Enter the output file path (e.g., folder_structure.json): ")
    export_folder_structure_to_json(root_folder, output_file)
    print(f"Folder structure exported to {output_file}")