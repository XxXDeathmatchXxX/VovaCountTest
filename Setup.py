from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'tasks_generator'
LONG_DESCRIPTION = 'tasks_generator'

# Setting up
setup(
    name="tasks_generator",
    version=VERSION,
    author="NecrisPhayder (Kirill Kudinov)",
    author_email="<dr.kireal@yandex.ru>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=open('README.md').read(),
    packages=find_packages(),
    install_requires=['random', 'fractions', 'math'],
    keywords=['python', 'logarythms', 'fractions'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)