 #!/usr/bin/python
# Post XML to a web service and get XML results.
# For more robust HTTP error handler use FancyURLOpener
# E Begoli
import urllib
import httplibimport
import httplib
from xml.dom.minidom import parse, parseString
target_url = "http://TestLocation&pagesize=50"
xml_request = """\
<?xml version='1.0' encoding='UTF-8' ?>
      <<criteria>
    <includeFilterSets>
        <filterSet>
            Test
        <filterSet>
		
def send_xml():
    result = urllib.urlopen( target_url, urllib.urlencode( {'request':xml_request} ) )
    #parse results and print the xml
    # or do whatever with it
    dom = parse( result )
    print dom.toprettyxml()
    result.close()

def main():
    send_xml()

if __name__ == "__main__":
    main()