import BeautifulSoup
import mechanize
import urllib3
import cookielib

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)
br.open("http://www.trainenquiry.com/ntes/")

br.form()
