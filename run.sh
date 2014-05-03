#!/bin/bash

num_vars=$#

if [ $num_vars -eq 0 ]

then
	python src/main.py

else
	python src/main.py $@
	
fi