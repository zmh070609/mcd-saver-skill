# MCP 集成说明（MCP_INTEGRATION）

本 Skill 的全部外部能力均来自 **麦当劳中国官方 MCP Server**（仓库：`M-China/mcd-mcp-server`）。

## 一、使用的 MCP Server

| 项目 | 内容 |
|------|------|
| Server | 麦当劳中国官方 MCP Server |
| 地址 | `https://mcp.mcd.cn` |
| 协议 | Streamable HTTP（支持 MCP 2025-06-18 及之前版本） |
| 鉴权 | `Authorization: Bearer <MCP Token>`（在 [open.mcd.cn/mcp](https://open.mcd.cn/mcp) 用手机号登录申请） |
| 限流 | 每 Token 每分钟 600 次请求 |

接入配置示例见 `mcp-config.example.json`。

## 二、使用的 MCP Tool

| 工具 | 用途 | 在本 Skill 中的作用 |
|------|------|--------------------|
| `now-time-info` | 获取当前时间 | 判断营业/活动时段，作为流程起点 |
| `query-nearby-stores` | 查询附近门店 | 根据用户给出的城市/地址锁定门店 |
| `query-meals` | 查询门店可售餐品 | 拉取菜单供用户选餐 |
| `query-store-coupons` | 查询门店可用券 | 获取该门店下可使用的优惠券 |
| `available-coupons` | 麦麦省券列表查询 | 获取当前可领取的优惠券 |
| `auto-bind-coupons` | 麦麦省一键领券 | 一键领取所有可领的券 |
| `query-my-coupons` | 我的优惠券查询 | 汇总账户可用券 |
| `calculate-price` | 商品价格计算 | 按官方规则计算券后应付总价 |

工具参数明细见 `references/tools.md`。

## 三、调用流程

```
用户：「帮我省钱点麦当劳」
  │
  ├─ ① now-time-info ──── 获取当前时间（判断时段）
  ├─ ② query-nearby-stores ──── 查附近门店，用户确认门店
  ├─ ③ query-meals ──── 拉取菜单，用户选餐
  ├─ ④ query-store-coupons / query-my-coupons ──── 查可用券
  ├─ ⑤ available-coupons + auto-bind-coupons ──── 有可领券则一键领取
  ├─ ⑥ calculate-price ──── 带券计算应付总价
  │
  └─ ⑦ 本地最省组合算法（scripts/best_combo.py）
         对比「原价 / 各券后价」，输出最省方案与节省金额
```

## 四、业务价值

- **对学生等价格敏感用户**：把「查店、查券、领券、比价」四步压成一句话，解决优惠券散落各处、忘记领取、不会叠加的问题。
- **对麦当劳**：官方 MCP 能力直达真实消费场景，领券即转化，提升核销率。
- **可扩展性**：菜单与价格能力（`query-meals` / `calculate-price`）已预留，后续可自然延伸出「预算内凑单」「套餐推荐」等玩法。
