import requests  # type: ignore
from scrapy.selector import Selector, SelectorList  # type: ignore
from utils.typeshints import request_content  # type: ignore
from utils.exceptions import WebSiteError  # type: ignore


class Scraper:
    """
    Base Model for spiders, this model contains scrap method and css, xpath selector
    """

    def __init__(self, url=None) -> None:
        self.url = url
        self.request_content = None

    def scrap(self) -> request_content | None:
        """
        Send http request to target URL and return request content.

        If the request status code is 200, it means everything is fine and returns the content of the request.
        If the status code is not equal to 200, it returns WebSiteError
        """

        req = requests.get(url=self.url)

        if req.status_code == 200:
            self.request_content = req.content
            return self.request_content

        raise WebSiteError(
            f"Received {req.status_code} http status code from {self.url}"
        )

    def css(self, query: str) -> SelectorList[Selector]:
        """
        Apply the given CSS selector and return a :class:`SelectorList` instance.

        ``query`` is a string containing the CSS selector to apply.

        In the background, CSS queries are translated into XPath queries using
        `cssselect`_ library and run ``.xpath()`` method.

        .. _cssselect: https://pypi.python.org/pypi/cssselect/
        """

        return Selector(text=self.request_content).css(query)

    def xpath(self, query: str) -> SelectorList[Selector]:
        """
        Find nodes matching the xpath ``query`` and return the result as a
        :class:`SelectorList` instance with all elements flattened. List
        elements implement :class:`Selector` interface too.

        ``query`` is a string containing the XPATH query to apply.

        ``namespaces`` is an optional ``prefix: namespace-uri`` mapping (dict)
        for additional prefixes to those registered with ``register_namespace(prefix, uri)``.
        Contrary to ``register_namespace()``, these prefixes are not
        saved for future calls.

        Any additional named arguments can be used to pass values for XPath
        variables in the XPath expression, e.g.::

            selector.xpath('//a[href=$url]')
        """
        return Selector(text=self.request_content).xpath(query)
