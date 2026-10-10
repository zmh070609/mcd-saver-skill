# 麦麦省钱助手（MCD Saver）

> 基于 **麦当劳中国官方 MCP 服务** 开发的省钱点餐 Skill，帮你在 WorkBuddy 里用最少的钱吃上麦当劳：查附近门店 → 查券/一键领券 → 选餐算最省组合。

本仓库为 **2026 麦当劳程序员创意开发大赛** 参赛作品，使用 WorkBuddy 辅助开发。

---

## 一、功能亮点

| 能力 | 说明 |
|------|------|
| 📍 附近门店 | 根据城市/地址查询最近的麦当劳门店 |
| 🎟️ 查券 + 领券 | 查门店可用券 + 麦麦省可领券，一键领取 |
| 💰 最省组合 | 选定餐品后计算券后价，给出最省点餐方案 |
| 🧾 透明汇报 | 原价 vs 券后价、省了多少，一目了然 |

---

## 二、基于的麦当劳 MCP 工具

本项目调用的工具均来自麦当劳中国官方 MCP Server（`M-China/mcd-mcp-server`）：

- `query-nearby-stores` 查询附近门店
- `query-store-coupons` 查询当前门店可用券
- `available-coupons` 麦麦省券列表查询
- `auto-bind-coupons` 麦麦省一键领券
- `query-my-coupons` 我的优惠券查询
- `query-meals` 查询当前门店可售卖餐品列表
- `calculate-price` 商品价格计算（支持带券）
- `now-time-info` 获取当前时间

完整参数见 `references/tools.md`。

---

## 三、MCP 接入说明

### 1. 申请 MCP Token
1. 打开 [麦当劳 MCP 开放平台](https://open.mcd.cn/mcp)
2. 点击右上角 **【登录】**，用**手机号验证登录**
3. 登录后右上角「登录」变为 **【控制台】**，点击进入
4. 点击 **激活** 申请 MCP Token，同意服务协议
5. 申请成功，**一键复制 Token**（请妥善保管，勿泄露）

### 2. 配置 MCP Server
将下方配置粘贴到 WorkBuddy 的 MCP 配置中，替换 `YOUR_MCP_TOKEN` 为你的 Token：

```json
{
  "mcpServers": {
    "mcd-mcp": {
      "type": "streamablehttp",
      "url": "https://mcp.mcd.cn",
      "headers": {
        "Authorization": "Bearer YOUR_MCP_TOKEN"
      }
    }
  }
}
```

> 也可参考仓库内的 `mcp-config.example.json`。注意：麦当劳 MCP Server 仅支持 MCP 2025-06-18 及之前版本；每个 Token 每分钟最多 600 次请求。

### 3. 使用
将本 Skill 放入 WorkBuddy 的 skills 目录后，在对话中说「帮我省钱点麦当劳」，即可触发上述工作流程。

---

## 四、最省组合算法（演示）

`scripts/best_combo.py` 是一个可独立运行的演示脚本，模拟「给定餐品 + 可用券，求券后最低总价」：

```bash
python3 scripts/best_combo.py
```

算法假设单笔订单最多叠加 1 张券，支持「满减券」与「折扣券（封顶）」两类，输出推荐用券与节省金额。真实场景由麦当劳 MCP 的 `calculate-price` 工具按官方规则计算。

---

## 五、参赛声明

1. 本作品为 **2026 麦当劳程序员创意开发大赛** 参赛作品，由作者使用 WorkBuddy 辅助开发完成。
2. 本作品基于 **麦当劳中国官方 MCP 服务**（`M-China/mcd-mcp-server`）开发，仅使用其公开接口，遵守《麦当劳 MCP 服务规则》及麦当劳中国相关使用条款。
3. 本作品为**非商业、原创**项目，代码开源供评审与学习使用；麦当劳相关商标、权益归麦当劳中国所有。
4. MCP Token 由作者本人申请，仅用于连接官方服务，未以任何方式泄露或转售。
5. 如与官方规则冲突，以活动页面（麦当劳 GitHub 官方账号 `M-China`）公布的最新规则为准。

---

## 六、GitHub 提交指引（按官方 Issue 模板）

1. Fork / 创建公开仓库，将本仓库内容推送到个人 GitHub 公开仓库。
2. 前往麦当劳 GitHub 官方账号 `M-China` 的活动页面，找到指定的参赛 Issue 模板。
3. 按模板填写：项目介绍、参赛声明、MCP 接入说明、仓库链接等，提交即完成报名。

---

## 七、安全说明

- MCP Token 等同个人凭证，**请勿提交到仓库或发给他人**。
- 本 Skill 仅在本地调用麦当劳官方接口，不收集、不上传任何个人隐私。
