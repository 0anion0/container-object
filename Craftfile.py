# craftr_module(nr.containerobject)

from craftr import *
session.path.append(path.local('..'))
from craftr.ext.maxon import c4d

objects = c4d.objects(
  sources = path.glob('src/**/*.cpp'),
  include = [project_dir] + path.local(['include', 'res/description']),
  legacy_api = True,
)

plugin = c4d.link(
  output = path.local('{}-r{}'.format(project_name, c4d.release)),
  inputs = [objects],
)


from craftr.ext.git import Git
from craftr.ext.archive import Archive
from craftr.ext.platform import name as osname

def archive():
  git = Git(project_dir)
  prefix = '{}-{}-r{}-{}'.format(project_name, git.describe(), c4d.release, osname)
  archive = Archive(prefix = prefix)
  archive.add(path.local(['res',
    'README.md',
    'CHANGELOG.md',
    'LICENSE.txt',
  ]))
  archive.add(plugin.outputs)
  archive.save()
  info(archive.name)
