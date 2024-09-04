#!/bin/bash

# Define variables
LOG_FILE="pip_install.log"
PYTHON_PATH="/usr/bin/python3"
VENV_DIR="django_venv"
REQUIREMENTS_FILE="requirements.txt"

# Check if the virtual environment already exists
if [ -d "$VENV_DIR" ]; then
    echo "The virtual environment '$VENV_DIR' already exists."
else
    echo "Creating the virtual environment '$VENV_DIR'..."
    $PYTHON_PATH -m venv $VENV_DIR
    if [ $? -ne 0 ]; then
        echo "Error: Failed to create the virtual environment." >&2
        exit 1
    fi
fi

# Activate the virtual environment
if [ -f "$VENV_DIR/bin/activate" ]; then
    echo "Activating the virtual environment..."
    source $VENV_DIR/bin/activate
else
    echo "Error: 'activate' file not found in '$VENV_DIR/bin'." >&2
    exit 1
fi

# Show pip version
echo "Pip version:"
python -m pip --version

# Create requirements.txt file if it does not exist
if [ ! -f "$REQUIREMENTS_FILE" ]; then
    echo "squery" > $REQUIREMENTS_FILE
    echo "File '$REQUIREMENTS_FILE' created with content 'squery'."
else
    echo "The file '$REQUIREMENTS_FILE' already exists."
fi

# Install packages using pip
echo "Installing packages from $REQUIREMENTS_FILE..."
python -m pip install --log $LOG_FILE --force-reinstall -r $REQUIREMENTS_FILE
if [ $? -ne 0 ]; then
    echo "Error: Package installation failed." >&2
    exit 1
fi

echo "Installation completed successfully. Check the log file '$LOG_FILE' for details."

