from setuptools import setup, find_packages

setup(
    name='prompt-engineering-framework',
    version='0.1.0',
    description='A reusable Python library for creating, managing, and rendering dynamic LLM prompts from templates',
    author='Kishore Kalingi',
    author_email='kishore@example.com',
    url='https://github.com/Kishorekalingi/prompt-engineering-framework',
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=[
        'pydantic>=2.0',
        'jinja2>=3.0',
        'pyyaml>=6.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)
