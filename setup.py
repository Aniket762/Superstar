import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    #Here is the module name.
    name="superstar",
 
    #version of the module
    version="0.1" ,
 
    #Name of Author
    author="Aniket Pal",
 
    #your Email address
    author_email="aniketindian8@gmail.com",
 
    #Small Description about module
    description="Generating bollywood star names",
 
    long_description=long_description,
 
    #Specifying that we are using markdown file for description
    long_description_content_type="text/markdown",
 
    #Any link to reach this module, if you have any webpage or github profile
    url="https://github.com/Aniket762/superstar",
    packages=setuptools.find_packages(),
 
    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
