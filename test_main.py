import unittest

# 导入待测试的函数
from main import cosine_similarity


class TestCosineSimilarity(unittest.TestCase):

    def test_identical_texts(self):
        """测试两个完全相同的文本的相似度是否为 1"""
        text1 = "我喜欢用Python编程。Python非常强大！"
        text2 = "我喜欢用Python编程。Python非常强大！"
        similarity = cosine_similarity(text1, text2)
        self.assertEqual(similarity, 1.0)

    def test_completely_different_texts(self):
        """测试两个完全不同的文本的相似度是否为 0"""
        text1 = "今天天气晴天"
        text2 = "Java是一种很棒的编程语言。"
        similarity = cosine_similarity(text1, text2)
        self.assertEqual(similarity, 0.0)

    def test_partial_overlap_texts(self):
        """测试两个部分重叠的文本的相似度"""
        text1 = "我喜欢用Python。"
        text2 = "Python是一种很棒的编程语言。"
        similarity = cosine_similarity(text1, text2)
        self.assertGreater(similarity, 0.0)
        self.assertLess(similarity, 1.0)

    def test_empty_and_non_empty_texts(self):
        """测试一个空文本与非空文本的相似度是否为 0"""
        text1 = ""
        text2 = "Python是一种很棒的编程语言。"
        similarity = cosine_similarity(text1, text2)
        self.assertEqual(similarity, 0.0)

    def test_single_word_match(self):
        """测试完全相同的单词文本的相似度是否为 1"""
        text1 = "Python"
        text2 = "Python"
        similarity = cosine_similarity(text1, text2)
        self.assertEqual(similarity, 1.0)

    def test_numeric_text_similarity(self):
        """测试包含数字的文本的相似度"""
        text1 = "Python 3.9 发布了"
        text2 = "Python 3.10 发布了"
        similarity = cosine_similarity(text1, text2)
        self.assertGreater(similarity, 0.0)
        self.assertLess(similarity, 1.0)


if __name__ == "__main__":
    unittest.main()
