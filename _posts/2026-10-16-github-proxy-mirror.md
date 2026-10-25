---
layout: post
title: "GitHub 加速镜像最新可用地址（2026年10月实测）"
date: 2026-10-25 12:00:00 +0800
categories: [GitHub, 教程]
tags: [github, 镜像, 加速, ghproxy]
toc: true
---

**最新说明**：GitHub 直连在国内时好时坏，raw 和 release 下载经常超时。以下加速地址于 **2026 年 10 月 25 日在国内网络实测**（raw 文件、release 附件、`git clone` 三种方式逐项验证）：

- `https://ghfast.top/`（三种方式全部通过）
- `https://gh-proxy.com/`（三种方式全部通过）
- `https://gh.llkk.cc/`（三种方式全部通过，偶发超时重试即可）
- `https://ghproxy.net/`（raw 和 `git clone` 可用；release 大文件不稳定，下载附件优先用前三个）

用法：**把原始 GitHub 链接完整拼在镜像地址后面**即可，不用改链接本身。

## 一键复制

<div style="border:1px solid #e1e4e8;border-radius:6px;padding:16px;margin:16px 0;">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
    <strong>git clone 加速（示例）</strong>
    <button onclick="copyBlock('cmd-clone')" style="padding:6px 12px;font-size:12px;cursor:pointer;border:1px solid #ccc;border-radius:4px;background:#fff;">一键复制</button>
  </div>
  <pre id="cmd-clone" style="margin:0;font-size:13px;overflow:auto;background:#f6f8fa;padding:12px;border-radius:6px;">git clone https://ghfast.top/https://github.com/用户名/仓库名</pre>
</div>

<div style="border:1px solid #e1e4e8;border-radius:6px;padding:16px;margin:16px 0;">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
    <strong>raw 文件加速（示例）</strong>
    <button onclick="copyBlock('cmd-raw')" style="padding:6px 12px;font-size:12px;cursor:pointer;border:1px solid #ccc;border-radius:4px;background:#fff;">一键复制</button>
  </div>
  <pre id="cmd-raw" style="margin:0;font-size:13px;overflow:auto;background:#f6f8fa;padding:12px;border-radius:6px;">https://ghfast.top/https://raw.githubusercontent.com/用户名/仓库名/分支/文件路径</pre>
</div>

<div style="border:1px solid #e1e4e8;border-radius:6px;padding:16px;margin:16px 0;">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
    <strong>release 附件加速（示例）</strong>
    <button onclick="copyBlock('cmd-release')" style="padding:6px 12px;font-size:12px;cursor:pointer;border:1px solid #ccc;border-radius:4px;background:#fff;">一键复制</button>
  </div>
  <pre id="cmd-release" style="margin:0;font-size:13px;overflow:auto;background:#f6f8fa;padding:12px;border-radius:6px;">https://ghfast.top/https://github.com/用户名/仓库名/releases/download/版本号/文件名</pre>
</div>

第一个镜像失效时，把前缀换成列表里的其他地址即可。

## 只下载单个文件：jsDelivr CDN

如果只需要仓库里的**单个源码文件**（不是 release 附件），用 jsDelivr 更稳——它是正规 CDN，国内有节点，基本不会失效：

<div style="border:1px solid #e1e4e8;border-radius:6px;padding:16px;margin:16px 0;">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
    <strong>jsDelivr 格式</strong>
    <button onclick="copyBlock('cmd-jsdelivr')" style="padding:6px 12px;font-size:12px;cursor:pointer;border:1px solid #ccc;border-radius:4px;background:#fff;">一键复制</button>
  </div>
  <pre id="cmd-jsdelivr" style="margin:0;font-size:13px;overflow:auto;background:#f6f8fa;padding:12px;border-radius:6px;">https://cdn.jsdelivr.net/gh/用户名/仓库名@分支/文件路径</pre>
</div>

注意 jsDelivr 的格式和镜像不同：不是拼接原链接，而是 `gh/用户名/仓库名@分支/路径`。它**不能**下载 release 附件，也不能 `git clone`。

## 怎么确认加速生效了

- `git clone`：速度从几 KB/s 提升到几百 KB/s 以上即为生效；
- 浏览器/ curl 下载：对比直连和镜像的同一文件，能下完且文件大小一致；
- 校验文件完整性：`shasum -a 256 文件名`，和 release 页面公布的校验值对比。

## 已失效地址（避坑）

以下曾经流行的地址，2026 年 10 月 25 日实测**已不可用**，如果老教程里看到请直接跳过：

- `ghproxy.com` / `mirror.ghproxy.com`（原最大镜像站，已关停）
- `github.moeyy.xyz`（连接失败）
- `ghproxy.cc`（连接失败）
- `hub.gitmirror.com`（连接失败）
- `gitclone.com`（404，已关停）
- `kkgithub.com`（连接失败）
- `gh.ddlc.top`（限流 429，偶尔可用）

## 常见问题

**为什么这些镜像经常换？**
这类服务多为个人/小团队用爱发电，服务器成本和风控压力大会导致关停或换域名，所以本文会持续更新。建议收藏，失效时回来看最新列表。

**镜像安全吗？**
镜像本质是中转代理，理论上可以看到传输内容。下载可执行文件时务必核对发布页的哈希值；**不要**在镜像地址后面拼接任何需要登录的链接。

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
        ☕ 如果这份列表帮你节省了时间，可以扫码支持一下
      </div>
    </div>
  </div>
