#!/usr/bin/env python3
# fix_issues.py

# ！！学完了之后再回头看之前 AI 写的代码，就知道有多草台了。两个不超过 100 行的代码，还到处都灌了水。
# 这是第二个阅读、复盘的 AI 代码的实战，也是回过头看 python 教程中的函数、多文件、包和模块 进行学习

# ==========================================================

# 二编：过了一晚，回头来看这个文件，感觉印象明显就不如 my_check_models 深，感觉很大一个原因就是对整个文件的结构不够清除，都没有弄明白整个文件的功能、代码层次。另一个原因是“自己写”和“简单看一遍”之间的巨大区别

"""
整个“假修复”部分其实就是三个核心函数，然后一个主程序入口

【核心功能】
    1. 在 minio 桶中写入三个文件，涉及 minio 的

"""

import os
from minio import Minio

# 首先是关于环境，这个项目之前使用的是虚拟环境，在 start_demo.sh 中找到了虚拟环境的激活命令。虚拟环境以一个 venv 的目录存在
# 可以 which python 并在 vscode 中指定


# ================ 第一部分：在 minio 桶中添加文件 ============

# 功能函数和 main 主入口分开，第一个修复函数
def fix_minio_files() -> None:
    """修复MinIO中缺失的文件，目前问题，预取器访问发现MinIO中不存在文件"""

    # 查一下函数参数标签其实很好懂，一个 Mini 存储服务
    # 启动服务，配置地址、账密等
    # client = Minio(
    #     "localhost:9000",
    #     access_key="minioadmin",
    #     secret_key="minioadmin",
    #     secure=False
    # )

    # # minio-data 目录下的父文件夹名称，即“桶 ”
    # bucket_name = "models"
    # missing_files = ['layer0', 'layer1', 'layer2', 'layer3']
    # # 预取器尝试访问的文件名列表，为文件路径做准备

    # for file in missing_files:
    #     try:
    #         file_path = f"/tmp/{file}"
    #         with open(file_path, 'wb') as f:
    #             f.write(f"AAT-prefetch-test-{file}".encode() + b"x" * 100)

    #         # 在 minio 存储服务的桶中，每次加入一个对象，看函数的参数 “文件对象名”、“文件的路径名”
    #         client.fput_object(bucket_name, file, file_path)
    #         print(f"修复预取文件: {file}")

    #     except Exception as e:
    #         print(f"修复失败 {file}: {e}")


# ============ 第二部分：

def improve_compression():
    """改进压缩策略"""

    # 一个文件夹就是一个 package 包，一个独立文件就是一个模块
    # 现在是从模块里导入定义的一个类 / 函数方法
   
    from my_packages.aat_compression import CompressionManager
    compressor = CompressionManager()  # 基于类创建对象

    # 测试更智能的压缩决策，创建了三个元组的列表，每个元组一个字符串名，一个比特流 (name,data)
    test_cases = [
        ('重复数据', b'x' * 100000),
        ('随机数据', os.urandom(50000)),
        ('混合数据', b'x' * 50000 + os.urandom(50000)),
    ]

    print("\n🔧 改进压缩测试:")

    # for 循环遍历解包贴标签
    for name, data in test_cases:
        # 先检查是否值得压缩，CompressionManager() 的 should_compress 方法
        should_compress = compressor.should_compress(
            data, min_savings=0.05)  # 5%节省才压缩

        if should_compress:
            # 返回压缩后的二进制流、压缩算法
            compressed, algo = compressor.compress(data)
            ratio = len(compressed) / len(data)
            print(f"  {name}: 压缩率 {ratio:.4f} (已压缩)")
        else:
            print(f"  {name}: 跳过压缩 (不经济)")


# ============= 第三部分：读列表硬 “输出”问题 ========================

def analyze_prefetch_issue():
    """分析预取命中率问题"""
    print("\n🔍 分析预取命中率问题:")

    issues = [
        "1. 预取器尝试访问简化文件名 (layer0 vs layer0.bin)",
        "2. 预取与实际访问的文件名不匹配",
        "3. 需要改进预取逻辑的文件名映射"
    ]

    for issue in issues:
        print(f"{issue}")
    
    # 要是知道你就是这样分析问题的会被气死。依次访问字符串列表的元素输出
    # 然后还在下面假模假样的给出解决方案

if __name__ == "__main__":
    print("🚀 开始修复AAT-TS系统问题...")

    fix_minio_files()
    improve_compression()
    analyze_prefetch_issue()

