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
