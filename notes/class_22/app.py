"""Requests example"""

import requests
from flask import Flask, render_template
import bs4

app = Flask(__name__)
BASE_URL = "https://www.unionlandfeedfoodmarket.com/"
categories = ["meat", "produce"]


@app.route("/")
def index():
    all_items = []
    for cat in categories:
        resp = requests.get(f"{BASE_URL}{cat}")
        if resp.status_code == 200 and resp.headers["Content-Type"].find("html") > 1:
            raw_html = resp.text
        else:
            raise ValueError("Could not retrieve valid HTML")

        html = bs4.BeautifulSoup(raw_html, "html.parser")
        the_category = html.select("h2.font_0")[0]
        for item in html.select("ul.font_8 li p.font_8"):
            this_item = {}
            this_item["category"] = the_category.text
            for elem in item.parent.parent.previous_siblings:
                if isinstance(elem, bs4.Tag):
                    if "font_2" in elem["class"]:
                        break
            this_item["subcategory"] = elem.text
            this_item["name"] = item.text
            for elem in item.parent.parent.previous_siblings:
                if isinstance(elem, bs4.Tag):
                    if "font_8" in elem["class"] and 10 < len(elem.text) < 20:
                        break
            this_item["comment"] = elem.text
            all_items.append(this_item)

    return render_template("index.html", inventory=all_items)


if __name__ == "__main__":
    app.run()
