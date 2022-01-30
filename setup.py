from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.2",
    author="sagnik",
    description="A small package ",
    long_description=long_description,#this will read from readme file above
    long_description_content_type="text/markdown",
    url="https://github.com/sagnik-chakraborty-DS/affair_logistic_regression",
    author_email="sagnikc137@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)
