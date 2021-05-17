import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="notifymanager",
    version="0.0.1",
    author="isuru perera",
    author_email="isurumahesh97@gmail.com",
    description="manage notifications in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iperera97/notifymanager",
    packages=["notifymanager"],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)