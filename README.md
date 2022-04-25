# CLIME Bus Factor

[![DOI](https://zenodo.org/badge/407346377.svg)](https://zenodo.org/badge/latestdoi/407346377)
[![Release Project](https://github.com/SoftwareSystemsLaboratory/clime-bus-factor/actions/workflows/release.yml/badge.svg)](https://github.com/SoftwareSystemsLaboratory/clime-bus-factor/actions/workflows/release.yml)

> A tool to calculate the bus factor metric of a Git repository

## Table of Contents

- [CLIME Bus Factor](#clime-bus-factor)
  - [Table of Contents](#table-of-contents)
  - [About](#about)
    - [Licensing](#licensing)
  - [How To Use](#how-to-use)
    - [Installation](#installation)
    - [Command Line Options](#command-line-options)

## About

The Software Systems Laboratory (SSL) CLIME Bus Factor project is a tool to calculate the bus factor metric of a Git repository. This tool relies on the output of the [CLIME Commits tool](https://github.com/SoftwareSystemsLaboratory/clime-commits).

### Licensing

This project is licensed under the BSD-3-Clause. See the [LICENSE](LICENSE) for more information.

## How To Use

### Installation

You can install the tool via `pip` with either of the two following one-liners:

- `pip install --upgrade pip clime-metrics`
- `pip install --upgrade pip clime-bus-factor`

### Command Line Options

`clime-git-bus-factor-compute -h`

``` shell
usage: CLIME Bus Factor Calculator [-h] [-i INPUT] [-o OUTPUT] [-v]

A tool to calculate the bus factor of a Git repository

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        Commits JSON file. DEFAULT: ./commits_loc.json
  -o OUTPUT, --output OUTPUT
                        Output JSON file. DEFAULT: ./bus_factor.json
  -b BIN, --bin BIN
                        Bin containing the number of days between computed bus
                        factor values. DEFAULT: 1
  -v, --version         Display version of the tool

Author(s): Nicholas M. Synovic, Matthew Hyatt, George K. Thiruvathukal
```

`clime-git-bus-factor-graph -h`

``` shell
usage: CLIME Bus Factor Grapher [-h] [-i INPUT] [-o OUTPUT] [--type TYPE]
                                [--title TITLE] [--x-label X_LABEL]
                                [--y-label Y_LABEL] [--stylesheet STYLESHEET]
                                [-v]

A tool to graph the bus factor of a repository

options:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        JSON export from clime-git-bus-factor-compute.
                        DEFAULT: ./bus_factor.json
  -o OUTPUT, --output OUTPUT
                        Filename of the graph. DEFAULT: ./bus_factor.pdf
  --type TYPE           Type of figure to plot. DEFAULT: line
  --title TITLE         Title of the figure. DEFAULT: ""
  --x-label X_LABEL     X axis label of the figure. DEFAULT: ""
  --y-label Y_LABEL     Y axis label of the figure. DEFAULT: ""
  --stylesheet STYLESHEET
                        Filepath of matplotlib stylesheet to use. DEFAULT: ""
  -v, --version         Display version of the tool

Author(s): Nicholas M. Synovic, Matthew Hyatt, George K. Thiruvathukal
```
