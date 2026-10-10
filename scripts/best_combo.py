#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
麦麦省钱助手 - 最省点餐组合计算（演示版）

输入：餐品清单 + 可用券清单
输出：应用券后总价最低的组合方案

券类型（简化模型）：
  - 满减券  {"type": "reduce",   "threshold": 30, "amount": 8}   满30减8
  - 折扣券  {"type": "discount", "rate": 0.9, "cap": 20}         9折，封顶省20元

规则（演示假设）：单笔订单最多叠加 1 张券。
真实计价由麦当劳 MCP 的 calculate-price 工具按官方规则执行。

用法：
  python3 best_combo.py
  # 自定义：修改 main() 里的 meals / coupons 即可
"""

from typing import Dict, List


def apply_coupon(total: float, c: Dict) -> float:
    """对总价 total 应用单张券 c，返回券后价。"""
    if c["type"] == "reduce":
        if total >= c["threshold"]:
            return total - c["amount"]
        return total
    if c["type"] == "discount":
        save = total * (1 - c["rate"])
        if "cap" in c and save > c["cap"]:
            save = c["cap"]
        return total - save
    return total


def calc(meals: List[Dict], coupons: List[Dict]):
    """枚举「不加券 / 各加一张券」，返回最低价方案。"""
    base = sum(m["price"] for m in meals)
    best = {"coupon": None, "total": base, "save": 0.0}
    for c in coupons:
        total = apply_coupon(base, c)
        save = round(base - total, 2)
        if save > best["save"]:
            best = {"coupon": c["name"], "total": round(total, 2), "save": save}
    return round(base, 2), best


def main():
    meals = [
        {"name": "巨无霸套餐", "price": 29.5},
        {"name": "麦辣鸡腿堡", "price": 21.0},
        {"name": "薯条(大)", "price": 12.0},
        {"name": "可乐(中)", "price": 9.5},
    ]
    coupons = [
        {"name": "满30减8", "type": "reduce", "threshold": 30, "amount": 8},
        {"name": "满50减15", "type": "reduce", "threshold": 50, "amount": 15},
        {"name": "全场9折(封顶20)", "type": "discount", "rate": 0.9, "cap": 20},
    ]

    base, best = calc(meals, coupons)

    print("=" * 42)
    print("麦麦省钱助手 · 最省组合测算（演示）")
    print("=" * 42)
    print("选购餐品:")
    for m in meals:
        print(f"  - {m['name']:<14} ¥{m['price']:.2f}")
    print(f"\n原价合计: ¥{base:.2f}")
    if best["coupon"]:
        print(f"推荐用券: {best['coupon']}")
        print(f"券后总价: ¥{best['total']:.2f}")
        print(f"为你省下: ¥{best['save']:.2f}")
    else:
        print("当前无可用券，按原价结算。")
    print("=" * 42)


if __name__ == "__main__":
    main()
