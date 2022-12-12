#!/bin/bash

# —---------------------------------------------------—
# venv and requirements
# —---------------------------------------------------—
setup(){
  which poetry
  if [[ $? -ne 0 ]]; then
    read -r -p "Enter your python3 alias to execute commands with (>=python3.9): " pylink
    sudo apt install "$pylink"-venv
    curl https://install.python-poetry.org | $pylink -
  fi
  poetry install
  poetry run pre-commit install
}

setup
