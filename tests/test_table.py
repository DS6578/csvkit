#!/usr/bin/env python

from cStringIO import StringIO
import unittest

from csvkit import table 

class TestColumn(unittest.TestCase):
    def setUp(self):
        self.c = table.Column(0, u'test', [u'test', u'column', None])

    def test_create_column(self):
        self.assertEqual(type(self.c), table.Column)
        self.assertEqual(self.c.index, 0)
        self.assertEqual(self.c.name, u'test')
        self.assertEqual(self.c.type, unicode)
        self.assertEqual(self.c, [u'test', u'column', None])

    def test_slice(self):
        self.assertEqual(self.c[1:], [u'column', None])

    def test_access(self):
        self.assertEqual(self.c[-1], None)

class TestTable(unittest.TestCase):
    def test_from_csv(self):
        with open('examples/testfixed_converted.csv', 'r') as f:
            t = table.Table.from_csv(f)

        self.assertEqual(type(t), table.Table)
        self.assertEqual(t.headers, [u'text', u'date', u'integer', u'boolean', u'float', u'time', u'datetime', u'empty_column'])
        self.assertEqual(type(t.columns[0]), table.Column)
        self.assertEqual(len(t.columns), 8)

    def test_to_csv(self):
        with open('examples/testfixed_converted.csv', 'r') as f:
            contents = f.read()
            f.seek(0)
            o = StringIO()
            table.Table.from_csv(f).to_csv(o)
            conversion = o.getvalue()
            o.close()
        
        self.assertEqual(contents, conversion)