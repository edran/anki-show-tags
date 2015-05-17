from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
from aqt.reviewer import Reviewer


def showTags():
    # global note
    note = mw.reviewer.card.note()
    c = str(note.stringTags())
    # c = Reviewer.card
    # show a message box
    showInfo("Tag: %s" % c)


action = QAction("Show tags", mw)
mw.connect(action, SIGNAL("triggered()"), showTags)
mw.form.menuTools.addAction(action)
