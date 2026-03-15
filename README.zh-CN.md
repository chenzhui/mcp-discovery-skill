# MCP Discovery Skill

[English](./README.md)

这是一个给 Codex 用的 skill，用来判断一项任务到底应该：

- 继续手工完成
- 安装一个 Codex skill
- 还是值得引入一个 MCP server

这个 skill 主要针对两类场景：

- Codex 当前缺少某项系统能力，直接影响任务推进。
- Codex 虽然能做，但流程高频、重复、低效，已经值得评估专用 skill 或 MCP。

## Quick Start

1. 克隆仓库。
2. 把 `mcp-discovery-skill` 文件夹复制到 Codex skills 目录。
3. 重启 Codex。
4. 当你遇到能力缺口，或遇到高频低效流程时，显式调用 `$mcp-discovery-skill`。

Windows 示例：

```powershell
git clone https://github.com/chenzhui/mcp-discovery-skill.git
Copy-Item -Recurse .\mcp-discovery-skill "C:\Users\<你自己>\.codex\skills\public\"
```

## 它解决什么问题

- 识别能力缺口和低效率重复流程。
- 搜索公开 MCP 发现站点和 GitHub。
- 评估候选 MCP 与 skill。
- 不默认安装工具，而是先判断是否真的值得引入。
- 帮助在 `手工方案 / skill / MCP` 三者之间做更合理的选择。

## 仓库结构

```text
mcp-discovery-skill/
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── evaluation.md
│   └── markets.md
└── scripts/
    └── discover_candidates.py
```

## 目录说明

- `SKILL.md`：skill 的核心定义和工作流。
- `agents/openai.yaml`：面向 UI 的 skill 元数据。
- `references/markets.md`：默认优先搜索的 MCP 市场入口。
- `references/evaluation.md`：候选 MCP / skill 的评估准则。
- `scripts/discover_candidates.py`：辅助搜索脚本，用于发现候选工具。

## 默认搜索入口

这个 skill 默认从这些公开发现面开始搜索：

- `https://www.mcpworld.com`
- `https://smithery.ai`
- `https://glama.ai/mcp`

它们只是默认起点，不是绝对权威排序。

## 安装方式

### 作为本地 Codex skill 安装

1. 找到你的 Codex skills 目录。
   Windows 常见路径：
   `C:\Users\<你自己>\.codex\skills\public\`
2. 把整个 `mcp-discovery-skill` 文件夹复制进去。
3. 重启 Codex 或开启一个新会话。

最终目录结构应类似：

```text
$CODEX_HOME/skills/public/mcp-discovery-skill/
```

### 通过 Git 获取

```bash
git clone https://github.com/chenzhui/mcp-discovery-skill.git
```

然后把整个文件夹复制到你的 Codex skills 目录，再重启 Codex。

## 使用方式

需要时显式调用：

```text
$mcp-discovery-skill
```

典型用法：

- `Use $mcp-discovery-skill to find an MCP for VMware Workstation screenshots.`
- `Use $mcp-discovery-skill to decide whether this repetitive browser workflow should stay manual or become a skill.`
- `Use $mcp-discovery-skill to search for a tool that can reduce repeated Android emulator setup work.`

## 搜索辅助脚本

示例：

```bash
python scripts/discover_candidates.py "vmware workstation screenshot mcp" --limit 5
```

这个脚本只负责辅助发现候选项，不会默认自动安装第三方工具。

## 为什么不做强制自动安装

这个仓库刻意没有把“自动安装 MCP”做成默认动作。

原因是：

- 强一些的 agent 往往已经能自己阅读安装文档并完成安装。
- 真正更难、更值钱的是先判断“该不该装”。
- 先做发现和评估，会让这个 skill 更小、更稳、更容易复用。

## License

MIT。见 [LICENSE](./LICENSE)。
