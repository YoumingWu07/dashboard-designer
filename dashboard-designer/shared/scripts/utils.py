"""
Dashboard Designer 共享工具函数
"""

import os
import re
from datetime import datetime
from pathlib import Path


def ensure_dir(path: str) -> Path:
    """确保目录存在，不存在则创建"""
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def sanitize_filename(name: str) -> str:
    """清理文件名，移除非法字符"""
    # 移除Windows和Linux不允许的字符
    illegal_chars = r'[<>:"/\\|?*]'
    return re.sub(illegal_chars, '_', name).strip()


def get_project_output_dir(project_name: str, base_dir: str = "output") -> Path:
    """获取项目输出目录"""
    safe_name = sanitize_filename(project_name)
    output_dir = Path(base_dir) / safe_name
    ensure_dir(output_dir)
    return output_dir


def get_timestamp() -> str:
    """获取当前时间戳字符串"""
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def read_file_content(file_path: str) -> str:
    """读取文件内容"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def write_file_content(file_path: str, content: str) -> None:
    """写入文件内容"""
    ensure_dir(os.path.dirname(file_path))
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)


def parse_file_extension(file_path: str) -> str:
    """获取文件扩展名（小写）"""
    return os.path.splitext(file_path)[1].lower()


def is_document_file(file_path: str) -> bool:
    """判断是否为文档文件"""
    ext = parse_file_extension(file_path)
    return ext in ['.txt', '.md', '.pdf', '.docx', '.doc', '.xlsx', '.xls']


def is_image_file(file_path: str) -> bool:
    """判断是否为图片文件"""
    ext = parse_file_extension(file_path)
    return ext in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp']


def get_file_type(file_path: str) -> str:
    """获取文件类型"""
    if is_document_file(file_path):
        return 'document'
    elif is_image_file(file_path):
        return 'image'
    else:
        return 'unknown'
