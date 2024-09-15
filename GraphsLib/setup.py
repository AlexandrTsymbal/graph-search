from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='GraphsLib',
    version='0.0.1',
    author='sanchezzzz300',
    author_email='sasha.tsymbal.04@gail.com',
    description='A simple library for finding the shortest path '
                'in a graph by different algorithms',
    long_description=readme(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
)
