# Software Systems Laboratory Metrics Git Bus Factor

> A `python` tool to calculate the bus factor of a `git` repository

![[https://img.shields.io/badge/python-3.9.6%20%7C%203.10-blue](https://img.shields.io/badge/python-3.9.6%20%7C%203.10-blue)](https://img.shields.io/badge/python-3.9.6%20%7C%203.10-blue)
[![DOI](https://zenodo.org/badge/407346377.svg)](https://zenodo.org/badge/latestdoi/407346377)
![[https://img.shields.io/badge/build-Example-red](https://img.shields.io/badge/build-Example-red)](https://img.shields.io/badge/build-Example-red)
![[https://img.shields.io/badge/license-BSD--3-yellow](https://img.shields.io/badge/license-BSD--3-yellow)](https://img.shields.io/badge/license-BSD--3-yellow)

## Table of Contents

- [Software Systems Laboratory Metrics Git Bus Factor](#software-systems-laboratory-metrics-git-bus-factor)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
  - [Developer Tooling](#developer-tooling)
    - [Operating System](#operating-system)
  - [How To Use](#how-to-use)
    - [Installation](#installation)
    - [Command Line Arguements](#command-line-arguements)

## About

The Software Systems Laboratory (SSL) Git Bus Factor Project is a `python` tool that lets users calculate and graph the bus facto of a `git` repository. This tool relies on the output of the [Git Commits LOC](https://github.com/SoftwareSystemsLaboratory/ssl-metrics-git-commits-loc) project.

This project is licensed under the BSD-3-Clause. See the [LICENSE](LICENSE) for more information.

## Developer Tooling

To maximize the utility of this project and the greater SSL Metrics project, the following software packages are **required**:

### Operating System

All tools developed for the greater SSL Metrics project **must target** Mac OS and Linux. SSL Metrics software is not supported or recommended to run on Windows *but can be modified to do so at your own risk*.

It is recomendded to develop on Mac OS or Linux. However, if you are on a Windows machine, you can use WSL to develop as well.

## How To Use

### Installation

You can install the tool via `pip` with either of the two following one-liners:

- `pip install --upgrade pip ssl-metrics-meta`
- `pip install --upgrade pip ssl-metrics-git-bus-factor`

### Command Line Arguements

`ssl-metrics-git-bus-factor-compute -h`

```shell
options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        JSON file outputted from ssl-metrics-git-commits-loc-extract to be used to calculate bus factor
  -o OUTPUT, --output OUTPUT
                        JSON file that will contain the bus factor metric information
```

`ssl-metrics-git-bus-factor-graph -h`

```shell
options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        The input data file that will be read to create the graphs
  -o OUTPUT, --output OUTPUT
                        The filename to output the bus factor graph to
  -m MAXIMUM_DEGREE_POLYNOMIAL, --maximum-degree-polynomial MAXIMUM_DEGREE_POLYNOMIAL
                        Estimated maximum degree of polynomial
  -r REPOSITORY_NAME, --repository-name REPOSITORY_NAME
                        Name of the repository that is being analyzed
  --x-window-min X_WINDOW_MIN
                        The smallest x value that will be plotted
  --x-window-max X_WINDOW_MAX
                        The largest x value that will be plotted
```
