---
title: "Next-intl 完全指南：轻松实现 Next.js 应用国际化"
date: 2025-01-01
categories: [技术, React, Next.js]
tags: [next-intl, 国际化, React, Next.js]
toc: true
---

## 什么是 next-intl？

`next-intl` 是一个强大的国际化（i18n）库，专为 Next.js 应用程序设计。它提供了简单而灵活的方式来管理多语言内容，支持服务器端渲染（SSR）和客户端渲染。

## 安装和基本配置

首先，安装 `next-intl`：

```bash
npm install next-intl
```

### 配置 `next.config.js`

```javascript
const withNextIntl = require('next-intl/plugin')();

module.exports = withNextIntl({
  // 其他 Next.js 配置
});
```

## 创建语言文件

在项目根目录创建 `messages` 文件夹，为每种语言添加 JSON 文件：

`messages/zh.json`:
```json
{
  "Index": {
    "title": "欢迎使用 next-intl",
    "description": "这是一个多语言网站示例"
  }
}
```

`messages/en.json`:
```json
{
  "Index": {
    "title": "Welcome to next-intl",
    "description": "This is a multilingual website example"
  }
}
```

## 配置国际化中间件

在 `middleware.ts` 中设置语言路由：

```typescript
import createMiddleware from 'next-intl/middleware';

export default createMiddleware({
  // 支持的语言
  locales: ['zh', 'en'],
  
  // 默认语言
  defaultLocale: 'zh'
});

export const config = {
  // 匹配所有路由，除了 _next/static、_next/image 和 favicon.ico
  matcher: ['/((?!_next/static|_next/image|favicon.ico).*)']
};
```

## 在页面中使用国际化

### 服务器组件

```typescript
import { useTranslations } from 'next-intl';

export default function IndexPage() {
  const t = useTranslations('Index');

  return (
    <div>
      <h1>{t('title')}</h1>
      <p>{t('description')}</p>
    </div>
  );
}
```

### 客户端组件

```typescript
'use client';

import { useTranslations } from 'next-intl';

export default function ClientComponent() {
  const t = useTranslations('Index');

  return <div>{t('title')}</div>;
}
```

## 动态插值

支持在翻译中使用动态值：

`messages/zh.json`:
```json
{
  "Greeting": {
    "welcome": "欢迎, {name}!"
  }
}
```

```typescript
const t = useTranslations('Greeting');
return <div>{t('welcome', { name: 'Alice' })}</div>;
```

## 高级特性

### 复数形式

`messages/zh.json`:
```json
{
  "Items": {
    "count": "{count, plural, =0 {没有物品} one {# 个物品} other {# 个物品}}"
  }
}
```

```typescript
const t = useTranslations('Items');
return <div>{t('count', { count: 5 })}</div>;
```

### 格式化日期和数字

```typescript
import { useTranslations } from 'next-intl';

export default function DateExample() {
  const t = useTranslations();

  return (
    <div>
      {/* 根据语言环境自动格式化 */}
      <p>{new Intl.DateTimeFormat(locale).format(new Date())}</p>
      <p>{new Intl.NumberFormat(locale).format(1234.56)}</p>
    </div>
  );
}
```

## 最佳实践

1. 保持翻译文件组织清晰
2. 使用命名空间分组相关翻译
3. 利用 TypeScript 提供类型安全
4. 考虑性能，只加载必要的语言资源

## 结论

`next-intl` 极大地简化了 Next.js 应用的国际化过程。通过其直观的 API 和强大的功能，你可以轻松创建支持多语言的现代 Web 应用。

## 参考资源

- [next-intl 官方文档](https://next-intl-docs.vercel.app/)
- [Next.js 国际化指南](https://nextjs.org/docs/advanced-features/i18n-routing)
