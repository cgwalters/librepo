import librepo
import os.path
import unittest

class TestCase(unittest.TestCase):
    repo_dir = os.path.normpath(os.path.join(__file__, "../../../repos"))

#def by_name(sack, name):
#    return librepo.Query(sack).filter(name=name)[0]