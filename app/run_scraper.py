import requests
from html.parser import HTMLParser


class Parser(HTMLParser):
    # method to append the start tag to the list start_tags.
    # def handle_starttag(self, tag, attrs):
    #     print(tag)
    #     # method to append the end tag to the list end_tags.
    #
    # def handle_endtag(self, tag):
    #     print(tag)
    # method to append the data between the tags to the list all_data.

    def handle_data(self, data):
        if data != "\n" and data != "\n\n":
            print("Encountered some data  :", [data.replace("\n","")])
            global st
            st.append(data)
    # method to append the comment to the list comments.

    # def handle_comment(self, data):


st = []
r = requests.get("https://en.wikipedia.org/wiki/Python_(programming_language)#Typing")
s = r.text
parser = Parser()

print(s.find("<table>"))
print(s.find("</table>"))
s = s[s.find('<table class="wikitable">')+6:]
s = s[:s.find("</table>")]
s = s[s.find("<tbody>")+6:s.find("</tbody>")]
parser.feed(s)
# print(s)
# print(st)