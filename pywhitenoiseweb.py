import webbrowser
from requests_html import HTMLSession
import re
import random
import os
import time

page_max = 6
viewsleep_max = 60
loopsleep_max = 60
breaktime_max = 1200

while True:
    session = HTMLSession()

    page = random.randrange(1, page_max)
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

    viewsleep = random.randrange(viewsleep_max / 2, viewsleep_max)
    print("[*] Sleeping for %s seconds" % viewsleep)
    time.sleep(viewsleep)

    print("[*] Killing Firefox")
    if os.name == 'nt':
        os.system("taskkill /f /im Firefox.exe")
    else:
        os.system("pkill firefox")

    loopsleep = random.randrange(loopsleep_max / 2, loopsleep_max)
    print("[*] Sleeping for %s seconds" % loopsleep)
    time.sleep(loopsleep)

    longbreak = random.randrange(0, 4)
    if longbreak == 0:
        breaktime = random.randrange(breaktime_max / 5, breaktime_max)
        print("[*] Taking a long break of %s seconds..." % breaktime)
        time.sleep(breaktime)
