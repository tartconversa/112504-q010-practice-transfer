"""核对业务资料的格式和交接标识。"""
import csv
import unittest
from pathlib import Path

SAMPLES = Path(__file__).resolve().parents[1] / "samples"
SCHEMAS = {'skills': ['version', 'station', 'outcome', 'basis', 'comparable'], 'cohorts': ['person', 'cohort', 'tower', 'shift', 'joined', 'course', 'version'], 'observations': ['attempt', 'person', 'station', 'at', 'kind', 'score', 'received'], 'invitations': ['invite', 'person', 'round', 'day', 'outcome', 'probability'], 'shifts': ['person', 'tower', 'level', 'shift', 'start', 'stop'], 'refreshers': ['slot', 'tower', 'shift', 'date', 'station', 'instructor', 'capacity', 'state']}
REFERENCES = [('observations', 'person', 'cohorts', 'person'), ('observations', 'station', 'skills', 'station'), ('invitations', 'person', 'cohorts', 'person'), ('shifts', 'person', 'cohorts', 'person'), ('refreshers', 'station', 'skills', 'station')]
OBSERVED = [('observations', 'attempt', 'S2', 2), ('refreshers', 'slot', 'R1', 2), ('shifts', 'person', 'P1', 2)]

class Sources(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tables = {}
        for table, fields in SCHEMAS.items():
            with (SAMPLES / (table + ".csv")).open(encoding="utf-8", newline="") as stream:
                records = csv.DictReader(stream, strict=True)
                if records.fieldnames != fields:
                    raise ValueError(f"字段不一致：{table}")
                cls.tables[table] = list(records)

    def test_records_have_documented_columns(self):
        for table, rows in self.tables.items():
            with self.subTest(table=table):
                self.assertTrue(rows)
                self.assertTrue(all(None not in row and None not in row.values() for row in rows))

    def test_source_links(self):
        for left, field, right, target in REFERENCES:
            with self.subTest(table=left, field=field):
                keys = {row[field] for row in self.tables[left] if row[field]}
                self.assertTrue(keys)
                self.assertLessEqual(keys, {row[target] for row in self.tables[right]})

    def test_shared_source_records_are_available(self):
        for table, field, value, seen in OBSERVED:
            with self.subTest(table=table, field=field, value=value):
                self.assertGreaterEqual(sum(row[field] == value for row in self.tables[table]), seen)
