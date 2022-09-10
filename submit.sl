#!/bin/bash -e
#SBATCH --mail-user=ecar239@aucklanduni.ac.nz
#SBATCH --mail-type=FAIL,END
#SBATCH -J GaEnergy 
#SBATCH -A uoa02731         # Project Account
#SBATCH --time=00:30:00     # Walltime
#SBATCH --ntasks=40
#SBATCH --mem-per-cpu=1500
#SBATCH --hint=nomultithread #no hyperthreading 
#SBATCH --output=GaEnergy.%j.out    # Include the job ID in the names of the output and error files 
#SBATCH --error=GaEnergy.%j.err 

module load VASP/5.4.4-CrayIntel-18.08 
srun vasp_std