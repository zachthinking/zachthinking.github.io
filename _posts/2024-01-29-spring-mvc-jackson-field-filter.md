---
layout: post
title: "Spring MVC + Jackson：过滤 JSON 响应字段"
date: 2024-01-29
categories: 技术
tags: [Spring MVC, Jackson, JSON, 后端开发]
toc: true
---

## 为什么需要字段过滤？

### 场景分析

在实际开发中，我们经常遇到这些情况：

1. **敏感信息保护**
   - 不想返回用户密码
   - 隐藏内部ID
   - 保护隐私数据

2. **接口灵活性**
   - 不同场景返回不同字段
   - 减少网络传输负载
   - 简化前端数据处理

## Jackson 字段过滤方案

### 1. 注解方式

#### @JsonIgnore

```java
public class User {
    private Long id;
    private String username;
    
    @JsonIgnore  // 完全忽略字段
    private String password;
}
```

#### @JsonIgnoreProperties

```java
// 类级别忽略多个字段
@JsonIgnoreProperties({"password", "internalId", "createdAt"})
public class User {
    private Long id;
    private String username;
    
    @JsonIgnore  // 单个字段忽略
    private String password;
    
    // 动态忽略
    @JsonIgnoreProperties(value = {"hibernateLazyInitializer", "handler"}, allowSetters = true)
    private UserDetails details;
}
```

@JsonIgnoreProperties 注解提供了更灵活的字段过滤方式：
- 可以在类级别批量忽略字段
- 支持动态忽略
- allowSetters 参数允许在反序列化时设置被忽略的字段

#### @JsonView

```java
public class Views {
    // 定义视图标记
    public interface Public {}
    public interface Internal extends Public {}
}

public class User {
    @JsonView(Views.Public.class)
    private Long id;
    
    @JsonView(Views.Public.class)
    private String username;
    
    @JsonView(Views.Internal.class)
    private String email;
}

@RestController
public class UserController {
    @GetMapping("/users")
    @JsonView(Views.Public.class)
    public List<User> getUsers() {
        // 只返回 Public 视图字段
    }
}
```

### 2. 动态过滤

#### 自定义 Mixin

```java
@Configuration
public class JacksonConfig {
    @Bean
    public ObjectMapper objectMapper() {
        ObjectMapper mapper = new ObjectMapper();
        mapper.addMixIn(User.class, UserMixin.class);
        return mapper;
    }
}

abstract class UserMixin {
    @JsonIgnore
    abstract String getPassword();
}
```

### 3. 属性过滤器

```java
public class DynamicFilter {
    public static PropertyFilter getFilter(String... fields) {
        return new SimpleBeanPropertyFilter() {
            @Override
            public void serializeAsField(
                Object pojo, 
                JsonGenerator jgen, 
                SerializerProvider provider, 
                PropertyWriter writer
            ) throws Exception {
                if (include(writer)) {
                    writer.serializeAsField(pojo, jgen, provider);
                }
            }
            
            private boolean include(PropertyWriter writer) {
                return Arrays.asList(fields).contains(writer.getName());
            }
        };
    }
}

@RestController
public class UserController {
    @GetMapping("/users")
    public MappingJacksonValue getUsers() {
        List<User> users = userService.findAll();
        
        MappingJacksonValue mapping = new MappingJacksonValue(users);
        SimpleBeanPropertyFilter filter = DynamicFilter.getFilter("id", "username");
        
        FilterProvider filters = new SimpleFilterProvider()
            .addFilter("userFilter", filter);
        
        mapping.setFilters(filters);
        return mapping;
    }
}
```

### 4. 序列化包含策略

```java
public class User {
    @JsonInclude(JsonInclude.Include.NON_NULL)
    private String email;  // 为 null 时不返回
    
    @JsonInclude(JsonInclude.Include.NON_EMPTY)
    private List<String> tags;  // 空集合不返回
}
```

## 高级过滤技巧

### 1. 条件过滤

```java
public class ConditionalFilter extends SimpleBeanPropertyFilter {
    @Override
    public void serializeAsField(
        Object pojo, 
        JsonGenerator jgen, 
        SerializerProvider provider, 
        PropertyWriter writer
    ) throws Exception {
        // 自定义复杂过滤逻辑
        if (shouldSerialize(pojo, writer)) {
            writer.serializeAsField(pojo, jgen, provider);
        }
    }
    
    private boolean shouldSerialize(Object pojo, PropertyWriter writer) {
        // 根据对象状态决定是否序列化
        if (pojo instanceof User) {
            User user = (User) pojo;
            return user.isActive();
        }
        return true;
    }
}
```

### 2. 嵌套对象过滤

```java
public class NestedFilter {
    public static MappingJacksonValue filterNested(Object object) {
        MappingJacksonValue mapping = new MappingJacksonValue(object);
        
        FilterProvider filters = new SimpleFilterProvider()
            .addFilter("userFilter", 
                SimpleBeanPropertyFilter.serializeAllExcept("password"))
            .addFilter("addressFilter", 
                SimpleBeanPropertyFilter.filterOutAllExcept("city", "country"));
        
        mapping.setFilters(filters);
        return mapping;
    }
}
```

## 性能与最佳实践

### 1. 性能优化

```java
// 使用单例 ObjectMapper
@Configuration
public class JacksonConfig {
    private static final ObjectMapper MAPPER = new ObjectMapper();
    
    static {
        MAPPER.configure(SerializationFeature.FAIL_ON_EMPTY_BEANS, false);
        MAPPER.setSerializationInclusion(JsonInclude.Include.NON_NULL);
    }
}
```

### 2. 安全考虑

```java
// 防止敏感信息泄露
@JsonIgnoreProperties({"hibernateLazyInitializer", "handler"})
public class BaseEntity { }
```

## 常见陷阱与解决

1. **循环引用**
   - 使用 `@JsonManagedReference`
   - `@JsonBackReference`

2. **延迟加载**
   - 配置 Jackson 支持 Hibernate
   - 使用 DTO 转换

## 替代方案对比

| 方案 | 灵活性 | 性能 | 复杂度 | 推荐场景 |
|------|--------|------|--------|----------|
| 注解 | 中 | 高 | 低 | 简单场景 |
| Mixin | 高 | 中 | 中 | 复杂过滤 |
| 动态过滤器 | 很高 | 低 | 高 | 动态需求 |

## 总结

Jackson 字段过滤是一种强大的技术，它为 JSON 序列化提供了极大的灵活性和精确控制。通过合理运用各种过滤技术，我们可以构建更加安全、高效的 API。

关键技术要点：
- 注解过滤
- 动态过滤
- 条件过滤
- 性能优化

## 扩展阅读

- Jackson 高级特性
- REST API 设计
- 数据传输最佳实践
