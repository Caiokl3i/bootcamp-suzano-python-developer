from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="conversor_unidades",
    version="0.0.1",
    author="Caio Victor Santos Valentim",
    author_email="caio.victor.santos12@gmail.com",
    description="Pacote simples para conversão de unidades (comprimento e temperatura).",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/seu_usuario/conversor-unidades",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)