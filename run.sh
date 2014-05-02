#!/bin/bash

num_vars=$#

if [ $num_vars -eq 0 ]

then
	python Main.py

else
	python Main.py $@
	
fi