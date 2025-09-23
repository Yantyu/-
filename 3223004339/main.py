import jieba
import math
import argparse
from collections import Counter

# 中文停用词列表
stop_words = {"的", "了", "在", "是", "我", "有", "和", "就", "不", "人", "都", "一", "一个", "上", "也", "很", "到",
              "说", "要", "去", "你", "会", "着", "没有", "看", "好", "自己", "这", "从", "自从",
              "于是", "向", "按照", "经过", "为了", "根据", "常常", "几乎", "可是", "可"}

# 中文文本预处理函数
def preprocess(text):
    """
    对输入文本进行分词，并去除停用词
    :param text: 输入文本
    :return: 经过处理的词语列表
    """
    # 使用 jieba 进行中文分词
    words = jieba.lcut(text)
    # 去除停用词
    words = [word for word in words if word not in stop_words]
    return words

# 计算余弦相似度
def cosine_similarity(text1, text2):
    """
    计算两个文本之间的余弦相似度
    :param text1: 第一个文本
    :param text2: 第二个文本
    :return: 余弦相似度
    """
    # 预处理文本
    words1 = preprocess(text1)
    words2 = preprocess(text2)

    # 统计词频
    counter1 = Counter(words1)
    counter2 = Counter(words2)

    # 获取所有唯一的词汇
    all_words = set(words1).union(set(words2))

    # 将词频转换为向量
    vector1 = [counter1.get(word, 0) for word in all_words]
    vector2 = [counter2.get(word, 0) for word in all_words]

    # 计算点积
    dot_product = sum(v1 * v2 for v1, v2 in zip(vector1, vector2))

    # 计算向量的模
    magnitude1 = math.sqrt(sum(v1 ** 2 for v1 in vector1))
    magnitude2 = math.sqrt(sum(v2 ** 2 for v2 in vector2))

    # 计算余弦相似度
    if magnitude1 == 0 or magnitude2 == 0:
        return 0  # 避免除以零
    else:
        return dot_product / (magnitude1 * magnitude2)

def main():
    """
    主函数，负责解析命令行参数，读取文件，计算相似度，并输出结果
    """
    # 创建 ArgumentParser 对象
    parser = argparse.ArgumentParser(description="论文查重")

    # 添加参数
    parser.add_argument('file1', type=str, help='原始文件路径')
    parser.add_argument('file2', type=str, help='修改后的文件路径')
    parser.add_argument('output_file', type=str, help='输出结果文件路径')

    # 解析命令行参数
    args = parser.parse_args()

    try:
        # 读取文件
        with open(args.file1, "r", encoding="utf-8") as f1:
            content1 = f1.read()
        with open(args.file2, "r", encoding="utf-8") as f2:
            content2 = f2.read()
    except FileNotFoundError as e:
        print(f"文件读取失败: {e}")
        return
    except Exception as e:
        print(f"读取文件时发生未知错误: {e}")
        return

    # 计算并输出相似度
    similarity = cosine_similarity(content1, content2)
    print(f"两个文本的余弦相似度: {similarity:.2%}")
    re = f"{args.file1}和{args.file2}的相似度为{similarity:.2%}"

    try:
        # 将结果写入输出文件
        with open(args.output_file, "w", encoding="utf-8") as f3:
            f3.write(re)
    except Exception as e:
        print(f"写入输出文件时发生错误: {e}")
        return

if __name__ == "__main__":
    main()
