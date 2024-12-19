#! /bin/bash -login

#SBATCH -D /group/ctbrowngrp4/2024-ccbaumler-crc/manual-run # Working directory for the job
#SBATCH -o ./logs/prep.%j.out              # Standard output file
#SBATCH -e ./logs/prep.%j.err              # Standard error file
#SBATCH -p bmh                              # Partition to submit to
#SBATCH -J fastq-grab                       # Job name
#SBATCH -t 2-00:00:00                       # Time limit (7 days and 0 hours)
#SBATCH -N 1                                # Number of nodes
#SBATCH -n 1                                # Number of tasks
#SBATCH -c 16                               # Number of CPU cores per task
#SBATCH --mem=124G                           # Memory per node
#SBATCH --mail-type=ALL                     # Send email on all job events
#SBATCH --mail-user=ccbaumler@ucdavis.edu   # Email address for notifications

# Fail on weird errors
set -e
set -x

# Load necessary modules or activate environments if needed
# module load ncdu (if ncdu is a module)

# Initialize conda if needed
conda_base=$(conda info --base)
. ${conda_base}/etc/profile.d/conda.sh

# Activate relevant environment if needed
#conda activate sra-tools
#conda activate sourmash
conda activate branchwater

#echo "" > logs/sig-summary.txt

#for id in $( awk -F, 'NR>1 {print $1}' sample-metadata.csv ); do
#    echo "prefetch $id"
#    prefetch $id
#
#    echo "dumping $id"
#    fasterq-dump $id --outdir fastq

#    sourmash sketch dna fastq/"$id"_1.fastq fastq/"$id"_2.fastq --name "$id" -p scaled=1000,k=21,k=31,k=51,abund -o sig/"$id".zip

#    sourmash sig summarize sig/"id".zip >> logs/sig-summary.txt

#done

#find /group/ctbrowngrp4/2024-ccbaumler-crc/manual-run/sig/* -type f > pathlist.txt

#sourmash sig collect pathlist.txt -o summary-manifest.csv -F csv
cd prefetch_gather

#sourmash scripts fastmultigather ../summary-manifest.csv ../../../2024-ccbaumler-gtdb/gtdb-220/gtdb-rs220-k31.zip --cores 6 --save-matches

sourmash scripts manysearch ../../../2024-ccbaumler-gtdb/gtdb-220/gtdb-rs220-k31.zip ../summary-manifest.csv -o many-search.results.csv
sourmash scripts manysearch ../../../2024-ccbaumler-gtdb/gtdb-220/gtdb-rs220-k31.zip ../summary-manifest.csv -N -o many-search.results.not-pretty.csv
