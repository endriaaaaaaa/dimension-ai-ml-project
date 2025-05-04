from setuptools import setup, find_packages

setup(
    name='dimension_ml',
    version='0.1.0',
    description='Proyecto de Machine Learning para análisis de datos y predicciones en YouTube',
    author='endriaaaaaaa',
    author_email='tu_email@example.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'tensorflow',
        'flask',
        'google-api-python-client',
    ],
)
