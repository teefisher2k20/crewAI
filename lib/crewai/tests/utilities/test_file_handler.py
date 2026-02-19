import json
import os
import unittest
import uuid
from datetime import datetime

import pytest
from crewai.utilities.file_handler import FileHandler, PickleHandler


class TestFileHandler(unittest.TestCase):
    def setUp(self):
        self.unique_id = str(uuid.uuid4())
        self.txt_file = f"test_log_{self.unique_id}.txt"
        self.json_file = f"test_log_{self.unique_id}.json"
        self.no_ext_file = f"test_log_{self.unique_id}"

    def tearDown(self):
        files_to_remove = [
            self.txt_file,
            self.json_file,
            self.no_ext_file,
            self.no_ext_file + ".txt",
            "logs.txt",
        ]
        for f in files_to_remove:
            if os.path.exists(f):
                if os.path.isdir(f):
                    os.rmdir(f)
                else:
                    os.remove(f)

    def test_initialize_path_boolean(self):
        handler = FileHandler(True)
        self.assertEqual(handler._path, os.path.join(os.curdir, "logs.txt"))

    def test_initialize_path_string_txt(self):
        handler = FileHandler(self.txt_file)
        self.assertEqual(handler._path, self.txt_file)

    def test_initialize_path_string_json(self):
        handler = FileHandler(self.json_file)
        self.assertEqual(handler._path, self.json_file)

    def test_initialize_path_string_no_extension(self):
        handler = FileHandler(self.no_ext_file)
        self.assertEqual(handler._path, self.no_ext_file + ".txt")

    def test_initialize_path_invalid_type(self):
        with self.assertRaises(ValueError) as cm:
            FileHandler(123)  # type: ignore
        self.assertEqual(str(cm.exception), "file_path must be a string or boolean.")

    def test_log_text_format(self):
        handler = FileHandler(self.txt_file)
        handler.log(agent="TestAgent", message="Hello World")

        self.assertTrue(os.path.exists(self.txt_file))
        with open(self.txt_file, encoding="utf-8") as f:
            content = f.read()
            self.assertIn('agent="TestAgent"', content)
            self.assertIn('message="Hello World"', content)
            # Verify timestamp format (approximate)
            timestamp_part = content.split(": ")[0]
            datetime.strptime(timestamp_part, "%Y-%m-%d %H:%M:%S")

    def test_log_json_format(self):
        handler = FileHandler(self.json_file)
        handler.log(agent="JSONAgent", status="success")

        self.assertTrue(os.path.exists(self.json_file))
        with open(self.json_file, encoding="utf-8") as f:
            data = json.load(f)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["agent"], "JSONAgent")
            self.assertEqual(data[0]["status"], "success")
            self.assertIn("timestamp", data[0])

        # Test appending
        handler.log(agent="JSONAgent2", status="error")
        with open(self.json_file, encoding="utf-8") as f:
            data = json.load(f)
            self.assertEqual(len(data), 2)
            self.assertEqual(data[1]["agent"], "JSONAgent2")

    def test_log_json_corrupted_recovery(self):
        with open(self.json_file, "w", encoding="utf-8") as f:
            f.write("invalid json")

        handler = FileHandler(self.json_file)
        handler.log(agent="RecoverAgent")

        with open(self.json_file, encoding="utf-8") as f:
            data = json.load(f)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["agent"], "RecoverAgent")

    def test_log_exception_wraps_in_value_error(self):
        # Trigger an exception by using a directory name where a file is expected
        os.mkdir(self.no_ext_file)
        # Use a path that is actually a directory to cause an error when trying to open for writing
        handler = FileHandler(self.no_ext_file)  # will be no_ext_file + .txt, but we'll use no_ext_file

        # Manually set path to the directory
        handler._path = self.no_ext_file

        with self.assertRaises(ValueError) as cm:
            handler.log(message="test")
        self.assertIn("Failed to log message", str(cm.exception))


class TestPickleHandler(unittest.TestCase):
    def setUp(self):
        # Use a unique file name for each test to avoid race conditions in parallel test execution
        unique_id = str(uuid.uuid4())
        self.file_name = f"test_data_{unique_id}.pkl"
        self.file_path = os.path.join(os.getcwd(), self.file_name)
        self.handler = PickleHandler(self.file_name)

    def tearDown(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_initialize_file(self):
        self.assertFalse(os.path.exists(self.file_path))

        self.handler.initialize_file()

        self.assertTrue(os.path.exists(self.file_path))
        self.assertGreaterEqual(os.path.getsize(self.file_path), 0)

    def test_save_and_load(self):
        data = {"key": "value"}
        self.handler.save(data)
        loaded_data = self.handler.load()
        self.assertEqual(loaded_data, data)

    def test_load_empty_file(self):
        loaded_data = self.handler.load()
        self.assertEqual(loaded_data, {})

    def test_load_corrupted_file(self):
        with open(self.file_path, "wb") as file:
            file.write(b"corrupted data")
            file.flush()
            os.fsync(file.fileno())  # Ensure data is written to disk

        with pytest.raises(Exception) as exc:
            self.handler.load()

        assert str(exc.value) == "pickle data was truncated"
        assert "<class '_pickle.UnpicklingError'>" == str(exc.type)
