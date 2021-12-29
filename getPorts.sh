#!/bin/bash
filename=$1
info=$(cat $filename | grep 'Ports:' | tr '\t' '\n' | tr -d '()' | tr '/' ' ' | tr ':,' '\n')
ports=$(echo "$info" | sed '1,3d' | awk '{print $1}' | tr '\n', ',' | tr -d ' ')
ports=${ports::-1} 

echo "$info"


if [[ $OSTYPE == 'darwin'* ]]; then
        echo -n "$ports" | pbcopy

else
	echo -n "$ports" | xclip -selection clipboard
fi
