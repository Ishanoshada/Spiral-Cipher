from setuptools import setup, find_packages
import os

# Read the contents of README file
with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Project metadata and configurations
setup(
    # Package information
    name="spiral-cipher",
    version="0.1.1",
    packages=find_packages(include=['spiral_cipher', 'spiral_cipher.*']),
    
    # Package dependencies
    install_requires=[
        'typing;python_version<"3.5"',  # Conditional dependency for older Python
    ],
    
    # Package metadata
    author="Ishan Oshada",
    author_email="ishan.kodithuwakku.offical@gmail.com",
    description="A spiral cipher implementation for text encryption and decryption",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="cipher, encryption, spiral, cryptography, security",
    
    # Project URLs
    url="https://github.com/ishanoshada/spiral-cipher",
    project_urls={
        "Bug Tracker": "https://github.com/ishanoshada/spiral-cipher/issues",
        "Documentation": "https://github.com/ishanoshada/spiral-cipher#readme",
        "Source Code": "https://github.com/ishanoshada/spiral-cipher",
    },
    
    # Classifiers help users find your project
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Security :: Cryptography",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    
    # Command line interface
    entry_points={
        'console_scripts': [
            'spiral-cipher=spiral_cipher.cli:main',
        ],
    },
    
    # Include additional files
    package_data={
        'spiral_cipher': ['py.typed'],  # For type checkers
    },
    
    # Additional package configurations
    zip_safe=False,  # Recommended for mypy
    platforms=['any'],
  
)