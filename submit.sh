#!/bin/sh
#BSUB -J ch_book
#BSUB -o plain_%J.out
#BSUB -e plain_%J.err
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=1G]"
#BSUB -R "span[hosts=1]"
#BSUB -u jonpo@dtu.dk
#BSUB -N
#BSUB -W 24:00
# end of BSUB options

# activate the virtual environment 
source chess-env/bin/activate

python ScriptImplementation/main.py
