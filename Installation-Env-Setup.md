# Installing and Running

This guide assumes you have ```python v3.9``` and ```conda``` already installed.

## Installing

1. Clone the repo from [Github](https://github.com/wuyasan/Speaking-Portal-B)
2. Follow the instructions for installing the [Montreal Forced Aligner](https://montreal-forced-aligner.readthedocs.io/en/latest/installation.html)
3. See the [MFA Language Requirements](#mfa-language-requirements) section for more information on installing the required language models.

## Running

1. Navigate to the ```src/api``` directory.
2. Activate the ```aligner``` conda environment or the environment in which you have installed `mfa`.
    ```bash
    conda activate aligner
    ```
3. Run the flask server.
    ```bash
    flask run
    ```

## MFA Language Requirements
1. English
    
    Download the dictionary
    ```bash
    mfa model download dictionary english_us_arpa
    ```
    Download the acoustic model
    ```bash
    mfa model download acoustic english_us_arpa
    ```
2. French

    Download the dictionary
    ```bash
    mfa model download dictionary french_mfa
    ```
    Download the acoustic model
    ```bash
    mfa model download acoustic french_mfa
    ```
3. Japanese

    Download the dictionary
    ```bash
    mfa model download dictionary japanese_mfa
    ```
    Download the acoustic model
    ```bash
    mfa model download acoustic japanese_mfa
    ```
You can find more information about the dictionaries and acoustic models [here](https://mfa-models.readthedocs.io/en/latest/)
