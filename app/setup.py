import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="medizinfuchs",
    version="0.0.1",
    author="Maryam Alam",
    author_email="maryamalam15@gmail.com",
    description="An app to extract data from medisinfuchs.de",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MaryamAlam15/medizinfuchs",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "beautifulsoup4==4.10.0",
        "requests==2.27.1",
        "pandas==1.4.0",
    ],
    python_requires='>=3.8',
)
