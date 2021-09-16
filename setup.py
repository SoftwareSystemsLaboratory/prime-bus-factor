from setuptools import setup

from ssl_metrics_bus_factor import version

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ssl-metrics-bus-factor",
    packages=["ssl_metrics_bus_factor"],
    version=version.version(),
    description="SSL Metrics - Bus Factor Metric",
    author="Software and Systems Laboratory - Loyola University Chicago",
    author_email="ssl-metrics@ssl.luc.edu",
    license="BSD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ssl.cs.luc.edu/projects/metricsDashboard",
    project_urls={
        "Bug Tracker": "https://github.com/SoftwareSystemsLaboratory/ssl-metrics-bus-factor/issues",
        "GitHub Repository": "https://github.com/SoftwareSystemsLaboratory/ssl-metrics-bus-factor",
    },
    keywords=[
        "git",
        "github",
        "software engineering",
        "metrics",
        "software systems laboratory",
        "ssl",
        "loyola",
        "loyola university chicago",
        "luc",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development",
        "Topic :: Scientific/Engineering",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.9",
    install_requires=[
        # ADD ME
    ],
    entry_points={
        "console_scripts": [
            "ssl-metrics-bus-factor-collect = ssl_metrics_bus_factor.FILENAME:main",
            "ssl-metrics-bus-factor-graph = ssl_metrics_bus_factor.create_graph:main",
        ]
    },
)
