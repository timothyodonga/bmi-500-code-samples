# bmi-500-code-samples

This repository contains code from a project where word and ngram analysis is performed on a test document.

First of all, make sure that you have pip installed on your computer so that you can install the dependencies needed to run the code. 
If you use venv to create a virtual environment, create you virtual environment and run the command below
`pip install -r requirements.txt`

If you prefer to use pipenv for your virtual environment, create a pipenv environment and run the command below
`pipenv install -r requirements.txt`

To run the script

`python compute_ngram_statistics.py <name of the text document>.txt`

You can test the code using the sample text document given i.e. all.txt using the command shown below

`python compute_ngram_statistics.py all.txt`

The output of the analysis will be found in a data folder, that is created as the program runs.