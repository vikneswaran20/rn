from setuptools import setup, find_packages
import rn

description = "CLI for Random values generation."

install_requirements = [
    "click >= 7.1.2"
]

setup(
    name='rn',
    version=rn.__version__,
    author='Vikneswaran S J',
    author_email="vikneswaran.jayaram@gmail.com",
    description=description,
    long_description=open("README.md").read(),
    license=rn.__license__,
    packages=find_packages(),
    install_requires=install_requirements,
    entry_points={
        'console_scripts': [
            'rn = rn.main:cli'
        ]
    },
    python_requires='>=3.7',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Terminals',
        'Topic :: Utilities'
    ],
)
