#!/bin/bash

count=1
while [ $count -le 16 ]
do
    python new_patient.py
    count=$(( $count + 1 ))
done
