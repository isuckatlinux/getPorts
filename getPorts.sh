#!/bin/bash

if [ "$#" -ne 1 ]; then
	echo "Illegal number of parameters, you only have to give the name of the grepeable file"
	exit -1
fi

filename=$1

if [ ! -f "$filename" ]; then
	echo "$filename not exist."
	exit -1
fi


info=$(cat $filename | grep 'Ports:' | tr '\t' '\n' | tr -d '()' | tr '/' ' ' | tr ':,' '\n')
ports=$(echo "$info" | sed '1,3d' | awk '{print $1}' | tr '\n', ',' | tr -d ' ')
ports=${ports::-1} 

echo "$info"


if [[ $OSTYPE == 'darwin'* ]]; then
        echo -n "$ports" | pbcopy

else
	echo -n "$ports" | xclip -selection clipboard
fi
