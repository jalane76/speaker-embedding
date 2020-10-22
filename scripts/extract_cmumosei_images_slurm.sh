#!/bin/bash

# Copy/paste this job script into a text file and submit with the command:
#    sbatch thefilename
# job standard output will go to the file slurm-%j.out (where %j is the job ID)

#SBATCH --time=100:00:00   # walltime limit (HH:MM:SS)
#SBATCH --nodes=1   # number of nodes
#SBATCH --ntasks-per-node=16   # 48 processor core(s) per node 
#SBATCH --mem=128G   # maximum memory per node
#SBATCH --mail-user=jalane@iastate.edu   # email address
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END
#SBATCH --mail-type=FAIL

# LOAD MODULES, INSERT CODE, AND RUN YOUR PROGRAMS HERE
module load singularity
singularity exec --nv \
    --bind /home/jalane/git/speaker-embedding:/workspace \
    --bind /data/Jesse:/data \
    /data/Jesse/singularity-images/speaker-embeddings_latest.sif \
    /workspace/extract-images.py \
    /data/cmumosei/Raw/Videos/Segmented/Combined/ \
    /data/cmumosei/Raw/Images/Segmented/Combined/