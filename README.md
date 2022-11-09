# gananath.github.io

This is an improved version of my old website which was written in simple HTML tech. In this upgraded version, all of the new web pages are generated automatically. The automation of the web page generation is written in python. Not only the webpages but this automation tool also adds hyperlinks to all the static and auto generated html files.


## Auto Webpage Generation

To run the automation; First add the content yaml page in `articles` folder and then  call `python ./src/build.py` script. This will auto generates the pages. Before running this script please verify that the required modules were installed.


## CI/CD with Github Actions

To automate the whole process I have used GitHubs CI/CD tool, github action. It continously build, deploy and tests(unit and integration) this web app using GitHub Actions. 
