#!/bin/sh

python3.10 -m venv django_venv

source ./django_venv/bin/activate || . ./django_venv/bin/activate

python3.10 -m pip install --upgrade pip

pip3 install -r requirement.txt
