from bs4 import BeautifulSoup
import CustomWebGen as cwg
import logging
import glob
import os

logging.basicConfig(
    level=logging.NOTSET,
    format="%(asctime)s:%(levelname)s:%(name)s:%(message)s",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()],
)

html_files = glob.glob("../*.html")


links = [
    ["../proteinstatai.html", "ProteinStatsAI"],
    ["../multi_task.html", "BrainGAN"],
    ["../nerd.html", "NERD"],
    ["../prob_retrieval.html", "Probabilistic Memory Retrieval"],
]

for filename in html_files:
    logging.info("Opening {}".format(filename))
    # iterating to each static html files
    if "cv.html" in os.path.basename(filename):
        logging.info("cv.html is skipped")
        continue
    with open(filename) as fp:
        soup = BeautifulSoup(fp, "html.parser")

    # Removing All unwanted links in the file
    logging.info("Started Removing Links for {}".format(filename))
    for i in links:
        d = cwg.NavLinkDeletor(soup, i[0], i[1], ["cv.html"])
        try:
            d.sidebar().navbar_menus()
            logging.info(
                "Removed link {}:{} from {}".format(i[0], i[1], filename)
            )
        except Exception as e:
            logging.critical(e)
            logging.error("{}:{}".format(i[0], i[1]))
    with open(filename, "w") as file:
        file.write(str(d.soup))

for i in links:
    try:
        os.remove(i[0])
        logging.info("{} removed from the webpages".format(i[0]))
    except Exception as e:
        logging.warning(e)

logging.info("All processs completed")
