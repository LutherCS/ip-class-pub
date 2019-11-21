import requests
from bs4 import BeautifulSoup

# url = "https://www.luther.edu/catalog/curriculum/"

# response = requests.get(url)

# # print(response.text)
# print(response.status_code)
# print(response.headers)
# print(response.headers["Content-Type"].split("; ")[0])

# if response.status_code == 200 and response.headers["Content-Type"].find("html") > -1:
#     raw_html = response.text
# else:
#     print("Bad stuff")

# html = BeautifulSoup(raw_html, "html.parser")
# print(html)

# for program in html.select("div#contentSections ul > li > h4 > a"):
#     p_name = program.text
#     p_url = program["href"]
#     print(f"{p_name}: {p_url}")


url = "https://www.luther.edu/catalog/curriculum/computer-science"

response = requests.get(url)

if response.status_code == 200 and response.headers["Content-Type"].find("html") > -1:
    raw_html = response.text
else:
    print("Bad stuff")

html = BeautifulSoup(raw_html, "html.parser")

for course in html.select("div.courseContainer"):
    # print(course)
    c_number = course.select("h4 span.courseNumber")[0].text
    c_title = course.select("h4 span.courseTitle")[0].text
    try:
        c_prereqs = course.select("ul li")[1].text[15:]
    except IndexError as ie:
        c_prereqs = None
        print(ie)
    print(f"{c_number}: {c_title} ({c_prereqs})")
