"""
配置管理器

管理工作目录、项目配置和路径解析。
"""

import os
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import Optional, Dict, List, Tuple

# 默认配置
DEFAULT_CONFIG = {
    "workspace": {
        "config_file": "workspace.yaml",
        "env_var": "DASHBOARD_WORKSPACE"
    },
    "paths": {
        "projects_dir": "projects",
        "input_dir": "input",
        "output_dir": "output",
        "documents_dir": "input/documents",
        "images_dir": "input/images"
    },
    "output_subdirs": [
        "01_需求分析",
        "02_原型设计/ascii",
        "02_原型设计/html",
        "03_UI设计/ui-code"
    ]
}


class ConfigManager:
    """配置管理器"""

    def __init__(self, workspace_path: Optional[str] = None):
        """
        初始化配置管理器

        Args:
            workspace_path: 工作目录路径，如果为None则从环境变量读取
        """
        self.workspace_path = self._resolve_workspace_path(workspace_path)
        self.config = self._load_plugin_config()

    def _resolve_workspace_path(self, workspace_path: Optional[str]) -> Optional[Path]:
        """解析工作目录路径"""
        if workspace_path:
            return Path(workspace_path).resolve()

        # 从环境变量读取
        env_var = DEFAULT_CONFIG["workspace"]["env_var"]
        env_path = os.environ.get(env_var)
        if env_path:
            return Path(env_path).resolve()

        return None

    def _load_plugin_config(self) -> dict:
        """加载插件配置"""
        return DEFAULT_CONFIG

    def check_workspace(self) -> Tuple[bool, List[str]]:
        """
        检查工作目录是否已初始化

        Returns:
            (是否已初始化, 缺失的文件/目录列表)
        """
        if not self.workspace_path:
            return False, ["未指定工作目录"]

        missing = []

        # 检查 workspace.yaml
        config_file = self.workspace_path / self.config["workspace"]["config_file"]
        if not config_file.exists():
            missing.append(f"{self.config['workspace']['config_file']}")

        # 检查 projects 目录
        projects_dir = self.workspace_path / self.config["paths"]["projects_dir"]
        if not projects_dir.exists():
            missing.append(f"{self.config['paths']['projects_dir']}/")

        return len(missing) == 0, missing

    def init_workspace(self) -> Dict[str, str]:
        """
        初始化工作目录

        Returns:
            创建的文件/目录路径
        """
        if not self.workspace_path:
            raise ValueError("未指定工作目录")

        # 确保工作目录存在
        if not self.workspace_path.exists():
            self.workspace_path.mkdir(parents=True, exist_ok=True)

        created = {}

        # 创建 workspace.yaml
        config_file = self.workspace_path / self.config["workspace"]["config_file"]
        if not config_file.exists():
            self._create_workspace_config(config_file)
            created["config"] = str(config_file)

        # 创建 projects 目录
        projects_dir = self.workspace_path / self.config["paths"]["projects_dir"]
        if not projects_dir.exists():
            projects_dir.mkdir(parents=True, exist_ok=True)
            created["projects_dir"] = str(projects_dir)

        return created

    def _create_workspace_config(self, config_path: Path) -> None:
        """创建工作空间配置文件"""
        content = f"""# 工作空间配置
version: "1.0"
created_at: {datetime.now().strftime("%Y-%m-%d")}

# 最近项目 (自动维护)
recent_projects: []

# 默认配置
defaults:
  ui_style: tech-blue
  auto_create_dirs: true
"""
        config_path.write_text(content, encoding="utf-8")

    def create_project(self, project_name: str) -> Dict[str, str]:
        """
        创建新项目

        Args:
            project_name: 项目名称

        Returns:
            创建的文件/目录路径
        """
        if not self.workspace_path:
            raise ValueError("未指定工作目录")

        project_dir = self.workspace_path / self.config["paths"]["projects_dir"] / project_name
        created = {}

        # 创建项目目录结构
        dirs_to_create = [
            self.config["paths"]["documents_dir"],
            self.config["paths"]["images_dir"],
        ] + self.config["output_subdirs"]

        for dir_path in dirs_to_create:
            full_path = project_dir / dir_path
            if not full_path.exists():
                full_path.mkdir(parents=True, exist_ok=True)
                created[dir_path] = str(full_path)

        # 创建项目配置文件
        project_config = project_dir / "project.yaml"
        if not project_config.exists():
            self._create_project_config(project_config, project_name)
            created["project.yaml"] = str(project_config)

        # 创建外部工具配置模板
        external_config = project_dir / self.config["paths"]["input_dir"] / "external.yaml"
        if not external_config.exists():
            self._create_external_config_template(external_config)
            created["external.yaml"] = str(external_config)

        # 更新 workspace.yaml 的最近项目列表
        self._update_recent_projects(project_name)

        return created

    def _create_project_config(self, config_path: Path, project_name: str) -> None:
        """创建项目配置文件"""
        content = f"""# 项目配置
name: {project_name}
created_at: {datetime.now().strftime("%Y-%m-%d")}
version: "1.0"

# 项目信息
info:
  description: ""
  owner: ""

# 外部工具配置 (可选)
external_tools:
  figma:
    file_key: ""
  modao:
    project_id: ""
"""
        config_path.write_text(content, encoding="utf-8")

    def _create_external_config_template(self, config_path: Path) -> None:
        """创建外部工具配置模板"""
        content = """# 外部设计工具配置
# 用于对接 Figma、墨刀等设计工具

figma:
  enabled: false
  # file_key: "ABC123DEF456"

modao:
  enabled: false
  # project_id: "proj_abc123"
"""
        config_path.write_text(content, encoding="utf-8")

    def _update_recent_projects(self, project_name: str) -> None:
        """更新最近项目列表"""
        config_file = self.workspace_path / self.config["workspace"]["config_file"]
        if not config_file.exists():
            return

        content = config_file.read_text(encoding="utf-8")

        # 简单的YAML更新（不使用pyyaml依赖）
        lines = content.split("\n")
        new_lines = []
        in_recent = False
        recent_added = False

        for line in lines:
            if line.startswith("recent_projects:"):
                in_recent = True
                new_lines.append(line)
                # 添加新项目到列表开头
                new_lines.append(f"  - name: {project_name}")
                new_lines.append(f"    path: projects/{project_name}")
                new_lines.append(f"    last_accessed: {datetime.now().strftime('%Y-%m-%d')}")
                recent_added = True
            elif in_recent and line.startswith("  -") and not recent_added:
                # 保留原有项目
                new_lines.append(line)
            elif in_recent and line.startswith("defaults:"):
                in_recent = False
                new_lines.append(line)
            else:
                new_lines.append(line)

        config_file.write_text("\n".join(new_lines), encoding="utf-8")

    def list_projects(self) -> List[Dict[str, str]]:
        """
        列出所有项目

        Returns:
            项目列表，每个项目包含 name 和 path
        """
        if not self.workspace_path:
            return []

        projects_dir = self.workspace_path / self.config["paths"]["projects_dir"]
        if not projects_dir.exists():
            return []

        projects = []
        for project_path in projects_dir.iterdir():
            if project_path.is_dir():
                project_config = project_path / "project.yaml"
                projects.append({
                    "name": project_path.name,
                    "path": str(project_path),
                    "has_config": project_config.exists()
                })

        return projects

    def get_project_paths(self, project_name: str) -> Dict[str, Path]:
        """
        获取项目的各路径

        Args:
            project_name: 项目名称

        Returns:
            路径字典
        """
        if not self.workspace_path:
            raise ValueError("未指定工作目录")

        project_dir = self.workspace_path / self.config["paths"]["projects_dir"] / project_name

        return {
            "project": project_dir,
            "input": project_dir / self.config["paths"]["input_dir"],
            "output": project_dir / self.config["paths"]["output_dir"],
            "documents": project_dir / self.config["paths"]["documents_dir"],
            "images": project_dir / self.config["paths"]["images_dir"],
        }

    def resolve_path(self, template: str, project_name: Optional[str] = None) -> Path:
        """
        解析路径变量

        Args:
            template: 路径模板，如 "${output}/01_需求分析"
            project_name: 项目名称

        Returns:
            解析后的路径
        """
        if not self.workspace_path:
            raise ValueError("未指定工作目录")

        # 替换变量
        result = template
        result = result.replace("${workspace}", str(self.workspace_path))

        if project_name:
            project_dir = self.workspace_path / self.config["paths"]["projects_dir"] / project_name
            result = result.replace("${project}", str(project_dir))
            result = result.replace("${input}", str(project_dir / self.config["paths"]["input_dir"]))
            result = result.replace("${output}", str(project_dir / self.config["paths"]["output_dir"]))
            result = result.replace("${documents}", str(project_dir / self.config["paths"]["documents_dir"]))
            result = result.replace("${images}", str(project_dir / self.config["paths"]["images_dir"]))

        return Path(result)


def main():
    parser = argparse.ArgumentParser(description='配置管理工具')
    subparsers = parser.add_subparsers(dest='command', help='命令')

    # check 命令
    check_parser = subparsers.add_parser('check', help='检查工作目录')
    check_parser.add_argument('--path', required=True, help='工作目录路径')

    # init 命令
    init_parser = subparsers.add_parser('init', help='初始化工作目录')
    init_parser.add_argument('--path', required=True, help='工作目录路径')

    # create-project 命令
    create_parser = subparsers.add_parser('create-project', help='创建新项目')
    create_parser.add_argument('--workspace', required=True, help='工作目录路径')
    create_parser.add_argument('--name', required=True, help='项目名称')

    # list-projects 命令
    list_parser = subparsers.add_parser('list-projects', help='列出所有项目')
    list_parser.add_argument('--workspace', required=True, help='工作目录路径')

    args = parser.parse_args()

    if args.command == 'check':
        manager = ConfigManager(args.path)
        is_valid, missing = manager.check_workspace()
        if is_valid:
            print(f"✓ 工作目录已初始化: {args.path}")
        else:
            print(f"✗ 工作目录未初始化，缺少:")
            for item in missing:
                print(f"  - {item}")

    elif args.command == 'init':
        manager = ConfigManager(args.path)
        created = manager.init_workspace()
        print(f"✓ 工作目录已初始化: {args.path}")
        for name, path in created.items():
            print(f"  创建: {path}")

    elif args.command == 'create-project':
        manager = ConfigManager(args.workspace)
        created = manager.create_project(args.name)
        print(f"✓ 项目已创建: {args.name}")
        for name, path in created.items():
            print(f"  创建: {path}")

    elif args.command == 'list-projects':
        manager = ConfigManager(args.workspace)
        projects = manager.list_projects()
        if projects:
            print(f"项目列表 ({len(projects)} 个):")
            for p in projects:
                config_status = "✓" if p["has_config"] else "✗"
                print(f"  {config_status} {p['name']}")
        else:
            print("暂无项目")

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
