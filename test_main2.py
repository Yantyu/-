import unittest
import os
import tempfile
from unittest.mock import patch
import argparse
from main import main


class TestPlagiarismChecker(unittest.TestCase):

    def setUp(self):
        # 创建临时目录和文件
        self.temp_dir = tempfile.TemporaryDirectory()
        self.file1_path = os.path.join(self.temp_dir.name, "file1.txt")
        self.file2_path = os.path.join(self.temp_dir.name, "file2.txt")
        self.output_file_path = os.path.join(self.temp_dir.name, "output.txt")

        # 写入测试内容
        with open(self.file1_path, "w", encoding="utf-8") as f1:
            f1.write("这是一个测试文本。")
        with open(self.file2_path, "w", encoding="utf-8") as f2:
            f2.write("这也是一个测试文本。")

    def tearDown(self):
        # 清理临时目录
        self.temp_dir.cleanup()

    def test_file_read_success(self):
        """测试文件读取成功"""
        with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
                file1=self.file1_path, file2=self.file2_path, output_file=self.output_file_path)):
            main()
            # 检查输出文件是否存在
            self.assertTrue(os.path.exists(self.output_file_path))


    def test_output_file_write_success(self):
        """测试结果写入成功"""
        with patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(
                file1=self.file1_path, file2=self.file2_path, output_file=self.output_file_path)):
            main()
            # 检查输出文件内容
            with open(self.output_file_path, "r", encoding="utf-8") as f:
                content = f.read()
            self.assertIn("相似度", content)



if __name__ == "__main__":
    unittest.main()