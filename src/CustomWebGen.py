from bs4 import BeautifulSoup
import os


class WebPageGenerator:
    """
    A custom built wegpage generator for gananth.github.io
    The methods in this class modifies beautifulsoup html object
    """

    def __init__(
        self,
        soup,
        title,
        description,
        content,
        filename,
        ignore,
    ):
        self.soup = soup
        self.title = title
        self.description = description
        self.content = content
        self.filename = os.path.basename(filename)
        self.ignore1 = ignore
        self.ignore2 = ignore + ["index.html"]  # ignores index.html files
        self.called = None

    def newpage(self):
        self.called = "newpage"
        self.page_title().meta_desc().heading().subheading().add_content()

    def addlinks(
        self, nav_project=False, nav_other=False, nav_sidebar=False, new=False
    ):
        if nav_project:
            self.navbar_project()
        if nav_other:
            self.navbar_others()
        if nav_sidebar:
            self.sidebar(new=new)
        self.called = "addlinks"

    def page_title(self):
        # updates page title
        if self.filename not in self.ignore2:
            self.soup.find("title").string = (
                self.title + ": " + self.description
            )
        self.called = "page_title"
        return self

    def meta_desc(self):
        # update meta content description
        #
        if self.filename not in self.ignore1:
            self.soup.find("meta", attrs={"name": "description"})[
                "content"
            ] = self.description
        self.called = "meta_desc"
        return self

    def navbar_project(self):
        # updates dropdown menu project
        # validation
        tag = self.soup.find_all(
            "a", attrs={"class": "dropdown-item", "href": self.filename}
        )
        tag_exist = sum([i.string == self.title for i in tag])
        if self.filename not in self.ignore1 and not tag_exist:
            tag = self.soup.find("hr", attrs={"class": "dropdown-divider"})
            extraSoup = BeautifulSoup(
                '<a class="dropdown-item" href="{}">{}</a>'.format(
                    self.filename, self.title
                ),
                "html.parser",
            )
            tag.insert_before(extraSoup)
        self.called = "navbar_project"
        return self

    def navbar_others(self):
        # updates dropdown menu named OTHERS
        # Validation
        tag = self.soup.find_all(
            "a", attrs={"class": "dropdown-item", "href": self.filename}
        )
        tag_exist = sum([i.string == self.title for i in tag])
        if self.filename not in self.ignore1 and not tag_exist:
            tag = self.soup.find("nav", attrs={"class": "navbar"})
            tag = tag.ul.ul.find_all("ul")[1].li
            extraSoup = BeautifulSoup(
                '\n<li><a class="dropdown-item" href="{}">{}</a></li>'.format(
                    self.filename, self.title
                ),
                "html.parser",
            )
            tag.insert_after(extraSoup)
        self.called = "navbar_others"
        return self

    def heading(self):
        # adds heading
        if self.filename not in self.ignore2:
            self.soup.find(
                "div", attrs={"class": "row p-4 alert alert-success"}
            ).h1.string = (
                "\n                    {}\n".format(self.title)
            )
        self.called = "heading"
        return self

    def subheading(self):
        # adds sub heading
        if self.filename not in self.ignore2:
            self.soup.find(
                "div", attrs={"class": "row p-4 alert alert-success"}
            ).h5.string = (
                "\n                    {}\n".format(self.description)
            )
        self.called = "subheading"
        return self

    def sidebar(self, new=False):
        # add sidebar navigation links
        # validation
        tag = self.soup.find_all(
            "a",
            attrs={
                "class": "btn",
                "href": self.filename,
                "role": "button",
            },
        )
        tag_exist = sum([i.string == self.title for i in tag])

        if self.filename not in self.ignore2 and not tag_exist:
            # Sidebar Addition
            tag = self.soup.find("div", attrs={"class": "col-sm-3 bg-light"})

            tag = tag.find(
                "a",
                attrs={
                    "class": (
                        "btn btn-primary btn-block custom-btn mt-1 text-light"
                    ),
                    "href": "cv.html",
                    "role": "button",
                },
            )

            if not new:
                extraSoup = BeautifulSoup(
                    '<a class="btn btn-primary btn-block custom-btn mt-1'
                    ' text-light" role="button" href={} >{}</a>'.format(
                        self.filename, self.title
                    ),
                    "html.parser",
                )
            else:
                extraSoup = BeautifulSoup(
                    '<a class="btn btn-outline-primary text-secondary btn-block'
                    ' custom-btn mt-1" role="button" href={} >{}</a>'.format(
                        self.filename, self.title
                    ),
                    "html.parser",
                )

            tag.insert_before(extraSoup)
        self.called = "sidebar"
        return self

    def add_content(self):
        # add contents
        if self.filename not in self.ignore2:
            tag = self.soup.find(
                "div",
                attrs={"class": "col-sm-9 border text-secondary rounded p-4"},
            )
            tag.clear()
            extraSoup = BeautifulSoup(self.content, "html.parser")
            tag.insert(1, extraSoup)
        self.called = "add_content"
        return self

    def __str__(self):
        return "<WebPageGenerator: %s(%s, %s)>" % (
            self.called,
            self.filename,
            self.title,
        )

    def __repr__(self):
        return "<WebPageGenerator: %s(%s, %s)>" % (
            self.called,
            self.filename,
            self.title,
        )


class NavLinkDeletor:
    """
    A custom built html navigation link deleter for gananth.github.io site
    The methods in this class deletes beautifulsoup html object
    """

    def __init__(self, soup, filename, title, ignore):
        self.soup = soup
        self.filename = os.path.basename(filename)
        self.title = title
        self.ignore = ignore
        self.called = None

    def sidebar(self):
        # deletes sidebar button
        if self.filename not in self.ignore:
            tag = self.soup.find_all(
                "a",
                attrs={
                    "class": (
                        "btn btn-primary btn-block custom-btn mt-1 text-light"
                    ),
                    "href": "{}".format(self.filename),
                    "role": "button",
                },
            )
            for i in tag:
                if i.string == self.title:
                    i.decompose()
        self.called = "sidebar"
        return self

    def navbar_menus(self):
        if self.filename not in self.ignore:
            tag = self.soup.find_all(
                "a",
                attrs={
                    "class": "dropdown-item",
                    "href": "{}".format(self.filename),
                },
            )
            for i in tag:
                if i.string == self.title:
                    i.decompose()
        self.called = "navbar_menus"
        return self

    def __str__(self):
        return "<NavLinkDeletor: %s(%s, %s)>" % (
            self.called,
            self.filename,
            self.title,
        )

    def __repr__(self):
        return "<NavLinkDeletor: %s(%s, %s)>" % (
            self.called,
            self.filename,
            self.title,
        )
