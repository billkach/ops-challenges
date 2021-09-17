#!/bin/bash

sudo wget http://archive.ubuntu.com/ubuntu/pool/universe/p/pygtk/python-gtk2_2.24.0-5.1ubuntu2_amd64.deb
sudo wget http://azure.archive.ubuntu.com/ubuntu/pool/universe/p/pygobject-2/python-gobject-2_2.28.6-14ubuntu1_amd64.deb
sudo wget http://security.ubuntu.com/ubuntu/pool/universe/p/pycairo/python-cairo_1.16.2-2ubuntu2_amd64.deb
sudo dpkg -i python-gobject-2_2.28.6-14ubuntu1_amd64.deb
sudo dpkg -i python-cairo_1.16.2-2ubuntu2_amd64.deb
sudo dpkg -i python-gtk2_2.24.0-5.1ubuntu2_amd64.deb
