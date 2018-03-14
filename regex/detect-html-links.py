import sys
import re

def detect_html_links(html):
    r"""
    detect html links in html
    >>> detect_html_links("<p><a href=\"http://www.quackit.com/html/tutorial/html_links.cfm\">Example Link</a></p>\n"
    ...                   "<div class=\"more-info\">\n"
    ...                   "<a href=\"http://www.quackit.com/html/examples/html_links_examples.cfm\">More Link Examples...</a>\n"
    ...                   "</div>")
    ['http://www.quackit.com/html/tutorial/html_links.cfm,Example Link', 'http://www.quackit.com/html/examples/html_links_examples.cfm,More Link Examples...']
    """

    anchor_pattern = re.compile('<a.*?<\/a>')
    href_pattern = re.compile('(?<=href=").*?(?=")')
    textname_pattern = re.compile('(?<=>)[^<].*?(?=<)')

    def _detect_html_link(line):
        anchors = re.findall(anchor_pattern, line)
        for anchor in anchors:
            href_match = href_pattern.search(anchor)
            textname_match = textname_pattern.search(anchor)
            href = href_match.group(0) if href_match else ''
            textname = textname_match.group(0) if textname_match else ''
            return ','.join([href.strip(), textname.strip()])

    return filter(lambda x: x is not None, [_detect_html_link(line) for line in html.split('\n')])


if __name__ == '__main__':
    import doctest
    doctest.testmod()
