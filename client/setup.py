from setuptools import setup, find_packages

setup(name="TrieN_Messenger_Client",
      version="0.0.1",
      description="Messenger_Client",
      author="Nikolay_Nikolaev",
      author_email="nikolaeff2007@gmail.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome']
      )
