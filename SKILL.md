---
name: mcd-saver
description: 麦麦省钱助手——接入麦当劳中国 MCP 服务，帮你查附近门店、查可用券、一键领券，并算出最省点餐组合。当用户想省钱吃麦当劳、找优惠、领券、比价时使用。触发词：麦当劳省钱、麦麦领券、麦当劳优惠、最省点餐、麦当劳怎么点便宜。
version: "1.0.0"
license: MIT
display_name: 麦麦省钱助手
display_name_en: MCD Saver
description_zh: 麦麦省钱助手——接入麦当劳中国 MCP 服务，查附近门店、查可用券、一键领券，计算最省点餐组合。
description_en: MCD Saver — connect to McDonald's China MCP to find nearby stores, list & claim coupons, and compute the cheapest meal combo.
---

# 麦麦省钱助手

接入麦当劳中国 MCP 服务（https://mcp.mcd.cn），帮用户用最少的钱吃上麦当劳。

## 前置条件

- 已按 `mcp-config.example.json` 配置麦当劳 MCP Server，并填入你本人申请的 MCP Token。
- Token 申请与接入步骤见 `README.md` 的「MCP 接入说明」。
- 工具清单与参数见 `references/tools.md`（提取自麦当劳官方 MCP 文档）。

## 工作流程

当用户表达「想省钱吃麦当劳 / 找优惠 / 领券 / 比价」等意图时，按以下步骤：

1. **定位门店**：调用 `query-nearby-stores`（用户提供城市或地址），确认目标门店。
2. **查券 + 领券**：
   - `query-store-coupons` 查该门店当前可用券
   - `available-coupons` 查麦麦省可领券列表
   - `auto-bind-coupons` 一键领取（无需逐个指定）
   - `query-my-coupons` 确认已到手券
3. **选餐 + 算最省**：
   - `query-meals` 查该门店菜单
   - 用户选定餐品后，用 `calculate-price`（带上可用券）算券后价
   - 调用 `scripts/best_combo.py` 给出最省组合建议（演示算法，见文件头用法）
4. **汇报**：输出门店、已领券、推荐组合、原价 vs 券后价、省了多少。

## 注意事项

- 每个 MCP Token 每分钟最多 600 次请求，合理控制调用频率，避免触发 429 限流。
- 下单环节仅返回支付链接，AI 无法直接完成支付，需用户在麦当劳 App 内完成。
- Token 等同个人凭证，仅本地配置使用，切勿提交到仓库或发给他人。

## 工具速查

见 `references/tools.md`。
