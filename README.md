# 📚 Free Library · 免费电子书下载站点推荐

一个专注于收集和推荐**免费电子书下载网站**的开源项目。本项目整理了 Z-Library、Anna's Archive 等主流免费电子书镜像站点的可用链接，并通过自动化手段持续检测各站点可达性，帮助你快速找到当前可访问的免费电子书资源。

> 站点链接随时可能失效或变更，本项目会**每小时自动检测**一次，并在页面上以 ✅ / ❌ 实时标记可用性，让你少走弯路。

## ✨ 项目特色

- **精选免费电子书站点** — 持续收录 Z-Library、Anna's Archive 等优质免费电子书下载镜像站
- **链接可用性实时检测** — 通过 GitHub Actions 每小时自动检测资源链接，可用标记 ✅，不可用标记 ❌
- **北京时间检测时间戳** — 每条链接均记录最近一次检测时间（格式 `yyyy-MM-dd HH:mm:ss`，北京时间），方便判断时效性
- **自动同步部署** — 检测结果更新后自动重新构建并部署到 GitHub Pages，页面内容始终与最新检测状态一致
- **美观的文档站点** — 基于 VitePress 构建，支持全文搜索、暗色主题、阅读时长统计等良好阅读体验

## 🔗 资源列表

所有免费电子书站点链接收录在 [docs/src/guide.md](docs/src/guide.md)，表格包含：

| 列 | 说明 |
|----|------|
| 资源 | 站点名称 + 跳转链接 |
| 状态 | ✅ 可访问 / ❌ 不可访问（每小时自动更新） |
| 简介 | 站点类型说明（如 Z-library 镜像站、安娜的档案镜像站） |
| 检测时间 | 最近一次检测时间（北京时间） |

## 🚀 快速开始

### 在线访问

直接访问部署在 GitHub Pages 上的站点即可查看最新可用的免费电子书下载链接。

### 本地预览

```bash
# 环境要求：Node.js >= 20，pnpm
pnpm install
pnpm docs:dev      # 本地开发预览
pnpm docs:build    # 构建生产版本
pnpm docs:preview  # 预览构建结果
```

## 🤖 自动化说明

项目通过 GitHub Actions 实现链接检测的自动化：

- **定时检测 + 部署**（[.github/workflows/auto-deploy.yml](.github/workflows/auto-deploy.yml)）
  - 每小时整点自动运行；
  - 先执行 [.github/scripts/check_links.py](.github/scripts/check_links.py) 检测 `guide.md` 中各站点链接可用性，更新状态与检测时间；
  - 随后自动构建并部署到 GitHub Pages，保证线上页面与最新检测结果一致；
  - 推送到 `main` 分支时同样会触发构建部署。
- **手动检测**（[.github/workflows/check-links.yml](.github/workflows/check-links.yml)）
  - 支持在 Actions 标签页手动触发，单独更新链接检测状态。

### 检测逻辑

`check_links.py` 采用浏览器请求头 + 跟随重定向的方式访问站点，只要服务器返回 HTTP 响应（含 4xx/5xx）即视为「可访问」（说明站点在线），仅在网络层错误（DNS 失败、连接超时/拒绝、证书错误等）时才标记为「不可访问」。

## 📁 项目结构

```
free-library/
├── .github/
│   ├── scripts/
│   │   └── check_links.py       # 资源链接检测脚本
│   └── workflows/
│       ├── auto-deploy.yml       # 自动检测 + 部署工作流
│       └── check-links.yml       # 链接检测（手动触发）
├── docs/
│   ├── .vitepress/
│   │   ├── config.mts            # VitePress 站点配置
│   │   └── configs/              # 导航 / 侧边栏等配置
│   └── src/
│       ├── index.md              # 首页
│       ├── guide.md              # 免费电子书站点资源列表
│       └── public/               # 静态资源（logo、二维码、图片等）
├── package.json
├── pnpm-lock.yaml
└── LICENSE
```

## 🛠 技术栈

| 技术 | 说明 |
|------|------|
| [VitePress](https://vitepress.dev/) | 静态站点生成器 |
| [Vue 3](https://vuejs.org/) | 前端框架 |
| [pagefind](https://pagefind.app/) | 离线全文搜索 |
| Python + urllib | 资源链接可用性检测脚本 |
| GitHub Actions | 定时检测与自动部署 |

## 🤝 贡献

欢迎补充更多优质、合法的免费电子书下载站点！你可以：

1. 在 [docs/src/guide.md](docs/src/guide.md) 中按表格格式新增站点链接；
2. 提交 Pull Request，CI 会自动检测链接可用性并更新状态。

> ⚠️ 请仅收录合法、合规的免费电子书资源站点。本项目不对站点的内容合法性负责，使用相关资源请遵守当地法律法规。

## 📄 许可证

[Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE)
