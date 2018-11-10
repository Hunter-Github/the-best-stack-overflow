from jinja2 import Template
from jinja2 import Environment, FileSystemLoader

with open("se_sites.txt", mode="r") as site_file:
    sites = [x.rstrip() for x in site_file.readlines()]
    

with open("se_filters.txt", mode="r") as filter_file:
    filters = [x.rstrip() for x in filter_file.readlines()]


Template("""{% for site in sites %}{% for filter in filters %}{{ site }}{{ filter }}
{% endfor %}{% endfor %}
""").stream(sites=sites, filters=filters).dump('all.filters')
