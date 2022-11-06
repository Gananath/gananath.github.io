from bs4 import BeautifulSoup
import src.CustomWebGen as cwg
import pytest
import yaml
import glob


def yaml_file():
    with open("./articles/nerd.yaml", "r") as stream:
        try:
            yam = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logging.error(exc)
    return yam


def soup():
    with open("./nerd.html") as fp:
        soup = BeautifulSoup(fp, "html.parser")
    return soup


def test_check_new_html():
    try:
        soup()
        assert True
    except:
        assert False


def test_yaml_file():
    try:
        yaml_file()
        assert True
    except:
        assert False


def test_title_soup():
    assert soup().find("title").string.split()[0] == "NERD:"


def test_content_soup():
    assert (
        soup()
        .find(
            "div", attrs={"class": "col-sm-9 border text-secondary rounded p-4"}
        )
        .p.getText()
        .split()[0]
        == "If"
    )


def test_nerd_nav_project():
    assert (
        soup()
        .find("a", attrs={"class": "dropdown-item", "href": "nerd.html"})
        .string
        == "NERD"
    )


def test_nerd_sidebar():
    assert (
        soup()
        .find(
            "a",
            attrs={
                "class": (
                    "btn btn-outline-primary text-secondary btn-block"
                    " custom-btn mt-1"
                ),
                "href": "nerd.html",
            },
        )
        .string
        == "NERD"
    )

def test_sidebar_braingan():
    assert (
        soup()
        .find(
            "a",
            attrs={
                "class": "btn btn-primary btn-block custom-btn mt-1 text-light",
                "href": "multi_task.html",
            },
        )
        .string
        == "BrainGAN"
    )
