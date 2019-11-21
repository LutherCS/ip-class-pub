# Scraping web pages for data

**Note: Use API, if available!**

## Preparation

```text
pip install requests BeautifulSoup4
```

## requests

```python
resp = requests.get(url)

print(resp.text)
print(resp.status_code)
print(resp.headers)
print(resp.headers["Content-Type"])
```

## BeautifulSoup

```python
html = BeautifulSoup(raw_html, "html.parser")
for ahref in html.select("div#contentSections ul > li > h4 > a"):
    p_url = ahref["href"]
    p_name = ahref.text
```

## References

* [Curriculum | 2019-20 Academic Catalog | Luther College](https://www.luther.edu/catalog/curriculum/)
* [Practical Introduction to Web Scraping in Python – Real Python](https://realpython.com/python-web-scraping-practical-introduction/)
* [Beautiful Soup Documentation — Beautiful Soup 4.4.0 documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
