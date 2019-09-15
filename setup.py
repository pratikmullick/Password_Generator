import setuptools

with open("README.md", 'r') as readme:
    long_description = readme.read()

setuptools.setup(
    name="Passgen",
    version="0.5.0",
    author="Pratik Mullick",
    author_email="pratik.mullick@gmail.com",
    description="A random password generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pratikmullick/password_generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3",
        "Operating System :: OS Independent",
        ],
    python_requires='>=3.5',
    )
