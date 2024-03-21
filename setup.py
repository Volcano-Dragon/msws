from setuptools import setup, find_packages

VERSION = '0.0.3' 
DESCRIPTION = 'Python package for generating the random number using Middle Square Weyl sequence'
LONG_DESCRIPTION = '''The msws package is designed to generate random numbers using the Middle Square Weyl sequence algorithm.
This algorithm offers a methodical approach to producing pseudo-random numbers with a focus on simplicity and efficiency.
The module offers functionalities to both generate random numbers and seed values necessary for the process.
'''

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="msws", 
        version=VERSION,
        author="Garv Saxena",
        author_email="garvsaxena185@gmail.com",
        url  = "https://github.com/Volcano-Dragon/msws",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        py_modules=['seed_gen','msws'],
        install_requires=[],        
        keywords=['PRNG', 'MSWS', 'Weyl sequence', 'Middle square'],
        classifiers= [
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
