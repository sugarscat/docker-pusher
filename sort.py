def process_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    # 分组
    hash_lines = [line for line in lines if line.startswith("#")]
    slash_lines = [line for line in lines if "/" in line and not line.startswith("#")]
    normal_lines = [line for line in lines if "/" not in line and not line.startswith("#")]

    # 排序（忽略大小写）
    hash_lines.sort(key=lambda x: x.lower())
    slash_lines.sort(key=lambda x: x.lower())
    normal_lines.sort(key=lambda x: x.lower())

    # 组装结果
    result = []
    result.extend(hash_lines)
    if hash_lines and (normal_lines or slash_lines):
        result.append("")  # 空行分隔
    result.extend(normal_lines)
    if normal_lines and slash_lines:
        result.append("")  # 空行分隔
    result.extend(slash_lines)

    # 覆盖写入同一个文件
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("\n".join(result))


# 使用示例
process_text_file("images.txt")