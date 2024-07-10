from setuptools import setup, find_packages

# Installation requirements needed absolutely for the program to run
install_requires = [
    "Django==5.0.*",
    "Jinja2==3.1.*",
]

# Additional feature sets and their requirements
extras_require = {
    "dev": [
        "flake8-black",
    ]
}


def read_file(fname):
    with open(fname, "r", encoding="utf-8") as f:
        return f.read()


setup(
    name="app",
    version="0.1.0",
    author="Nataly Basova",
    author_email="umz-strahova@mail.ru",
    description="Goods flow meter",
    long_description=read_file("README.md"),
    long_description_content_type="text/markdown",
    url="https://github.com/NatalyBasova/otus_project",
    packages=find_packages(),
    install_requires=install_requires,
    extras_require=extras_require,
    entry_points={"console_scripts": ["app=app.main:main"]},
    python_requires=">=3.9",
)
