#!/usr/bin/env bash
# Run this script to test the library on you machine.

if [ -z ${WATCHMEN_VENV_ROOT+x} ]
then
    WATCHMEN_VENV_ROOT="$HOME/.virtualenvs/watchmen"
    echo "WATCHMEN_VENV_ROOT not set, using default ($WATCHMEN_VENV_ROOT)." 
fi

source ${WATCHMEN_VENV_ROOT}/bin/activate
pytest -v -s
