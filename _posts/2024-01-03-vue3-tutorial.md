---
layout: post
title: "Vue 3 完全指南：从入门到实践"
date: 2024-01-03
categories: 技术
tags: [Vue3, JavaScript, 前端开发]
toc: true
---

Vue 3 是一个用于构建用户界面的渐进式框架，相比 Vue 2 带来了许多重要的改进和新特性。本文将全面介绍 Vue 3 的核心概念和使用方法。


## Vue 3 新特性概览

Vue 3 带来了以下主要改进：

- **Composition API**：更好的代码组织和逻辑复用
- **更快的渲染速度**：虚拟 DOM 重写，更优的 diff 算法
- **更小的包体积**：支持树摇优化
- **更好的 TypeScript 支持**
- **Teleport、Fragments、Suspense** 等新特性

## Composition API 详解

Composition API 是 Vue 3 最重要的特性之一，它提供了一种全新的组织组件逻辑的方式。

```javascript
import { ref, onMounted } from 'vue'

export default {
  setup() {
    // 响应式状态
    const count = ref(0)
    
    // 方法
    const increment = () => {
      count.value++
    }
    
    // 生命周期钩子
    onMounted(() => {
      console.log('组件已挂载')
    })
    
    // 返回给模板使用
    return {
      count,
      increment
    }
  }
}
```

## 响应式系统

Vue 3 的响应式系统使用 `Proxy` 替代了 Vue 2 的 `Object.defineProperty`，主要 API 包括：

- **ref**：用于基本类型的响应式
- **reactive**：用于对象的响应式
- **computed**：计算属性
- **watch/watchEffect**：侦听器

```javascript
import { ref, reactive, computed, watch } from 'vue'

// ref 示例
const count = ref(0)
console.log(count.value) // 0

// reactive 示例
const state = reactive({
  name: 'Vue 3',
  version: '3.0'
})

// computed 示例
const doubleCount = computed(() => count.value * 2)

// watch 示例
watch(count, (newValue, oldValue) => {
  console.log(`count 从 ${oldValue} 变为 ${newValue}`)
})
```

## 生命周期钩子

Vue 3 的生命周期钩子与 Vue 2 相似，但在 Composition API 中有了新的使用方式：

```javascript
import {
  onBeforeMount,
  onMounted,
  onBeforeUpdate,
  onUpdated,
  onBeforeUnmount,
  onUnmounted
} from 'vue'

export default {
  setup() {
    onBeforeMount(() => {
      // 组件挂载前
    })
    
    onMounted(() => {
      // 组件挂载后
    })
    
    // 其他生命周期钩子...
  }
}
```

## 实战示例

下面是一个简单的待办事项应用示例：

```vue
<template>
  <div class="todo-app">
    <input 
      v-model="newTodo" 
      @keyup.enter="addTodo"
      placeholder="添加新任务"
    >
    
    <ul>
      <li v-for="todo in todos" :key="todo.id">
        <input 
          type="checkbox" 
          v-model="todo.completed"
        >
        <span :class="{ completed: todo.completed }">
          {{ todo.text }}
        </span>
      </li>
    </ul>
  </div>
</template>

<script>
import { ref } from 'vue'

export default {
  setup() {
    const newTodo = ref('')
    const todos = ref([])
    
    const addTodo = () => {
      if (newTodo.value.trim()) {
        todos.value.push({
          id: Date.now(),
          text: newTodo.value,
          completed: false
        })
        newTodo.value = ''
      }
    }
    
    return {
      newTodo,
      todos,
      addTodo
    }
  }
}
</script>

<style>
.completed {
  text-decoration: line-through;
  color: #999;
}
</style>
```

## 总结

Vue 3 通过 Composition API、性能优化和新特性的加入，为开发者提供了更好的开发体验和更强大的功能。掌握这些核心概念和使用方法，将帮助你更好地使用 Vue 3 进行开发。

## 参考资料

- [Vue 3 官方文档](https://v3.vuejs.org/)
- [Vue 3 Composition API 文档](https://v3.vuejs.org/guide/composition-api-introduction.html)
