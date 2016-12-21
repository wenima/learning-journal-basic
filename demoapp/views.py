from pyramid.view import view_config
import io
import os

ENTRIES = [
    {"title" : "Entry 1", "id": 0, "creaton_date": "Dec 20, 2016",
    "body": "I learned some stuff about some other stuff."},
    {"title" : "Entry 2", "id": 1, "creaton_date": "Dec 20, 2016",
    "body": "I learned some stuff about some other stuff."},
    {"title" : "Entry 3", "id": 2, "creaton_date": "Dec 20, 2016",
    "body": "I learned some stuff about some other stuff."}
]

@view_config(route_name="home", renderer="templates/list.jinja2 ")
def home_page(request):
    """View for the homepage."""
    return {"ENTRIES": ENTRIES}

@view_config(route_name="detail", renderer="string")
def detail(request):
    import pdb; pdb.set_trace()
    the_id = int(request, matchdict["id"])
    entry = ENTRIES[the_id]
    return {"entry": entry}
