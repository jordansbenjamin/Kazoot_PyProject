#!/bin/bash

# Check python version and existence
check_python(){
    if ! [[ -x "$(command -v python3)" ]]; then
        echo "Error: 
            To start Kazoot, Python 3 is required and it looks like you don't have it installed.
            Please install the latest version of Python 3, you can do so by checking out: https://www.python.org/downloads/installing-python/" >&2
        exit 1
    fi
}

# Creates virtual environment
create_virtual_venv(){
    python3 -m venv $1
}

# Activates virtual environment
activate_virtual_venv(){
    source $1/bin/activate
}

# Upgrades to the latest version of pip
upgrade_pip(){
    pip install --upgrade pip
}

# Install requirements and dependencies
install_requirements(){
    pip install -r $1  
}

# Main execution of bash script
echo "Welcome! Let's get you setup to start Kazoot!"

sleep 2

clear

check_python

create_virtual_venv .venv

activate_virtual_venv .venv
echo "Virtual environment created and activated!"

sleep 2

upgrade_pip

clear

install_requirements requirements.txt

clear

echo "Requirements and dependencies installed!"

sleep 2

clear

echo "Setup complete! Virtual environment initialised, dependencies installed, to start playing Kazoot, run: ./run_kazoot.sh"