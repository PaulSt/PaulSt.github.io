---
layout: post
title:  "NGSTrefftz on the cluster in Göttingen"
categories: python
---

There are some very nice [instructions](https://cpde.math.uni-goettingen.de/en/software/goesetup/index.html) showing how to log in on the HPC cluster in Göttingen and how to get ngsolve and xfem up and running. Based on the setup scripts there, I put together an [install script for ngstrefftz](/assets/hpc-ngstrefftz.txt).

The script uses the following recommended directory structure
```
$BASEDIR
├── src
├── build
├── packages
└── modules
```
where `$BASEDIR` will by default be the home directory.
Make sure to have ngsolve installed, you can find an install script [here](https://cpde.math.uni-goettingen.de/static/scripts/cluster_install.bash).

With this, only a simple `run.sh` script is missing to get your code started. The script takes care of choosing the correct hardware and loading the modules. 
A list of hardware can be found [here](https://www.gwdg.de/web/guest/hpc-on-campus/scc), most important choices are the partition `-p`, allowed runtime `-t`, thread `-n`, nodes `-N`, and memory `--mem`. 

```
#!/bin/bash
#SBATCH -p medium
#SBATCH -t 24:00:00
#SBATCH -n 24
#SBATCH --mem 128GB
#SBATCH -N 1
#source /usr/users/pstocke/.bashrc
#pip3 install --user pandas

export BASEDIR=/usr/users/pstocke
export MODULEPATH="$MODULEPATH:${BASEDIR}/modules"

module load gcc/9.3.0
module load python/3.9.0
module load intel-parallel-studio/cluster.2020.4
module load ngsolve/serial
module load ngstrefftz/serial

/usr/bin/time -v python3 -u example.py
```

This can be run using `sbatch run.sh`. Check all submitted processes using `squeue -u username` and cancel any of them using `scancel jobnumber`.
