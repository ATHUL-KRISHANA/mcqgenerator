from setuptools import find_packages,setup
setup(
    name='mcq',
    version='0.0.1',
    author='athul',
    install_requires=['groq','langchain','streamlit','python-dotenv','PyPDF2','langchain-groq'],
    packages=find_packages()

)