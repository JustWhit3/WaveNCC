<p align="center"><img src="https://github.com/JustWhit3/WaveNCC/blob/main/img/logo.svg" height=220></p>

<h3 align="center">A program to compute the normalization coefficients of a given orthogonal 1-D complex wave function</h3>
<p align="center">
    <img title="v1.0" alt="v1.0" src="https://img.shields.io/badge/version-v1.0-informational?style=flat-square"
    <a href="LICENSE">
        <img title="MIT License" alt="license" src="https://img.shields.io/badge/license-MIT-informational?style=flat-square">
    </a>
	<img title="Python 3.8" alt="Python 3.8" src="https://img.shields.io/badge/Python-3.8-informational?style=flat-square">
    </a><br>
	<img title="Code size" alt="code size" src="https://img.shields.io/github/languages/code-size/JustWhit3/WaveNCC?color=red">
	<img title="Repo size" alt="repo size" src="https://img.shields.io/github/repo-size/JustWhit3/WaveNCC?color=red">
	<img title="Total lines" alt="total lines" src="https://img.shields.io/tokei/lines/github/JustWhit3/WaveNCC?color=red">
</p>

## Table of contents

- [Introduction](#introduction)
- [Repository structure](#repository-structure)
- [Documentation](#documentation)
- [How to use](#how-to-use)

## Introduction

This program computes the normalization coefficients <img src="https://render.githubusercontent.com/render/math?math=\color{green}{c_n}"> of a given orthogonal 1-dimensional complex wave-function <img src="https://render.githubusercontent.com/render/math?math=\color{green}{\psi_n(x)}"> for a given *n* index, or for a whole set of orthogonal wave-functions. Additionally, it performs orthogonality and orthonormality checks and plots the normalized wave-functions shapes. More physical and mathematical information can be found [here](https://github.com/JustWhit3/WaveNCC/blob/main/doc/Background%20explanation.md).

The set of <img src="https://render.githubusercontent.com/render/math?math=\color{green}{\psi_n(x)}"> wave-functions is used in quantum mechanics to find a generic solution for the 1-D [Schrödinger equation](https://users.aber.ac.uk/ruw/teach/327/hatom.php) and in particular for the equation of the harmonic oscillator.

This program computes the coefficients only for a certain kind of wave-function, which should be:

- Orthogonal.
- Real or complex.
- 1-dimensional (therefore, with only one variable).
- Time independent.

The function may depends on an index *n* but this is not necessary, since the program can calculate the coefficients also if *n=0*.
> NB: equation color is green in order to improve the readability both for light and dark GitHub themes.

An example output of the program:

<img src="https://github.com/JustWhit3/WaveNCC/blob/main/img/intro.gif">

The software is and will stay **free**, but if you want to support me with a donation it would be really appreciated!

<a href="https://www.buymeacoffee.com/JustWhit33" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## Repository structure

```txt
WaveNCC/
├── .github/
│   ├── workflows
│   │   ├── codeql-analysis.ylm
├── doc/
│   ├── Background explanation.md
│   ├── Download and install.md
│   ├── Todo.md
│   ├── CONTRIBUTING.md
│   ├── CREDITS.md
├── src/
│   ├── utils.py
│   ├── functions.py
│   ├── main.py
├── img/
│── README.md
│── LICENSE
│── CITATION.cff
│── requirements.txt
│── .gitignore
│── .all-contributorsrc
```

## Documentation

Here you can find a list of the documentation files of the repository:

- [Background explanation](https://github.com/JustWhit3/WaveNCC/blob/main/doc/Background%20explanation.md): contains some t theoretical explanations about the algorithm and the physics / mathematical background topics of the program.
- [Download, install and test](https://github.com/JustWhit3/WaveNCC/blob/main/doc/Download%20and%20install.md): contains information about how to install the requirements, test the code and run it.
- [Credits](https://github.com/JustWhit3/WaveNCC/blob/main/doc/CREDITS.md): contains a list of all the people who contributed to this project.
- [Contributing](https://github.com/JustWhit3/WaveNCC/blob/main/doc/CONTRIBUTING.md): contains some information about how to contribute to this project.
- [Todo](https://github.com/JustWhit3/WaveNCC/blob/main/doc/Todo.md): contains a list of todo stuff which could be implemented to extend the software with new tools.

## How to use

Once you ran the program and choose an option, it will be asked to insert real and imaginary part of the wave-function you want to normalize. An example is the following:

```txt
Enter the REAL part: np.cos(n*x)
Enter the IMAGINARY part: np.sin(n*x)
```

Then, you can insert the integration extremes, which will be used to check the orthogonality / orthonormality of the wave-function and to compute the normalization coefficients, for example:

```txt
Enter the LOWEST integration extreme: -3
Enter the HIGHEST integration extreme: 3
```

The next step is to insert the wave-function index *n* :

```txt
Enter the wave-function index "n": 3
```

And finally the normalization coefficient and a plot of the normalzied wave-function will be displayed:

```txt
The normalization coefficient for n = 3  is:  0.4086571521491726
```
