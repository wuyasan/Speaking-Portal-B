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

---

## Project Specific Concerns

- MFA is a command line tool and has a lot of different [input file configs](https://montreal-forced-aligner.readthedocs.io/en/latest/user_guide/corpus_structure.html#corpus-structure).

- MFA is not a drop-in replacement for gentle. We will have to write a local server script to interact with it for our project.

- Moreover, the JSON output of MFA, as seen [here](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/issues/453),  is not same as the JSON output of gentle. This will lead to breaking changes in the codebase. We will have too modify the video processing code accordingly.

## Trial Findings

- The test can be found in the ```mfa_test``` folder with the names, ```inputs``` and ```japanese```.

- Upon first running the ```mfa validate``` on our data previouly used with leads to an issue, with ```.wav``` format of the audio file. We have posted the issue on the [MFA github](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner/issues/543).

- ```mfa validate``` commmand runs successfully on the ```japanese``` data. However, ```align``` command fails. We are still investigating the issue.