import setuptools

setuptools.setup(
    name="pyconfighandler",
    version="0.0.1",
    author="Robert R. Puccinelli",
    author_email="robert.puccinelli@outlook.com",
    description="Handler utilities for configuration files.",
    url="https://github.com/czbiohub/pyconfighandler",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*",
                                               "tests.*", "tests"]),
    install_requires=[

    ],
    test_suite="tests",
    classifiers=[
        "CZ Biohub :: Bioengineering",
    ],
)
