from setuptools import setup

setup(name="resolution_gui",
      version="1.0",
      description="A resolution GUI app for prop logic",
      url="https://github.com/Claydough6/gui_resolution",
      author="Clay Bell and Kevin Khaghani",
      author_email="claybell01@gmail.com",
      license="MIT",
      packages=["resolution_gui"],
      install_requires=[
          "ttkthemes",
          "pyprover",
          "pyparsing",
      ],
      zip_safe=False)
