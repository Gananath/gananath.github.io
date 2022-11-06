from bs4 import BeautifulSoup
import CustomWebGen as cwg
import logging
import glob
import yaml
import os

logging.basicConfig(
    level=logging.NOTSET,
    format="%(asctime)s:%(levelname)s:%(name)s:%(message)s",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()],
)

root_path="."
yaml_files = glob.glob(root_path+"/articles/*.yaml")
html_files = glob.glob(root_path+"/*.html")
html_list = [os.path.basename(i) for i in html_files]

# Create new pages from content files
def new_page_creation():
    for yml in yaml_files:
        logging.info("CREATING NEW WEB PAGE.")
        logging.info("YAML Loading: {}".format(yml))
        with open(yml, "r") as stream:
            logging.info("Opening {}".format(yml))
            try:
                yam = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                logging.error(exc)
        # Fetching values from yaml files
        filename = yam["filename"] + ".html"
        title = yam["title"]
        description = yam["desc"]
        content = yam["content"]
        nav_project = yam["project_menu"]
        nav_other = yam["other_menu"]
        nav_sidebar = yam["sidebar"]
        if filename not in html_list:
            # Opening a base template file for modification
            # This modified base file then becomes the new web page
            logging.info("Loading Template Files for {}".format(filename))
            with open(root_path+"/squeeznet-nano.html") as fp:
                soup = BeautifulSoup(fp, "html.parser")
            p = cwg.WebPageGenerator(
                soup, title, description, content, filename, ["cv.html"]
            )

            # To prevent creation of new bugs
            # No navigation links for  navbar is cretated
            # Only sidebar with outline button is created
            p.newpage()
            logging.info(
                "New HTML page has been created for {}.".format(filename)
            )
            # p.addlinks(nav_other=True,nav_sidebar=True)

            # writes the new webpage to the root directory
            with open(root_path+"/" + filename, "w") as file:
                file.write(str(p.soup))
            logging.info("Writing {} to disk.".format(filename))

            # After creating the new web pages its links will be automatically
            # added to all other static html files
            logging.info("Link generation for static html files")

            logging.info("{} COMPLETED\n\n".format(filename))


def adding_links2pages():
    # Adding menu and sidebar links
    html_files = glob.glob(root_path+"/*.html")
    for yml in yaml_files:
        logging.info("CREATING LINKS")
        with open(yml, "r") as stream:
            logging.info("Opening {}".format(yml))
            try:
                yam = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                logging.error(exc)

        filename = yam["filename"] + ".html"
        title = yam["title"]
        description = yam["desc"]
        content = yam["content"]
        nav_project = yam["project_menu"]
        nav_other = yam["other_menu"]
        nav_sidebar = yam["sidebar"]

        for html in html_files:
            if "cv.html" in os.path.basename(html):
                logging.info("skipped cv.html file")
                continue
            logging.info("Link Loading {}".format(html))
            with open(html) as fp:
                soup = BeautifulSoup(fp, "html.parser")
            page_link = cwg.WebPageGenerator(
                soup, title, description, content, filename, ["cv.html"]
            )

            if "index.html" in os.path.basename(html):
                page_link.addlinks(
                    nav_project=nav_project,
                    nav_other=nav_other,
                    nav_sidebar=False,
                )
            elif filename == os.path.basename(html):
                page_link.addlinks(
                    nav_project=nav_project,
                    nav_other=nav_other,
                    nav_sidebar=nav_sidebar,
                    new=True,
                )
            else:
                page_link.addlinks(
                    nav_project=nav_project,
                    nav_other=nav_other,
                    nav_sidebar=nav_sidebar,
                )

            logging.info("Links has been created for {}".format(filename))
            with open(html, "w") as file:
                file.write(str(page_link.soup))
            logging.info("Writing {} to disk.".format(html))

    logging.info("All Process COMPLETED\n\n")


def main():
    print("------START OF PROGRAM------")
    new_page_creation()
    print("#" * 60)
    print()
    adding_links2pages()
    print("------END OF PROGRAM--------")


if __name__ == "__main__":
    main()
