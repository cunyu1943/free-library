---
# https://vitepress.dev/reference/default-theme-home-page
layout: home

hero:
  name: "村雨遥"
  text: "Free Library"
  tagline: 电子书免费下载网站推荐，每小时自动检查网站是否可用。
  image:
    src: imgs/site/logo.png
  actions:
    - theme: brand
      text: 资源列表
      link: /guide
    - theme: alt
      text: 在 GitHub 查看
      link: https://github.com/cunyu1943/free-library

features:
  - title: 精选免费电子书站点
    details: 收录 Z-Library、Anna's Archive 等资源站，以及 Project Gutenberg、书格、中文维基文库等公版书与开放授权数字图书馆，目前已整理 30 个资源链接。
    link: /guide
    linkText: 查看全部资源
  - title: 链接可用性实时检测
    details: 通过 GitHub Actions 每小时自动检测资源链接，可用标记 ✅，不可用标记 ❌，并在每条链接上记录北京时间检测时间戳。
    link: https://github.com/cunyu1943/free-library/actions
    linkText: 查看自动化流程
  - title: 自动同步部署
    details: 检测结果更新后自动重新构建并部署到 GitHub Pages，页面内容始终与最新检测状态一致，无需手动维护。
    link: https://cunyu1943.github.io/free-library/guide
    linkText: 访问在线站点
---

<HomeUnderline />
