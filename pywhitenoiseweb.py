import webbrowser
from requests_html import HTMLSession
import re
import random
import os
import time

while True:
    session = HTMLSession()

    page = random.randrange(1,6)
    siteinfo_re = re.compile("\/siteinfo\/(.+)")

    site = "http://www.alexa.com/topsites/category;" + str(page) +"/Top/Business/"
    print("[*] Grabbing link from %s" % site)
    r = session.get(site)
    links = []
    for l in r.html.links:
        m = siteinfo_re.match(l)
        if m:
            links.append(m.group(1))

    link = "http://www." + random.choice(links)

    print("[*] Opening %s in Firefox" % link)
    webbrowser.get('firefox').open(link)

    viewsleep = random.randrange(30,60)
    print("[*] Sleeping for %s seconds" % viewsleep)
    time.sleep(viewsleep)

    if os.name == 'nt':
        os.system("taskkill /f /im Firefox.exe")
    else:
        print("[*] Killing Firefox")
        os.system("pkill firefox")

    loopsleep = random.randrange(30, 60)
    print("[*] Sleeping for %s seconds" % loopsleep)
    time.sleep(loopsleep)

    longbreak = random.randrange(0,4)
    if longbreak == 0:
        breaktime = random.randrange(240, 1200)
        print("[*] Taking a long break of %s seconds..." % breaktime)
        time.sleep(breaktime)
