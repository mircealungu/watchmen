#!/usr/bin/env bash
# Run this script to setup your development environment.

TOP=$(cd $(dirname $0) && pwd -L)

if [ "$(id -u)" == "0" ]; then
   echo "This script should not be run as root. " 1>&2
   exit 1
fi

echo "Hello developer! Let's get you setup! :)"

# Required packages.
read -p "Install dependencies with apt? Will need root priviliges." -n 1 -r
echo    # move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "Apt-get installing..."
    sudo apt-get install -y \
    python3.6 \
    python3.6-dev \
    python-virtualenv \
    virtualenvwrapper
else
    echo "Skipping apt-get install."
fi

# create virtualenv, consistent with virtualenv-wrapper conventions
echo "Setting up virtual environment..."
if [ -z ${WATCHMEN_VENV_ROOT+x} ]
then
    WATCHMEN_VENV_ROOT="$HOME/.virtualenvs/watchmen"
    echo "WATCHMEN_VENV_ROOT not set, using default ($WATCHMEN_VENV_ROOT)." 
fi

if [ ! -d ${WATCHMEN_VENV_ROOT} ]; then
    mkdir -p $(dirname ${WATCHMEN_VENV_ROOT})
    virtualenv -p python3.6 ${WATCHMEN_VENV_ROOT}
fi
source ${WATCHMEN_VENV_ROOT}/bin/activate
cd "${TOP}"

# install requirements
pip install -r requirements.txt 

echo "Done!"
