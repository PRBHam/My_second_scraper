# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
# Line 4 is importing scraperwiki which is a library
import scraperwiki
import lxml.html
#
print("Hello")
# # Read in a page
html = scraperwiki.scrape("http://foo.com")
print(html)
# # This code gets the html from scraperwiki.scrape
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
root.cssselect("a")
#
print(root.cssselect("a"))
print (root)
root.cssselect
List of matches=root.cssselect("a")
For match in List of matches:
  print(match)
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
