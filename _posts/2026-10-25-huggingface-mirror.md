---
layout: post
title: "hf-mirror.com：HuggingFace 国内镜像加速实测（2026年11月）"
date: 2026-10-25 15:30:00 +0800
modified_date: 2026-11-12
description: "2026 年 11 月国内实测 hf-mirror.com 与 aifasthub.com，提供 HuggingFace 模型网页下载、HF_ENDPOINT 环境变量和 hf download 配置方法。"
categories: [HuggingFace, 教程]
tags: [huggingface, hf-mirror, 镜像, 加速, AI]
toc: true
related: [github-proxy-mirror, docker-desktop-mirror]
---

**最新说明**：HuggingFace 直连在国内时好时坏，即使能通速度也不理想。以下方案于 **2026 年 11 月 12 日在国内网络实测**（API 探测 + 10MB 真实下载测速）：

- `https://hf-mirror.com`（首选，本次 10MB 下载约 1.85 MB/s）
- `https://aifasthub.com`（备用，本次测速更快，约 2.87 MB/s）
- `https://modelscope.cn`（魔搭社区，国产模型首选，不是镜像但更好用）

10MB 实测下载速度对比（单次测速仅反映本次国内网络环境）：

| 线路 | 速度 | 结论 |
|---|---|---|
| huggingface.co 直连 | 连接超时 | 本次未能完成下载 |
| **hf-mirror.com** | **约 1.85 MB/s** | 稳定可用，首选 |
| aifasthub.com | 约 2.87 MB/s | 本次速度更快，可作备用 |

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

## 不想下载模型：直接调用百炼大模型 API

如果只是做问答、翻译或 AI 应用，不一定要先把模型下载到本地。阿里云百炼提供通义千问等模型的 API，可以省去本地部署和显卡成本，适合先小量验证需求。

通过我的云小站可以领取一张 **8 折优惠券**，页面也提供百炼模型推理、知识库等产品。优惠券的适用产品、使用门槛和有效期以阿里云领取页及结算页为准。

<div style="border:1px solid #fed7aa;background:#fffaf5;border-radius:6px;padding:16px;margin:16px 0;">
  <a href="https://www.aliyun.com/minisite/goods?userCode=ovyc4rns"
     target="_blank"
     rel="sponsored nofollow noopener"
     data-cps-partner="aliyun"
     data-cps-product="bailian"
     data-cps-source-page="huggingface-mirror"
     data-cps-placement="model_api_section"
     style="display:inline-block;padding:10px 18px;border-radius:6px;background:#ea580c;color:#fff;text-decoration:none;font-weight:600;">
    领取阿里云 8 折优惠券
  </a>
  <p style="margin:12px 0 0;font-size:13px;color:#666;line-height:1.7;">
    推广说明：这是返佣链接。通过它购买符合条件的产品，我会获得返佣，不会增加你的购买成本；实际优惠与返佣均以阿里云规则为准。
  </p>
</div>

## 常见问题

**为什么直连时好时坏？**
HuggingFace 的页面和文件分布在多个域名和 CDN 上，国内到这些节点的路由不稳定，今天能通不代表明天能通。本文 2026 年 11 月 12 日复测时官网直连超时，两个镜像则都完成了 10MB 文件下载。

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
