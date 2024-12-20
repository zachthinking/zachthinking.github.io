---
layout: post
title: "Vue3 + ElementPlus 实现网页全屏功能：从头部到侧边栏的完美隐藏"
date: 2024-01-25
categories: 技术
tags: [Vue3, ElementPlus, 前端开发, 用户体验]
toc: true
---

## 全屏功能的意义

### 为什么需要全屏功能？

1. **沉浸式体验**
   - 减少干扰
   - 提升专注度
   - 增强内容可读性

2. **界面美观**
   - 隐藏多余元素
   - 突出核心内容
   - 提升视觉效果

## 技术实现方案

### 1. 全屏 API 简介

```javascript
// 浏览器全屏 API
interface FullscreenDocument extends Document {
  fullscreenElement: Element | null;
  exitFullscreen(): Promise<void>;
}

interface FullscreenElement extends HTMLElement {
  requestFullscreen(): Promise<void>;
}
```

### 2. Vue3 + ElementPlus 实现

#### 组件结构

```vue
<template>
  <el-container>
    <!-- 头部 -->
    <el-header v-if="!isFullscreen">
      <!-- 头部内容 -->
    </el-header>

    <el-container>
      <!-- 侧边栏 -->
      <el-aside v-if="!isFullscreen" width="200px">
        <!-- 侧边栏菜单 -->
      </el-aside>

      <!-- 主内容区 -->
      <el-main>
        <el-button @click="toggleFullScreen">
          {{ isFullscreen ? '退出全屏' : '进入全屏' }}
        </el-button>

        <!-- 页面主要内容 -->
      </el-main>
    </el-container>
  </el-container>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

// 全屏状态
const isFullscreen = ref(false)

// 全屏切换方法
const toggleFullScreen = () => {
  if (!isFullscreen.value) {
    enterFullscreen()
  } else {
    exitFullscreen()
  }
}

// 进入全屏
const enterFullscreen = () => {
  const element = document.documentElement
  if (element.requestFullscreen) {
    element.requestFullscreen()
  }
  isFullscreen.value = true
}

// 退出全屏
const exitFullscreen = () => {
  if (document.exitFullscreen) {
    document.exitFullscreen()
  }
  isFullscreen.value = false
}

// 监听全屏状态变化
const handleFullscreenChange = () => {
  isFullscreen.value = !!document.fullscreenElement
}

onMounted(() => {
  document.addEventListener('fullscreenchange', handleFullscreenChange)
})

onUnmounted(() => {
  document.removeEventListener('fullscreenchange', handleFullscreenChange)
})
</script>

<style scoped>
.fullscreen-container {
  width: 100%;
  height: 100vh;
}
</style>
```

### 3. 兼容性处理

```javascript
// 跨浏览器全屏 API 兼容
function requestFullScreen(element) {
  const methods = [
    'requestFullscreen',
    'webkitRequestFullScreen',
    'mozRequestFullScreen',
    'msRequestFullscreen'
  ]

  for (let method of methods) {
    if (element[method]) {
      element[method]()
      return true
    }
  }
  return false
}
```

## 高级功能

### 1. 快捷键支持

```javascript
const handleKeydown = (event) => {
  // F11 快捷键
  if (event.key === 'F11') {
    event.preventDefault()
    toggleFullScreen()
  }
}

onMounted(() => {
  window.addEventListener('keydown', handleKeydown)
})

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeydown)
})
```

### 2. 全屏状态样式

```vue
<style>
.fullscreen-mode {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 9999;
  background: white;
}
</style>
```

## 性能优化

### 1. 防抖处理

```javascript
import { debounce } from 'lodash-es'

const optimizedToggleFullScreen = debounce(toggleFullScreen, 300)
```

### 2. 状态管理

```javascript
// Pinia 状态管理
const useFullscreenStore = defineStore('fullscreen', {
  state: () => ({
    isFullscreen: false
  }),
  actions: {
    toggle() {
      this.isFullscreen = !this.isFullscreen
    }
  }
})
```

## 最佳实践

1. **用户体验**
   - 提供明确的全屏切换按钮
   - 支持键盘快捷键
   - 保持界面一致性

2. **性能考虑**
   - 避免频繁切换
   - 使用防抖
   - 优化重绘

3. **兼容性**
   - 检测浏览器支持
   - 提供降级方案

## 常见问题

### 1. 移动设备兼容

```javascript
// 检测移动设备
const isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)

if (isMobile) {
  // 移动设备可能需要特殊处理
}
```

### 2. 权限问题

```javascript
// 检查全屏权限
if (document.fullscreenEnabled) {
  // 支持全屏
} else {
  // 不支持全屏
  ElMessage.warning('当前浏览器不支持全屏')
}
```

## 总结

全屏功能不仅仅是一个技术实现，更是提升用户体验的重要手段。通过 Vue3 和 ElementPlus，我们可以轻松构建出既美观又实用的全屏交互。

关键点：
- 使用浏览器全屏 API
- 响应式处理界面元素
- 提供良好的用户交互

## 扩展阅读

- MDN 全屏 API 文档
- Vue3 最佳实践
- 用户交互设计指南
