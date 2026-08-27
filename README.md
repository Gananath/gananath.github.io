# gananath.github.io

This is an improved version of my old website which was written in simple HTML tech. In this upgraded version, all of the new web pages are generated automatically. The automation of the web page generation is written in python. Not only the webpages but this automation tool also adds hyperlinks to all the static and auto generated html files.


## Auto Webpage Generation

To run the automation, first add the content YAML page to the `articles` folder and then run the following command:

python ./src/build.py

This will automatically generate the required pages. Before running this script, please verify that all required modules and dependencies are installed.

## Testing

The unit test script is located at `src/tests/unit_test.py`.

To run the tests, execute the following command:

pytest src/tests/unit_test.py

The test script verifies that the automation and page-generation functionality are working as expected.



## CI/CD with Github Actions

To automate the whole process I have used GitHubs CI/CD tool, github action. It continously build, deploy and tests(unit and integration) this web app using GitHub Actions. 
