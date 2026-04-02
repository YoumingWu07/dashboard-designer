"""
依赖检查和安装脚本

检查插件所需的Python依赖是否已安装，并提供安装指导。
"""

import sys
import subprocess
from pathlib import Path

# 依赖定义
REQUIRED_PACKAGES = {
    "python-docx": {
        "import_name": "docx",
        "version": ">=0.8.11",
        "description": "Word文档解析",
        "required_for": ["requirement-analyzer"]
    },
    "openpyxl": {
        "import_name": "openpyxl",
        "version": ">=3.1.2",
        "description": "Excel文件生成",
        "required_for": ["requirement-analyzer"]
    },
    "PyPDF2": {
        "import_name": "PyPDF2",
        "version": ">=3.0.0",
        "description": "PDF文档解析",
        "required_for": ["requirement-analyzer"]
    },
    "pyyaml": {
        "import_name": "yaml",
        "version": ">=6.0",
        "description": "YAML配置解析",
        "required_for": ["config_manager"]
    }
}

def check_package(package_name: str, import_name: str) -> bool:
    """
    检查单个包是否已安装

    Args:
        package_name: 包名（pip安装名）
        import_name: 导入名

    Returns:
        是否已安装
    """
    try:
        __import__(import_name)
        return True
    except ImportError:
        return False

def check_all_dependencies() -> dict:
    """
    检查所有依赖

    Returns:
        {
            "installed": [...],  # 已安装的包
            "missing": [...],    # 缺失的包
            "details": {...}     # 详细信息
        }
    """
    result = {
        "installed": [],
        "missing": [],
        "details": {}
    }

    for package_name, info in REQUIRED_PACKAGES.items():
        is_installed = check_package(package_name, info["import_name"])

        if is_installed:
            result["installed"].append(package_name)
        else:
            result["missing"].append(package_name)

        result["details"][package_name] = {
            **info,
            "installed": is_installed
        }

    return result

def get_install_command(missing_packages: list) -> str:
    """
    生成安装命令

    Args:
        missing_packages: 缺失的包列表

    Returns:
        安装命令字符串
    """
    packages_with_version = []
    for pkg in missing_packages:
        version = REQUIRED_PACKAGES[pkg]["version"]
        packages_with_version.append(f"{pkg}{version}")

    return f"pip install {' '.join(packages_with_version)}"

def install_dependencies(missing_packages: list = None) -> bool:
    """
    安装缺失的依赖

    Args:
        missing_packages: 要安装的包列表，如果为None则安装所有缺失的包

    Returns:
        是否安装成功
    """
    if missing_packages is None:
        result = check_all_dependencies()
        missing_packages = result["missing"]

    if not missing_packages:
        print("✓ 所有依赖已安装")
        return True

    packages_with_version = []
    for pkg in missing_packages:
        version = REQUIRED_PACKAGES[pkg]["version"]
        packages_with_version.append(f"{pkg}{version}")

    cmd = [sys.executable, "-m", "pip", "install"] + packages_with_version

    print(f"正在安装依赖: {' '.join(packages_with_version)}")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print("✓ 依赖安装成功")
            return True
        else:
            print(f"✗ 安装失败: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ 安装失败: {e}")
        return False

def print_status():
    """打印依赖状态"""
    result = check_all_dependencies()

    print("=" * 50)
    print("Dashboard Designer 依赖检查")
    print("=" * 50)

    if not result["missing"]:
        print("\n✓ 所有依赖已安装，插件可以正常使用\n")
    else:
        print(f"\n✗ 缺失 {len(result['missing'])} 个依赖:\n")
        for pkg in result["missing"]:
            info = result["details"][pkg]
            print(f"  - {pkg}{info['version']}")
            print(f"    用途: {info['description']}")
            print(f"    影响功能: {', '.join(info['required_for'])}")
            print()

        print("安装命令:")
        print(f"  {get_install_command(result['missing'])}")
        print()

        print("或运行:")
        print(f"  python3 {Path(__file__).parent / 'dependency_checker.py'} --install")
        print()

    print("已安装的依赖:")
    for pkg in result["installed"]:
        info = result["details"][pkg]
        print(f"  ✓ {pkg} - {info['description']}")

    print("=" * 50)

    return result


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Dashboard Designer 依赖管理')
    parser.add_argument('--check', action='store_true', help='检查依赖状态')
    parser.add_argument('--install', action='store_true', help='安装缺失的依赖')
    parser.add_argument('--json', action='store_true', help='JSON格式输出')

    args = parser.parse_args()

    if args.install:
        success = install_dependencies()
        sys.exit(0 if success else 1)
    elif args.check or True:
        result = check_all_dependencies()

        if args.json:
            import json
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print_status()

        sys.exit(0 if not result["missing"] else 1)


if __name__ == '__main__':
    main()
