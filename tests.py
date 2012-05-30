#!/usr/bin/python

import unittest
import subprocess

def do(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    return stdout

class TestPositionLeftmostWidthFull(unittest.TestCase):

    def test_position(self):

        def check(sheet):
            a = do("grep \.position-0 %s" % sheet)
            b = do("grep \.position-leftmost %s" % sheet)
            self.assertEqual(a.replace('position-0', 'position-leftmost'), b, sheet)

        for n in [12, 16]:
            check("decogrids-%d.css" % n)
            check("gapless/decogrids-%d-gapless.css" % n)
        check("gapless/decogrids-9-gapless.css")

    def test_width(self):

        def check(n, sheet):
            a = do("grep \.width-%d %s" % (n, sheet))
            b = do("grep \.width-full %s" % sheet)
            self.assertEqual(a.replace("width-%d" % n, 'width-full'), b, sheet)

        for n in [12, 16]:
            check(n, "decogrids-%d.css" % n)
            check(n, "gapless/decogrids-%d-gapless.css" % n)
        check(9, "gapless/decogrids-9-gapless.css")

    def test_no_div_in_gapless(self):

        def check(sheet):
            a = do("grep div %s" % sheet)
            self.assertEqual("", a)

        for n in [9, 12, 16]:
            check("gapless/decogrids-%d-gapless.css" % n)
        
if __name__ == '__main__':
    unittest.main()    
