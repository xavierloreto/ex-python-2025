def main():
    # Ask the user for the file name
    file_name = input("file name: ").strip().lower()

    # Dictionary that maps file extensions to MIME types
    mime_types = {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "gif": "image/gif",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip", 
    }

    # Extract the file extension from the user's input
    # Split the file name by "." and get the last value of the list
    file_extension = file_name.split(".")[-1]

    # Check if the file extension is in the dictionary
    if file_extension in mime_types:
        print(mime_types[file_extension])
    # Print generic type for unknown files
    else:
        print("application/octet-stream")

# Start the program
if __name__ == "__main__":
    main()
