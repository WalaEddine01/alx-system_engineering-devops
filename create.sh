#!/bin/bash

# Check if filename was provided
if [ $# -eq 0 ]; then
    echo "Error: Please provide a filename"
    echo "Usage: $0 <filename>"
    exit 1
fi

filename=$1

# Create the file with shebang line
echo "#!/usr/bin/bash" > "$filename"

# Make the file executable
chmod +x "$filename"

# Print confirmation
echo "Created executable bash file: $filename"