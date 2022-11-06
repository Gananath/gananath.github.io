from bs4 import BeautifulSoup
import src.CustomWebGen as cwg
import pytest
import glob



def soup():
    with open("./squeeznet-nano.html") as fp:
        soup = BeautifulSoup(fp, "html.parser")
    return soup


def data():
    title = "Title"
    description = "description"
    content = "<p>hello</p>"
    filename = "/newfile.html"
    nav_project = False
    nav_other = True
    nav_sidebar = True
    return (
        title,
        description,
        content,
        filename,
        nav_project,
        nav_other,
        nav_sidebar,
    )


def new_soup():
    p = cwg.WebPageGenerator(
        soup(), data()[0], data()[1], data()[2], data()[3], ["cv.html"]
    )
    return p


def test_check_yaml_files():
    yaml_files = glob.glob("./articles/*.yaml")
    assert "./articles/deepspectra.yaml" in yaml_files


def test_soup_file():
    assert type(soup()).__name__ == "BeautifulSoup"


def test_squeezent_soup():
    assert (
        "".join(soup().find("h1", attrs={"class": "display-5"}).string.split())
        == "Squeeznet-nano"
    )


def test_squeezent_hyperlink():
    assert len(soup().find_all("a")) > 0


def test_new_soup():
    assert "<WebPageGenerator" in str(new_soup())


def test_new_soup_attributes():
    assert new_soup().title == "Title"
    assert new_soup().description == "description"
    assert new_soup().content == "<p>hello</p>"


def test_new_soup_desc():
    lst = ["page_title", "sidebar", "subheading", "add_content", "addlinks"]
    for i in lst:
        assert i in dir(new_soup())


def test_new_soup_page_title():
    assert (
        new_soup().page_title().soup.find("title").string.split()[0] == "Title:"
    )


def test_new_soup_meta_desc():
    assert (
        new_soup()
        .meta_desc()
        .soup.find("meta", attrs={"name": "description"})["content"]
        == "description"
    )


def test_new_soup_newpage():
    a = new_soup()
    a.newpage()
    assert a.soup.find("title").string.split()[0] == "Title:"
    assert (
        a.soup.find("meta", attrs={"name": "description"})["content"]
        == "description"
    )
