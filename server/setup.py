from setuptools import setup, find_packages

setup(name="Trien_mess_server",
      version="0.0.1",
      description="mess_server",
      author="Nikolay Nikolaev",
      author_email="nikolaeff2007@gmail.com",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome']
      )
