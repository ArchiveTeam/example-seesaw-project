# encoding=utf8
import datetime
import os
import os.path
import shutil
import json

from seesaw.project import *
from seesaw.config import *
from seesaw.item import *
from seesaw.task import *
from seesaw.pipeline import *
from seesaw.externalprocess import *
from seesaw.tracker import *

project = Project(
  title = "Example project",
  project_html = """
    <img class="project-logo" alt="Project logo" src="http://archive.org/images/glogo.png" height="50px" />
    <h2>Example project <span class="links"><a href="http://example.com/">Example website</a> &middot; <a href="http://example.heroku.com/">Leaderboard</a></span></h2>
    <p>This is an example project. Under a logo and title there's some room for extra information.</p>
  """,
  utc_deadline = datetime.datetime(2013,1,1, 12,0,0)
)

pipeline = Pipeline(
# SetItemKey("item_name", "1083030"),
  SetItemKey("item_name", StringConfigValue(name="example.item_name", title="Item name", default="1083030")),
  PrintItem(),
  ExternalProcess("Echo", [ "echo", "1234", u"áßðf" ]),
  ExternalProcess("Echo", [ "python", "my_script.py" ]),
  ExternalProcess("sleep", [ "sleep", str(NumberConfigValue(name="example.sleep", title="Time to sleep", description="The example project will sleep n seconds.", min=1, max=15, default="5").value)]),
  ExternalProcess("pwd", [ "pwd" ]),
  PrintItem()
)

