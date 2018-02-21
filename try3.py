from bs4 import BeautifulSoup
import urllib.request as req
import re

site = req.Request('http://stratpoint.com/projects/')
page = req.urlopen(site)
soup = BeautifulSoup(page, 'html.parser') # from url

target = soup.find(id=re.compile('projects-list')).div.find_all('div', recursive=False)
tags = []
for tag in target:
    project = {}
    project['name'] = tag.select('.project-brief')[0].h2.string
    project['img'] = tag.a.attrs['href']

    tags.append(project)

print(tags)

projects = soup.select('.project')
tags = []
for proj in projects:
    project = {}
    project['name'] = proj.find(class_=re.compile('project-brief')).h2.string
    project['img'] = proj.attrs['href']

    tags.append(project)

target = soup.find(id=re.compile('projects-list'))
tag_name = target = soup.find(id=re.compile('projects-list')).name
tag_attrs = tag.attrs
