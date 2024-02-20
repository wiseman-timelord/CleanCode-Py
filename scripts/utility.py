# Script: utility.py

# other functions/imports need adjusting for this function to be in utility.
def determine_type(filename):
    """Determines the script type based on the file extension."""
    file_extension = os.path.splitext(filename)[1].lower()
    return FILE_EXTENSION_TO_TYPE_MAP.get(file_extension, "Unknown")