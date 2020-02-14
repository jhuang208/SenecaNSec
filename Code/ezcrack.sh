#!/bin/bash
if [ -z "$1" ] && [ -z "$2" ]; then
	echo "Please put the passwd and shadow file as arguments."
	exit
fi
unshadow $1 $2 > passwdshadow
john passwdshadow
rm passwdshadow
