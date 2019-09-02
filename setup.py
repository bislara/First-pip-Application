import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='app_lara_test',  
     version='0.1',
     scripts=['app_lara_test'] ,
     author="Biswajeet_Sahoo",
     author_email="biswajeetsahoo54@gmail.com",
     description="A Test package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/bislara/First-pip-Application",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )


