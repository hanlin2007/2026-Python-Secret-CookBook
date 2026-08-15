#!/usr/bin/env python3
# fix_issues.py

# ！！学完了之后再回头看之前 AI 写的代码，就知道有多草台了。两个不超过 100 行的代码，还到处都灌了水。
# 这是第二个阅读、复盘的 AI 代码的实战，尝试对多文件、多包、模块系统进行学习

import os
from minio import Minio

# 首先是关于环境，这个项目之前使用的是虚拟环境，在 start_demo.sh 中找到了虚拟环境的激活命令。虚拟环境以一个 venv 的目录存在
# 可以 which python 并在 vscode 中指定


# 功能函数和 main 主入口分开，第一个修复函数
def fix_minio_files() -> None:
    """修复MinIO中缺失的文件，目前问题，预取器访问发现MinIO中不存在文件"""
    # 查一下函数参数标签其实很好懂，一个Mini存储服务
    client = Minio(
        "localhost:9000",
        access_key="minioadmin",
        secret_key="minioadmin",
        secure=False
    )

    # minio-data 目录下的父文件夹名称：桶
    bucket_name = "models"

    # 预取器尝试访问的文件名列表
    missing_files = ['layer0', 'layer1', 'layer2', 'layer3']

    for file in missing_files:
        try:
            # 在项目根目录下创建的 /tmp 目录
            file_path = f"/tmp/{file}"

            # 使用 open 方式打开文件 f.write()
            with open(file_path, 'wb') as f:
                # encode() 把字符按 encode 参数编码，二进制 "x" 字符串
                f.write(f"AAT-prefetch-test-{file}".encode() + b"x" * 100)

            # 在 minio 存储服务的对象中，每次加入一个对象，看函数的参数 “对象名”、“文件的路径名”
            client.fput_object(bucket_name, file, file_path)

            print(f"✅ 修复预取文件: {file}")
        except Exception as e:
            print(f"❌ 修复失败 {file}: {e}")


def improve_compression():
    """改进压缩策略"""

    # 从包里面选模块，包可以管理多个模块，一个文件就是一个模块，导入一个类
    from my_modules.aat_compression import CompressionManager

    # 基于类创建对象
    compressor = CompressionManager()

    # 测试更智能的压缩决策，创建了三个元组的列表，每个元组一个字符串名，一个比特流
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

    # 总之这就完了，全是玩具测试，硬写的玩具文件，没有真实文件


def analyze_prefetch_issue():
    """分析预取命中率问题"""
    print("\n🔍 分析预取命中率问题:")

    # 从测试日志可以看出问题：
    issues = [
        "1. 预取器尝试访问简化文件名 (layer0 vs layer0.bin)",
        "2. 预取与实际访问的文件名不匹配",
        "3. 需要改进预取逻辑的文件名映射"
    ]

    for issue in issues:
        print(f"   - {issue}")
    # 要是知道你就是这样分析问题的会被气死。依次访问字符串列表的元素输出
    # 然后在下面假模假样的给出解决方案

if __name__ == "__main__":
    print("🚀 开始修复AAT-TS系统问题...")

    fix_minio_files()
    improve_compression()
    analyze_prefetch_issue()

    print("\n🎯 修复建议:")
    print("1. 更新预取器逻辑，正确处理文件扩展名")
    print("2. 改进压缩决策阈值")
    print("3. 优化缓存策略配置")
