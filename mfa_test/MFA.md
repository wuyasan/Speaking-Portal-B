# MFA - Research and Trial

Montreal Forced Aligner (MFA) is a tool for aligning speech data to a text transcript. 
It is the replacement for our current aligner, which is gentle. 

Migration from gentle to MFA is essential for adding new languages other than english to the project.

---

## Research

- MFA is python based like gentle, however it runs as a command line tool and has a lot more configuration options, this makes it a lot harder to use it directly as a drop-in replacement for gentle. 

- Installation instructions for MFA can be found [here](https://montreal-forced-aligner.readthedocs.io/en/latest/installation.html).

- The environment setup using conda can be found [here](https://montreal-forced-aligner.readthedocs.io/en/latest/installation.html#environment-setup).

```bash

# Create a new environment

conda config --add channels conda-forge
conda create -n aligner montreal-forced-aligner

```

