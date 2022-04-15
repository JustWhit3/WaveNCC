# Download and install

## Table of contents

- [Download](#download)
- [Prerequisites](#prerequisites)
- [Run the program](#run-the-program)

## Download

To download the program you can proceed in two independent ways.

First of all, you need to download the code: go to the [main page](https://github.com/JustWhit3/WaveNCC) of the repository and click on the upper right green button called `Code`. Then click on `Download ZIP` and wait the download to be completed.

Alternatively you can download the latest version of the repository from the ``Releases`` button on the right of the repository main page by clicking on the source code link

## Prerequisites

To correctly run the program you need some prerequisite installed in your device:

- Python 3.8.10.
- [Doctest](https://docs.python.org/3/library/doctest.html) for Python.
- All the required libraries with the right version.

To install the required libraries you can run:

```shell
pip install -r requirements.txt
```

## Run the program

To run the code you can simply enter this command in the shell:

```shell
python src/main.py
```

Extra information about how to move inside the command line once you have ran the code can be found in the [How to use](https://github.com/JustWhit3/WaveNCC#:~:text=with%20new%20tools.-,How%20to%20use,-Once%20you%20ran) section of the README.

If you want to run the tests you have to type:

```shell
python src/functions.py
```

If anything is displayed it means that tests ran correctly.

Tests have been performed using the [Doctest](https://docs.python.org/3/library/doctest.html) framework.

If you want a detailed tests log printed on the screen, simply enter:

```shell
python src/functions.py -v
```
