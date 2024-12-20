---
layout: post
title: "Jackson：Java 世界最强大的 JSON 处理库"
date: 2024-01-28
categories: 技术
tags: [Java, JSON, 序列化, 开源库]
toc: true
---

## Jackson 简介

### 什么是 Jackson？

Jackson 是 Java 生态系统中最流行、最强大的 JSON 处理库。它提供了高性能的 JSON 解析、生成和数据绑定功能，被广泛应用于 Web 服务、微服务和企业级应用中。

### 为什么选择 Jackson？

1. **卓越性能**
   - 高速序列化/反序列化
   - 低内存占用
   - 处理大规模 JSON

2. **灵活性**
   - 多种数据绑定模式
   - 丰富的定制选项
   - 支持复杂对象结构

## 基本使用

### 1. Maven 依赖

```xml
<dependency>
    <groupId>com.fasterxml.jackson.core</groupId>
    <artifactId>jackson-databind</artifactId>
    <version>2.15.2</version>
</dependency>
```

### 2. 对象序列化

```java
import com.fasterxml.jackson.databind.ObjectMapper;

public class User {
    private String name;
    private int age;
    // 构造函数、Getter/Setter
}

public class JacksonExample {
    public static void main(String[] args) throws Exception {
        ObjectMapper mapper = new ObjectMapper();
        
        // 对象转 JSON
        User user = new User("张三", 30);
        String json = mapper.writeValueAsString(user);
        System.out.println(json);
        // 输出: {"name":"张三","age":30}
    }
}
```

### 3. JSON 反序列化

```java
public class DeserializationExample {
    public static void main(String[] args) throws Exception {
        ObjectMapper mapper = new ObjectMapper();
        
        // JSON 转对象
        String json = "{\"name\":\"李四\",\"age\":25}";
        User user = mapper.readValue(json, User.class);
        System.out.println(user.getName()); // 输出: 李四
    }
}
```

## 高级特性

### 1. 注解使用

```java
import com.fasterxml.jackson.annotation.*;

public class AdvancedUser {
    @JsonProperty("username")  // 自定义 JSON 字段名
    private String name;

    @JsonIgnore  // 忽略字段
    private String password;

    @JsonFormat(pattern = "yyyy-MM-dd")  // 日期格式化
    private Date birthDate;

    @JsonInclude(JsonInclude.Include.NON_NULL)  // 忽略空值
    private String email;
}
```

### 2. 复杂对象处理

```java
public class ComplexObjectExample {
    public static void main(String[] args) throws Exception {
        ObjectMapper mapper = new ObjectMapper();
        
        // 处理泛型集合
        List<User> users = Arrays.asList(
            new User("张三", 30),
            new User("李四", 25)
        );
        
        // 复杂对象序列化
        String json = mapper.writerWithDefaultPrettyPrinter()
                            .writeValueAsString(users);
        
        // 反序列化复杂对象
        List<User> parsedUsers = mapper.readValue(
            json, 
            mapper.getTypeFactory().constructCollectionType(List.class, User.class)
        );
    }
}
```

### 3. 定制序列化

```java
public class CustomSerializerExample {
    public static class CustomUserSerializer extends JsonSerializer<User> {
        @Override
        public void serialize(User user, JsonGenerator gen, SerializerProvider provider) 
            throws IOException {
            gen.writeStartObject();
            gen.writeStringField("fullName", user.getName());
            gen.writeNumberField("userAge", user.getAge());
            gen.writeEndObject();
        }
    }

    @JsonSerialize(using = CustomUserSerializer.class)
    public class User {
        // 原有属性
    }
}
```

## 性能优化

### 1. ObjectMapper 重用

```java
public class PerformanceOptimization {
    // 推荐：全局单例 ObjectMapper
    private static final ObjectMapper MAPPER = new ObjectMapper();

    public void processJson() throws Exception {
        // 重用 ObjectMapper 实例
        String json = MAPPER.writeValueAsString(data);
    }
}
```

### 2. 配置优化

```java
ObjectMapper mapper = new ObjectMapper()
    .configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false)
    .setSerializationInclusion(JsonInclude.Include.NON_NULL)
    .enable(SerializationFeature.INDENT_OUTPUT);
```

## 常见应用场景

### 1. RESTful API

```java
@RestController
public class UserController {
    @PostMapping("/users")
    public ResponseEntity<User> createUser(@RequestBody User user) {
        // 自动反序列化请求体
        userService.save(user);
        return ResponseEntity.ok(user);
    }
}
```

### 2. 配置管理

```java
public class ConfigurationLoader {
    public AppConfig loadConfig(String configPath) throws IOException {
        ObjectMapper mapper = new ObjectMapper(new YAMLFactory());
        return mapper.readValue(new File(configPath), AppConfig.class);
    }
}
```

## 替代方案对比

| 特性 | Jackson | Gson | Fastjson | Moshi |
|------|---------|------|----------|-------|
| 性能 | 极高 | 高 | 很高 | 中等 |
| 灵活性 | 非常好 | 好 | 一般 | 好 |
| 注解支持 | 非常丰富 | 有限 | 一般 | 有限 |
| 社区支持 | 非常活跃 | 活跃 | 中等 | 较小 |

## 最佳实践

1. **全局单例 ObjectMapper**
2. **合理配置序列化选项**
3. **使用注解简化配置**
4. **处理异常情况**
5. **关注性能**

## 常见问题

### 1. 未知属性处理

```java
// 忽略未知属性
mapper.configure(DeserializationFeature.FAIL_ON_UNKNOWN_PROPERTIES, false)
```

### 2. 日期处理

```java
// 配置日期格式
mapper.registerModule(new JavaTimeModule());
mapper.configure(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS, false);
```

## 总结

Jackson 是 Java JSON 处理的瑞士军刀，通过其卓越的性能、丰富的特性和灵活的配置，为开发者提供了极致的 JSON 处理体验。

关键优势：
- 高性能
- 灵活配置
- 丰富注解
- 广泛应用

## 扩展阅读

- Jackson 官方文档
- JSON 处理最佳实践
- Java 序列化技术
