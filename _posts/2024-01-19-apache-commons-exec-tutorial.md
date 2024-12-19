---
layout: post
title: "Apache Commons Exec：Java 系统命令执行终极指南"
date: 2024-01-19
categories: 技术
tags: [Java, Apache Commons, 系统编程, 命令执行]
toc: true
---

## Commons Exec 简介

### 什么是 Commons Exec？

Apache Commons Exec 是一个专门用于在 Java 中执行外部系统命令的类库。相比 `Runtime.getRuntime().exec()`，它提供了更加强大、安全和灵活的系统命令执行机制。

### 为什么选择 Commons Exec？

1. **更好的命令执行控制**
2. **丰富的异常处理**
3. **跨平台兼容性**
4. **资源管理**
5. **超时控制**

## 快速开始

### Maven 依赖

```xml
<dependency>
    <groupId>org.apache.commons</groupId>
    <artifactId>commons-exec</artifactId>
    <version>1.3</version>
</dependency>
```

## 基本用法

### 1. 简单命令执行

```java
import org.apache.commons.exec.CommandLine;
import org.apache.commons.exec.DefaultExecutor;

public class SimpleExecExample {
    public static void main(String[] args) throws Exception {
        // 创建命令行
        CommandLine cmdLine = new CommandLine("ls");
        cmdLine.addArgument("-l");

        // 创建执行器
        DefaultExecutor executor = new DefaultExecutor();
        
        // 执行命令
        int exitValue = executor.execute(cmdLine);
        System.out.println("Exit Value: " + exitValue);
    }
}
```

### 2. 跨平台命令执行

```java
public class CrossPlatformExample {
    public static void main(String[] args) throws Exception {
        // Windows 和 Unix 通用
        CommandLine cmdLine = new CommandLine("ping");
        cmdLine.addArgument("localhost");

        DefaultExecutor executor = new DefaultExecutor();
        executor.execute(cmdLine);
    }
}
```

## 高级特性

### 1. 命令参数处理

```java
// 动态参数替换
CommandLine cmdLine = new CommandLine("git");
cmdLine.addArgument("clone");
cmdLine.addArgument("${url}");
cmdLine.setSubstitutionMap(Collections.singletonMap("url", "https://github.com/example/repo.git"));
```

### 2. 超时控制

```java
import org.apache.commons.exec.ExecuteWatchdog;

public class TimeoutExample {
    public static void main(String[] args) throws Exception {
        CommandLine cmdLine = new CommandLine("sleep");
        cmdLine.addArgument("10");

        DefaultExecutor executor = new DefaultExecutor();
        
        // 5秒超时
        ExecuteWatchdog watchdog = new ExecuteWatchdog(5000);
        executor.setWatchdog(watchdog);

        try {
            executor.execute(cmdLine);
        } catch (ExecuteException e) {
            if (watchdog.killedProcess()) {
                System.out.println("命令执行超时");
            }
        }
    }
}
```

### 3. 输出流处理

```java
import org.apache.commons.exec.PumpStreamHandler;
import java.io.ByteArrayOutputStream;

public class StreamHandlingExample {
    public static void main(String[] args) throws Exception {
        CommandLine cmdLine = new CommandLine("echo");
        cmdLine.addArgument("Hello, World!");

        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        PumpStreamHandler streamHandler = new PumpStreamHandler(outputStream);

        DefaultExecutor executor = new DefaultExecutor();
        executor.setStreamHandler(streamHandler);
        executor.execute(cmdLine);

        System.out.println("命令输出：" + outputStream.toString());
    }
}
```

### 4. 环境变量设置

```java
public class EnvironmentExample {
    public static void main(String[] args) throws Exception {
        CommandLine cmdLine = new CommandLine("printenv");

        Map<String, String> env = new HashMap<>(System.getenv());
        env.put("CUSTOM_VAR", "Hello Exec");

        DefaultExecutor executor = new DefaultExecutor();
        executor.execute(cmdLine, env);
    }
}
```

## 异常处理

### 常见异常类型

1. `ExecuteException`：命令执行失败
2. `IOException`：系统 I/O 错误
3. `ExecuteWatchdog.TimeoutException`：命令执行超时

```java
try {
    executor.execute(cmdLine);
} catch (ExecuteException e) {
    System.err.println("命令执行失败，退出码：" + e.getExitValue());
} catch (IOException e) {
    System.err.println("系统错误：" + e.getMessage());
}
```

## 安全性最佳实践

1. **避免直接拼接用户输入**
2. **使用参数占位符**
3. **限制命令执行权限**
4. **设置合理的超时**

## 性能优化

1. 重用 `DefaultExecutor`
2. 合理控制超时时间
3. 使用 `PumpStreamHandler` 高效处理流
4. 避免频繁创建执行器实例

## 替代方案

1. `Runtime.getRuntime().exec()`
2. `ProcessBuilder`
3. Java 9+ `ProcessHandle`

## 常见坑点

1. **僵尸进程**：使用 `ExecuteWatchdog` 控制
2. **编码问题**：注意字符集
3. **平台兼容性**：编写跨平台代码

## 总结

Apache Commons Exec 提供了一个强大、灵活的系统命令执行解决方案。通过合理使用其特性，可以安全、高效地在 Java 中执行外部命令。

关键记忆点：
- 使用 `CommandLine` 构建命令
- 利用 `DefaultExecutor` 执行
- 通过 `ExecuteWatchdog` 控制超时
- 使用 `PumpStreamHandler` 处理输出

## 扩展阅读

- Apache Commons Exec 官方文档
- Java 进程管理最佳实践
- 系统编程安全指南
