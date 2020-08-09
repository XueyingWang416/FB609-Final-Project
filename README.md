# :blossom: FB609 Final Project: Valuing Basket Options :octocat::blossom:

This repository contains Python Implementation of our Basket Options Evaluation Project.

Project GitHub Repo: <https://github.com/XueyingWang416/FB609-Final-Project>

## 1. Code Running Environment Setup

This Python implementation requires a number of libaries to run, the dependencies are listed in `requirements.txt`. To run the code, it is recommended to setup a separate virtual environment first. Specifically (Anaconda installation is assumed),

1. Open Mac/Linux Terminal or Windows Command Line, run the following script command:
    `conda create -n quantenv`
    This will create a Python environment called `quantenv`, you can also specify the Python version here, for instance,
    `conda create -n quantenv python=3.6.10`
2. Install the required libraries:
    `pip install -r requirements.txt`
3. (Optional) Install jupyter notebook if haven't:
   `pip install notebook`
4. `cd` to project directory and launch jupyter notebok inside the directory:
   `cd ~/FB609-Final-Project`
   `jupyter notebook`

## Special Features

1. ***Data Visualization***

    Here to have a more intuitive visualization of the stock correlation, we use the Seaborn library to display heatmaps of stock correlations.

2. ***Power Speed-Up Using Numba***

    Here we use the Python Numba library for acceleration. Specifically, we use the `@njit` annotation, which enables `non-python` mode and *Just-In-Time* compilation, which instead of interpreting bytecode every time a method is invoked, will compile the bytecode into the machine code instructions of the running machine, and then invoke this object code instead. Also, to utilize the power of modern multi-core CPU, we also add the `parallel=True` option: `@njit(parallel=True)`
