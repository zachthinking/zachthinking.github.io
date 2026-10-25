---
layout: post
title: "Everything 下载与使用教程：Windows 文件搜索神器（2026年10月实测）"
date: 2026-10-25 16:30:00 +0800
categories: 软件
tags: [Windows, 文件搜索, 效率工具, 系统工具, 下载]
toc: true
related: [github-proxy-mirror, docker-desktop-mirror]
---

**最新说明**：2026 年 10 月 25 日在国内网络实测，Everything 官网（voidtools.com）**可以直连**，当前最新版 **1.4.1.1032**，2MB 安装包实测约 5 秒下完（约 400KB/s）。

- 官网地址：`https://www.voidtools.com/`
- x64 安装版直链（多语言，含简体中文）：

<div style="border:1px solid #e1e4e8;border-radius:6px;padding:16px;margin:16px 0;">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
    <strong>Everything 1.4.1.1032 x64 安装版（官方直链）</strong>
    <button onclick="copyBlock('dl-setup')" style="padding:6px 12px;font-size:12px;cursor:pointer;border:1px solid #ccc;border-radius:4px;background:#fff;">一键复制</button>
  </div>
  <pre id="dl-setup" style="margin:0;font-size:13px;overflow:auto;background:#f6f8fa;padding:12px;border-radius:6px;">https://www.voidtools.com/Everything-1.4.1.1032.x64-Setup.exe</pre>
</div>

- 便携版（免安装 zip）：`https://www.voidtools.com/Everything-1.4.1.1032.x64.zip`
- 商店版：Microsoft Store 搜 "Everything" 也可安装

<div style="border-left:4px solid #d97706;background:#fffbeb;padding:12px 16px;margin:16px 0;font-size:14px;color:#664d03;">
  ⚠️ <strong>别去第三方下载站。</strong>Everything 安装包只有 2MB，官网直连完全够用；下载站的"高速下载器"普遍捆绑全家桶。认准 voidtools.com。
</div>

## Everything 是什么

Windows 自带的搜索找文件要等几秒到几分钟，Everything 把百万级文件的搜索压缩到 **100 毫秒以内**——你边打字，结果边出来。它由 voidtools 开发，免费、无广告，内存占用约 10-30MB，是 Windows 上公认的文件搜索标配。

![Everything 界面](/assets/images/posts/2024-01-23-everything/Everything.Search.Window.png)

## 装好后建议先改的 3 个设置

1. **开机自启**：工具 → 选项 → 常规 → 勾选「随系统启动」（安装版默认已开）
2. **快捷键唤起**：工具 → 选项 → 快捷键 → 给「显示窗口」绑一个顺手的组合键（比如 `Alt + 空格`），之后任何时候一按就出搜索框
3. **中文界面**：安装时选了简体中文就不用管；如果界面是英文，工具 → 选项 → 常规 → 语言 → 简体中文

## 搜索语法速查

直接在搜索框输入，组合使用：

```
*.pdf              所有 PDF 文件
doc 2026           文件名同时含 "doc" 和 "2026"
size:>1GB          大于 1GB 的文件
modified:today     今天修改过的文件
ext:mp4;mkv        只要 mp4 和 mkv
path:"D:\工作"      限定在指定目录下搜
```

最常用的就前四个，记住能解决 90% 的日常搜索。

## 高级玩法（用得少但值得知道）

- **正则搜索**：搜索 → 勾选「正则表达式」，比如 `^project.*\.(txt|md)$` 匹配 project 开头的文本文件
- **网络位置**：可以索引局域网共享文件夹和 NAS，选项 → 索引 → NTFS/文件夹里添加
- **命令行**：自带 `es.exe` 命令行工具，可以写脚本批量找文件

## 常见问题

**第一次打开索引很慢？**
首次启动要建索引，百万文件约 1 分钟内完成，之后实时增量更新，不用再等。

**搜索结果不准 / 缺文件？**
工具 → 选项 → 索引 → 「强制重建」。另外 Everything 默认只索引 NTFS 分区，U 盘（FAT32/exFAT）需要在「文件夹」里手动添加。

**免费版和商业版区别？**
个人免费版功能完整，没有功能墙。官网的捐赠完全自愿。

## 同类工具对比

| | Everything | Windows 搜索 | Listary | utools |
|---|---|---|---|---|
| 搜索速度 | 极快（<100ms） | 慢（秒级） | 快 | 快 |
| 资源占用 | 低 | 高 | 低 | 中 |
| 价格 | 免费 | 系统自带 | 基础免费 | 基础免费 |
| 定位 | 纯文件搜索 | 系统综合搜索 | 搜索+启动器 | 插件平台 |

只要「找文件」这一件事，Everything 没有对手；想要启动器、剪贴板等扩展能力再看 Listary 或 utools。

## 总结

Everything 是 Windows 上少有的「装完就回不去」的工具：2MB、免费、毫秒级搜索。官网直连实测畅通，5 秒下完，没有理由再用系统自带搜索凑合。

<!-- Toast 提示 -->
<div id="copy-toast" style="position:fixed;top:20px;left:50%;transform:translateX(-50%);background:#333;color:#fff;padding:8px 16px;border-radius:6px;font-size:13px;opacity:0;transition:opacity 0.3s;z-index:9999;">已复制到剪贴板</div>

<script>
function copyBlock(id) {
  const text = document.getElementById(id).innerText;
  navigator.clipboard.writeText(text).then(function() {
    const toast = document.getElementById("copy-toast");
    toast.style.opacity = "1";
    setTimeout(function() { toast.style.opacity = "0"; }, 1500);
  });
}
</script>

  <!-- 公众号 + 赞赏区 -->
  <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:24px;margin-top:16px;">
    <div style="display:flex;flex-direction:column;align-items:center;">
      <img src="/assets/images/mp-zha-ke-ai-si-qr.jpg"
           style="width:200px;height:200px;border-radius:6px;" />
      <div style="font-size:13px;color:#666;margin-top:8px;text-align:center;max-width:220px;">
        📮 公众号「扎克爱思」：这里写工具，那里写生活——一个程序员如何让 AI 接管自己的工作、健康和投资
      </div>
    </div>
    <div style="display:flex;flex-direction:column;align-items:center;">
      <img src="https://cdn.zachthinking.com/donate_wechat.png"
           style="width:200px;height:200px;border-radius:6px;" />
      <div style="font-size:13px;color:#666;margin-top:8px;text-align:center;max-width:220px;">
        ☕ 如果这个教程帮你节省了时间，可以扫码支持一下
      </div>
    </div>
  </div>
