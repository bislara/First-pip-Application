import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='weather_app_nitr',  
     version='0.1',
     scripts=['weather_info'] ,
     author="Biswajeet_Sahoo",
     author_email="biswajeetsahoo54@gmail.com",
     description="A Test package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/bislara/First-pip-Application/tree/master/weather_app",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )


