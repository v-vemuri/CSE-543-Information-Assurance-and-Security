#!/bin/bash

if [[ -z $1 ]];
then
     echo "Please provide the program number that needs to be fuzzed"
     exit 123
else
     echo "Fuzzing ./prog_$1"    
fi

echo "RANDOM=$RANDOM"
prng_seed=$RANDOM
echo "Using $prng_seed as PRNG seed"

for i in {1..20000}; do
        echo "i=$i"
        echo "prng_seed=$prng_seed, iter=$i\r"
        python3 fuzzer.py "$prng_seed" "$i" -0 | ./prog_$1 2>/dev/null || {
		status=$?
                if [ "$status" -eq 139 ]; then
                       echo "status=$status"
                       break
                fi
        }
done
echo "Done with all the iterations"
