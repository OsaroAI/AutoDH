from setuptools import find_packages, setup
import versioneer

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="osaro-AutoDH",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Eddie Groshev",
    url="https://github.com/OsaroAI/AutoDH",
    description="Library for automatic extraction of Denavit-Hartenberg parameters",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    keywords="autdh automatic dh denavit-hartenberg robotics robot kinematics ik fk inverse forward",
    license="MIT",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests", "tests.*"]),
    install_requires=[
        "click",
        "numpy",
        "prettytable",
        "flake8",
        "bandit",
        "isort"
    ],
    extras_require={
        "test": [
            "pytest",
            "pytest-cov",
            "pytest-mock",
            "flake8>=3.7.9,<4",
            "isort>=5.8.0,<6",
            "mypy>=0.910,<1",
            "pytest-cov",
            "pytest-env",
            "pytest-html",
            "pytest-mock",
            "pytest-timeout",
            "pytest>=6.2.3,<7",
        ],
    },
)
