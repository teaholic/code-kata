from setuptools import setup, find_packages

setup(
    name="python-katas",
    version="0.0.1",
    description="Python Katas - Coding Katas",
    author="@teaholic",
    long_description_content_type="text/markdown",
    classifiers=["Development Status :: 3 - Alpha",],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=[],
    extras_require={"test": ["tox==3.27.0"]},
)
