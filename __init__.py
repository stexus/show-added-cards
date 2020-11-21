from aqt import gui_hooks, mw
from aqt.utils import tooltip

def on_did_add_note(note) -> None:
    mw.toolbar.draw()

def getAdded():
    return len(mw.col.find_cards(query="added:1"))

def addLinkHandler() -> None:
    tooltip("Added")
def on_top_toolbar_did_init_links(links, toolbar) -> None:
    added = getAdded()
    show_add_link = toolbar.create_link(
        "added",
        "Added: %s" % added,
        addLinkHandler,
        tip="Added cards today",
        id="added"
    );
    links.append(show_add_link);


gui_hooks.add_cards_did_add_note.append(on_did_add_note)
gui_hooks.top_toolbar_did_init_links.append(on_top_toolbar_did_init_links)


