import unittest
import requests
from pymarc.record import Record
from read_marc import get_record

class TestGetRecord(unittest.TestCase):

    def test_get_record(self):
        self.r = requests.get('http://ilsnext.sandbox.kohalibrary.com/api/work/35736')
        self.record = get_record(self.r)
        self.assertIsInstance(self.record, Record)
        self.assertEqual(self.record.leader, '00336cam a2200097 i 4500')


if __name__ == '__main__':
    unittest.main()