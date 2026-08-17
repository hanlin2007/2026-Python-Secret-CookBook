#!/usr/bin/env python3

# 再来看这个文件，这算是一个工具模块组件，没有入口，放在 packages 中被 import 导入
# 还是体现了多文件，函数式编程分离的思想，把每个复用的组件给拆开。
# 这就理解了整个系统的逻辑，最终一个调入口就构成了整个分层存储系统

import logging
import gzip
import zlib    # zlib library, which is based on GNU zip 一个压缩模块
import pickle
from enum import Enum

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger("AAT-Compression")

# logger.setLevel(0)

# ==================================================================

# 使用 Google 搜索 python logging 即可找到官方文档，有一个非常清晰的示例和详细的设计说明

# logger = logging.getLogger(__name__)  # 1) 创建 logger 对象

# def main():  
#     2) logger 的基本参数配置，如写入的文件名、详细等级（官方文档查）
#     logging.basicConfig(filename='myapp.log', level=logging.INFO)

#     logger.info('Started')   3) logger 的 info 打印函数
#     mylib.do_something()
#     logger.info('Finished')

# logger = logging.getLogger(__name__)

# def do_something():
#     logger.info('Doing something')

# INFO: __main__: Started
# INFO: mylib: Doing something
# INFO: __main__: Finished


# =================================================================



class CompressionAlgorithm(Enum):
    GZIP = "gzip"
    ZLIB = "zlib"
    NONE = "none"




class CompressionManager:
    def __init__(self, default_algorithm=CompressionAlgorithm.GZIP):
        self.default_algorithm = default_algorithm
        logger.info(f"压缩管理器初始化，默认算法: {default_algorithm.value}")

    def compress(self, data, algorithm=None):
        """压缩数据"""
        if algorithm is None:
            algorithm = self.default_algorithm

        if algorithm == CompressionAlgorithm.NONE or not data:
            return data, algorithm

        try:
            if algorithm == CompressionAlgorithm.GZIP:
                compressed = gzip.compress(data)
            elif algorithm == CompressionAlgorithm.ZLIB:
                compressed = zlib.compress(data)
            else:
                raise ValueError(f"不支持的压缩算法: {algorithm}")

            # 计算压缩率
            original_size = len(data)
            compressed_size = len(compressed)
            compression_ratio = compressed_size / original_size if original_size > 0 else 0

            logger.debug(f"压缩完成: {original_size} -> {compressed_size} "
                         f"(比率: {compression_ratio:.2f})")

            return compressed, algorithm

        except Exception as e:
            logger.error(f"压缩失败: {e}")
            return data, CompressionAlgorithm.NONE

    def decompress(self, data, algorithm):
        """解压数据"""
        if algorithm == CompressionAlgorithm.NONE or not data:
            return data

        try:
            if algorithm == CompressionAlgorithm.GZIP:
                decompressed = gzip.decompress(data)
            elif algorithm == CompressionAlgorithm.ZLIB:
                decompressed = zlib.decompress(data)
            else:
                raise ValueError(f"不支持的压缩算法: {algorithm}")

            logger.debug(f"解压完成: {len(data)} -> {len(decompressed)}")
            return decompressed

        except Exception as e:
            logger.error(f"解压失败: {e}")
            return data

    def should_compress(self, data, min_savings=0.1):
        """判断是否值得压缩"""
        if not data or len(data) < 1024:  # 小于1KB不压缩
            return False

        # 测试压缩
        test_compressed, _ = self.compress(data[:min(8192, len(data))])
        savings = 1 - (len(test_compressed) / len(data))

        return savings >= min_savings
