# workbuddy.md — 使用 WorkBuddy 开发的对话上下文记录

> 本项目由参赛者使用 WorkBuddy（AI 工作台）辅助开发。本文档为开发过程的对话上下文摘要，用于 WorkBuddy 联动活动专项奖励的核验。

## 开发环境

- 工具：WorkBuddy 桌面版（AI Agent 工作台）
- 方式：与 WorkBuddy AI 助手多轮对话驱动，由 AI 起草代码与文档，参赛者做决策、提供素材并执行提交
- 时间：2026 年 10 月 9 日 — 10 月 10 日

## 开发过程回顾

### 1. 赛题理解与信息核实（10 月 9 日）
- 参赛者向 WorkBuddy 提供活动文章链接，WorkBuddy 抓取并总结活动规则（基于麦当劳 MCP 开发 Skill、开源到 GitHub、按模板提 Issue 报名）。
- WorkBuddy 通过网络检索核实了麦当劳官方 MCP Server（`M-China/mcd-mcp-server`，`https://mcp.mcd.cn`）真实可用，确认报名前提（GitHub 账号 + MCP Token）。
- WorkBuddy 给出了 GitHub 注册与 MCP Token 申请的分步教程，参赛者自行完成注册与申请。

### 2. 功能选型（10 月 10 日）
- WorkBuddy 基于麦当劳 MCP 真实工具列表提出 3 个候选方案：省钱助手 / 点餐助手 / 积分管家。
- 参赛者选定「麦麦省钱助手」（查附近门店 → 查券/一键领券 → 算最省组合）。

### 3. 项目开发（10 月 10 日）
- WorkBuddy 参考本地已有 Skill 的标准格式（SKILL.md 结构），生成项目骨架：
  - `SKILL.md`：WorkBuddy 技能定义（查店 → 查券 → 领券 → 算最省的工作流）
  - `README.md`：项目介绍、安装方法、使用示例、参赛声明
  - `mcp-config.example.json`：MCP 接入配置模板（Token 占位符）
  - `references/tools.md`：所用麦当劳 MCP 工具速查（含入参/出参/限流说明）
  - `scripts/best_combo.py`：最省组合算法（单笔订单最多叠加 1 张券，支持满减券与折扣券封顶）
- WorkBuddy 在本地实际运行 `scripts/best_combo.py` 完成自测：模拟原价 ¥72 的点餐，命中「满 50 减 15」券后应付 ¥57，节省 ¥15，验证算法正确。

### 4. 开源与报名（10 月 10 日）
- WorkBuddy 逐步引导参赛者在 GitHub 网页端完成公开仓库创建与文件上传（网页拖拽方式，未使用命令行 git）。
- WorkBuddy 按官方要求补齐 `CONTEST_DECLARATION.md`（原文照抄官方仓库）、`MCP_INTEGRATION.md` 与本文件，并起草报名 Issue 文本。
- 参赛者在官方活动仓库按模板提交报名 Issue。

## 声明

以上过程真实发生于参赛者本人的 WorkBuddy 会话中，对话原始记录可在参赛者的 WorkBuddy 客户端历史中查验。
