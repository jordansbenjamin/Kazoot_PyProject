#!/bin/bash

check_python(){
    if ! [[ -x "$(command -v python3)" ]]; then
        echo "Error: 
            To play Kazoot, Python 3 is required and it looks like you don't have it installed.
            Please install the latest version of Python 3, you can do so by checking out: https://www.python.org/downloads/installing-python/" >&2
        exit 1
    fi
}

check_venv_exists(){
    if ! [[ -d ".venv" ]]; then
        echo "Error:
            Virtual environment does not exist, please create a virtual environment by running: ./setup_kazoot.sh"
        exit 1
    fi
}

check_active_venv(){
    if [[ -n "$VIRTUAL_ENV" ]]; then
        clear
        python3 main.py
    else
        echo "Virtual environment was not active, activating now..."

        source .venv/bin/activate
        clear
        python3 main.py
    fi
}

# Main execution of bash script
check_python
check_venv_exists
check_active_venv