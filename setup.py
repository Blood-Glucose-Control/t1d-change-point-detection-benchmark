from setuptools import setup, find_packages

setup(
    name="t1d_cpd_benchmark",
    version="0.1.5",
    description="An open source benchmark for semi-supervised change point detection of type 1 diabetic meals from continuous glucose monitor time series data. Originally created to present to PyData Global 2024 in association with sktime and skchange.",
    url="https://github.com/Blood-Glucose-Control/t1d-change-point-detection-benchmark",
    packages=find_packages(),
    license="MIT",
    author="Christopher Risi",
    author_email="christopher.risi@uwaterloo.ca",
    include_package_data=True,
    install_requires=[
        "numpy>=1.25.0",
        "pandas>=2.0.3",
        "datasets>=3.0.0"
    ],
)
