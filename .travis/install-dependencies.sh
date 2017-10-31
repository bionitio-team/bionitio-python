#!/bin/sh

# Install Python dependencies

echo 'Python install'
(
   pip install pylint
   pip install .
  
)
