---
layout: post
title: "HuggingFace 加速镜像最新可用地址（2026年10月实测）"
date: 2026-10-25 15:30:00 +0800
categories: [HuggingFace, 教程]
tags: [huggingface, 镜像, 加速, AI]
toc: true
related: [github-proxy-mirror, docker-desktop-mirror]
---

**最新说明**：HuggingFace 直连在国内时好时坏，即使能通速度也不理想。以下方案于 **2026 年 10 月 25 日在国内网络实测**（API 探测 + 10MB 真实下载测速）：

- `https://hf-mirror.com`（最推荐，下载速度约为直连的 2 倍）
- `https://aifasthub.com`（备用，略快于直连）
- `https://modelscope.cn`（魔搭社区，国产模型首选，不是镜像但更好用）

10MB 实测下载速度对比：

| 线路 | 速度 | 结论 |
|---|---|---|
| huggingface.co 直连 | 约 0.45 MB/s | 今天能通，但慢，且历史上经常直接断 |
| **hf-mirror.com** | **约 1.0 MB/s** | 稳定可用，首选 |
| aifasthub.com | 约 0.57 MB/s | 可作备用 |

## 用法一：网页直接换域名

把 `huggingface.co` 换成 `hf-mirror.com`，其余路径不变：

<div style="border:1px solid #e1e4e8;border-radius:6px;padding:16px;margin:16px 0;">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
    <strong>模型页 / 文件下载链接替换示例</strong>
    <button onclick="copyBlock('cmd-web')" style="padding:6px 12px;font-size:12px;cursor:pointer;border:1px solid #ccc;border-radius:4px;background:#fff;">一键复制</button>
  </div>
  <pre id="cmd-web" style="margin:0;font-size:13px;overflow:auto;background:#f6f8fa;padding:12px;border-radius:6px;">https://hf-mirror.com/gpt2/resolve/main/config.json</pre>
</div>

## 用法二：HF_ENDPOINT 环境变量（推荐）

`huggingface_hub`、`hf download`、`transformers`、`datasets` 等官方工具链都认 `HF_ENDPOINT`，设置一次全部生效：

<div style="border:1px solid #e1e4e8;border-radius:6px;padding:16px;margin:16px 0;">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
    <strong>Linux / macOS（写进 ~/.bashrc 或 ~/.zshrc）</strong>
    <button onclick="copyBlock('cmd-env')" style="padding:6px 12px;font-size:12px;cursor:pointer;border:1px solid #ccc;border-radius:4px;background:#fff;">一键复制</button>
  </div>
  <pre id="cmd-env" style="margin:0;font-size:13px;overflow:auto;background:#f6f8fa;padding:12px;border-radius:6px;">export HF_ENDPOINT=https://hf-mirror.com</pre>
</div>

<div style="border:1px solid #e1e4e8;border-radius:6px;padding:16px;margin:16px 0;">
  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;">
    <strong>Windows PowerShell</strong>
    <button onclick="copyBlock('cmd-ps')" style="padding:6px 12px;font-size:12px;cursor:pointer;border:1px solid #ccc;border-radius:4px;background:#fff;">一键复制</button>
  </div>
  <pre id="cmd-ps" style="margin:0;font-size:13px;overflow:auto;background:#f6f8fa;padding:12px;border-radius:6px;">$env:HF_ENDPOINT = "https://hf-mirror.com"</pre>
</div>

设置之后正常用官方命令即可，不用改任何代码：

```bash
pip install -U "huggingface_hub[cli]"
hf download gpt2                 # 新版命令
# 或旧版：huggingface-cli download gpt2
```

Python 代码里用 `from_pretrained(...)` 也一样，只要环境变量在，就会自动走镜像。

## 用法三：国产模型直接去魔搭

如果用的是通义千问、DeepSeek、GLM 等国产模型，[ModelScope（魔搭社区）](https://modelscope.cn) 通常比镜像更快更全，还有官方维护的 SDK：

```bash
pip install modelscope
modelscope download --model Qwen/Qwen2-0.5B
```

## 常见问题

**为什么直连时好时坏？**
HuggingFace 的页面和文件分布在多个域名和 CDN 上，国内到这些节点的路由不稳定，今天能通不代表明天能通。本文实测当天直连可用但只有 0.45 MB/s，拉一个几 GB 的模型要好几个小时。

**镜像安全吗？**
镜像本质是中转代理，理论上可以看到传输内容。**不要**在镜像站点登录 HuggingFace 账号，**不要**用镜像拉取需要授权的私有模型。公开模型下载后如担心完整性，可以和官方页面公布的文件哈希值比对。

**hf-mirror 会不会也失效？**
有可能。这类服务多为社区维护，本文会持续复测更新，建议收藏，失效时回来看最新列表。

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
        ☕ 如果这份实测帮你节省了时间，可以扫码支持一下
      </div>
    </div>
  </div>
