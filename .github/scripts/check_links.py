#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""检测 guide.md 表格中资源链接是否可访问，并更新状态列与检测时间列。"""

import os
import re
import sys
import io
import datetime
import urllib.request
import urllib.error

# 强制 stdout 使用 UTF-8，避免在非 UTF-8 终端（如 Windows GBK）打印 emoji 时报错
if sys.stdout.encoding != "utf-8":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

MD_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "docs", "src", "guide.md")
MD_PATH = os.path.abspath(MD_PATH)


def extract_url(cell: str) -> str | None:
    """从表格单元格中提取第一个 Markdown 链接地址。"""
    m = re.search(r"\[[^\]]*\]\((https?://[^)]+)\)", cell)
    return m.group(1) if m else None


def is_accessible(url: str) -> bool:
    """尝试访问 URL，判断是否可以访问。

    判定原则：只要服务器给予了 HTTP 响应（含 2xx/3xx/4xx/5xx）即视为“可访问”，
    因为 4xx/5xx 也说明站点在线、服务正常响应；
    只有网络层错误（DNS 失败、连接超时/拒绝、证书错误等）才视为“不可访问”。
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;q=0.9,"
            "image/avif,image/webp,*/*;q=0.8"
        ),
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    }
    # 跟随重定向，最多 5 次
    opener = urllib.request.build_opener(
        urllib.request.HTTPRedirectHandler()
    )
    for attempt in range(2):
        try:
            req = urllib.request.Request(url, headers=headers, method="GET")
            with opener.open(req, timeout=20) as resp:
                # 读到响应即视为可访问（不限制具体状态码）
                resp.read(1024)
                return True
        except urllib.error.HTTPError as e:
            # 服务器返回了 HTTP 错误状态码，说明站点在线
            if e.code is not None:
                return True
        except (urllib.error.URLError, TimeoutError, OSError):
            # 网络层错误：DNS 失败、连接超时/拒绝、证书错误等
            continue
    return False


def main() -> None:
    # 北京时间（UTC+8）
    bj_tz = datetime.timezone(datetime.timedelta(hours=8))
    now = datetime.datetime.now(bj_tz).strftime("%Y-%m-%d %H:%M:%S")

    with open(MD_PATH, encoding="utf-8") as f:
        lines = f.readlines()

    changed = False
    # 跳过表头（前两行）与分隔行
    for idx in range(2, len(lines)):
        line = lines[idx]
        if not line.strip().startswith("|"):
            continue

        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        # 表格列：资源 | 状态 | 简介 | 检测时间
        if len(cells) < 4:
            continue

        url = extract_url(cells[0])
        if not url:
            continue

        reachable = is_accessible(url)
        status = "✅" if reachable else "❌"

        # 状态或检测时间变化则写回（检测时间每次都会更新）
        if cells[1] != status or cells[3] != now:
            cells[1] = status
            cells[3] = now
            lines[idx] = "| " + " | ".join(cells) + " |\n"
            changed = True
            print(f"{'可用' if reachable else '不可用'}: {url}")
        else:
            print(f"无变化: {url}")

    if changed:
        with open(MD_PATH, "w", encoding="utf-8") as f:
            f.writelines(lines)
        print("已更新 guide.md")
    else:
        print("无需更新")


if __name__ == "__main__":
    main()
