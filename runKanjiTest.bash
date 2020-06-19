#!/bin/bash

gsettings set org.gnome.desktop.interface text-scaling-factor 1.8

python3.8 ./KanjiTest.py

gsettings reset org.gnome.desktop.interface text-scaling-factor

