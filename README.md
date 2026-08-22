# VitePress 个人站点模板

基于 [VitePress](https://vitepress.dev/) 构建的个人站点模板，集成了丰富的社区插件与自定义主题样式，开箱即用。

## 功能特性

- **全文搜索** — 基于 [pagefind](https://pagefind.app/) 的离线全文搜索
- **RSS 订阅** — 通过 `vitepress-plugin-rss` 自动生成 RSS
- **Git 变更日志** — 基于 `@nolebase/vitepress-plugin-git-changelog` 自动记录页面修改历史
- **公告弹窗** — 自定义公告组件，支持文本、图片、按钮，5 秒自动关闭
- **打赏功能** — 集成 `vitepress-plugin-sponsor`，支持支付宝/微信二维码
- **站点统计** — 基于 [不蒜子](https://busuanzi.pure.js.org/) 的访问量与访客数统计
- **文章元信息** — 自动显示更新日期、字数统计、预估阅读时长
- **代码组图标** — `vitepress-plugin-group-icons` 为代码块添加语言图标
- **自定义样式** — 引用块、代码块、侧边栏图标、模糊隐藏、标记高亮等多套自定义样式
- **霞鹜文楷字体** — 全站使用 LXGW WenKai GB Screen R 字体
- **Hero 下划线动画** — 首页标题带 SVG 下划线装饰
- **暗色主题** — 默认启用深色模式
- **GitHub Pages 自动部署** — 配置了 GitHub Actions 工作流，推送到 `main` 分支自动构建部署

## 项目结构

```
.
├── .github/
│   └── workflows/
│       └── auto-deploy.yml       # GitHub Actions 自动部署
├── docs/
│   ├── .vitepress/
│   │   ├── configs/
│   │   │   ├── nav.ts            # 导航栏配置
│   │   │   └── sidebar.ts        # 侧边栏配置
│   │   ├── theme/
│   │   │   ├── components/
│   │   │   │   ├── ArticleMetadata.vue  # 文章元信息（字数/阅读时长）
│   │   │   │   ├── DataPanel.vue        # 站点访问量统计面板
│   │   │   │   ├── HomeUnderline.vue    # 首页标题下划线装饰
│   │   │   │   └── notice.vue           # 公告弹窗组件
│   │   │   ├── style/
│   │   │   │   ├── var.css              # CSS 变量与字体
│   │   │   │   ├── index.css            # 样式入口
│   │   │   │   ├── blockquote.css       # 引用块样式
│   │   │   │   ├── blur.css             # 模糊隐藏样式
│   │   │   │   ├── hidden.css           # 隐藏样式
│   │   │   │   ├── marker.css           # 标记高亮样式
│   │   │   │   ├── sidebarIcon.css      # 侧边栏图标样式
│   │   │   │   ├── vp-code.css          # 代码块样式
│   │   │   │   ├── vp-code-group.css    # 代码组样式
│   │   │   │   └── vp-code-title.css    # 代码标题样式
│   │   │   ├── untils/
│   │   │   │   └── functions.ts         # 工具函数（字数统计）
│   │   │   └── index.ts                 # 主题入口
│   │   └── config.mts                   # VitePress 站点配置
│   └── src/
│       ├── public/
│       │   ├── imgs/                    # 图片资源
│       │   └── svg/                     # SVG 图标
│       ├── index.md                     # 首页
│       ├── api-examples.md             # API 示例页
│       └── markdown-examples.md        # Markdown 扩展示例页
├── package.json
├── pnpm-lock.yaml
└── LICENSE                             # CC BY 4.0
```

## 快速开始

### 环境要求

- Node.js >= 20
- pnpm（推荐）

### 安装依赖

```bash
pnpm install
```

### 本地开发

```bash
pnpm docs:dev
```

### 构建生产

```bash
pnpm docs:build
```

### 预览构建结果

```bash
pnpm docs:preview
```

## 自定义配置

### 站点信息

编辑 [docs/.vitepress/config.mts](docs/.vitepress/config.mts) 修改站点标题、描述、语言等基础配置：

```ts
export default defineConfig({
  title: "你的站点名",
  description: "你的站点描述",
  lang: 'zh-CN',
  // ...
})
```

### 导航栏与侧边栏

- 导航栏：编辑 [docs/.vitepress/configs/nav.ts](docs/.vitepress/configs/nav.ts)
- 侧边栏：编辑 [docs/.vitepress/configs/sidebar.ts](docs/.vitepress/configs/sidebar.ts)

### 公告弹窗

编辑 [docs/.vitepress/theme/components/notice.vue](docs/.vitepress/theme/components/notice.vue) 修改公告内容，或在 [config.mts](docs/.vitepress/config.mts) 中通过 `AnnouncementPlugin` 配置。

### 打赏二维码

替换以下图片文件：

- `docs/src/public/imgs/award/alipay.jpg` — 支付宝收款码
- `docs/src/public/imgs/award/wechatpay.jpg` — 微信收款码

### 主题色与字体

编辑 [docs/.vitepress/theme/style/var.css](docs/.vitepress/theme/style/var.css) 修改 CSS 变量，包括品牌色、Hero 渐变色、字体等。

## 部署

项目已配置 GitHub Actions 自动部署工作流（[.github/workflows/auto-deploy.yml](.github/workflows/auto-deploy.yml)），推送到 `main` 分支即可自动构建并部署到 GitHub Pages。

如需手动部署，请参考 [VitePress 部署文档](https://vitepress.dev/guide/deploy)。

## 技术栈

| 技术 | 说明 |
|------|------|
| [VitePress](https://vitepress.dev/) | 静态站点生成器 |
| [Vue 3](https://vuejs.org/) | 前端框架 |
| [pagefind](https://pagefind.app/) | 离线全文搜索 |
| [不蒜子](https://busuanzi.pure.js.org/) | 站点访问统计 |
| [LXGW WenKai](https://github.com/lxgw/LxgwWenKai) | 霞鹜文楷字体 |

## Star 趋势

[![Star History Chart](https://api.star-history.com/svg?repos=cunyu1943/vitpress&type=Date)](https://star-history.com/#cunyu1943/vitpress&Date)

## 许可证

[Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE)
