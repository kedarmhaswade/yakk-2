#!/bin/zsh
# run it as ./semiprimes.sh 1kp.txt | sort | uniq |sort -n > 500500sm.txt
file_contents=$(<$1)
xs=("${(@f)file_contents}")
for i in "${xs[@]}"; do
    for j in "${xs[@]}"; do
        echo $((i*j))
    done
done
