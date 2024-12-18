---
layout: post
title: "Docker 实战指南：从入门到进阶"
date: 2024-01-05
categories: 技术
tags: [Docker, 容器化, DevOps, 教程]
toc: true
---

Docker 是一个开源的应用容器引擎，让开发者可以打包他们的应用以及依赖包到一个可移植的容器中，然后发布到任何流行的 Linux 或 Windows 机器上。本文将全面介绍 Docker 的核心概念和使用方法。

## Docker 基础概念

### 核心组件

Docker 包含三个核心组件：

1. **Docker 引擎**：负责创建和管理 Docker 容器
2. **Docker 镜像**：容器的模板，包含了应用及其依赖
3. **Docker 容器**：镜像的运行实例

### 工作原理

Docker 使用客户端-服务器架构：

- **Docker daemon**：服务器组件，管理容器
- **Docker CLI**：命令行客户端，与 daemon 交互
- **Docker registry**：存储和分发 Docker 镜像

## 安装 Docker

### Windows 安装

1. 下载 [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop)
2. 运行安装程序
3. 启用 WSL 2（Windows Subsystem for Linux）
4. 启动 Docker Desktop

### Linux 安装

Ubuntu/Debian:
```bash
# 更新包索引
sudo apt-get update

# 安装依赖
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# 添加 Docker 官方 GPG 密钥
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# 设置稳定版仓库
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 安装 Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```

## Docker 基本命令

### 镜像管理

```bash
# 搜索镜像
docker search nginx

# 拉取镜像
docker pull nginx:latest

# 列出本地镜像
docker images

# 删除镜像
docker rmi nginx:latest
```

### 容器操作

```bash
# 运行容器
docker run -d -p 80:80 --name my-nginx nginx

# 列出运行中的容器
docker ps

# 列出所有容器（包括停止的）
docker ps -a

# 停止容器
docker stop my-nginx

# 启动容器
docker start my-nginx

# 删除容器
docker rm my-nginx
```

## Dockerfile 详解

Dockerfile 是用于构建 Docker 镜像的文本文件。

### 基本结构

```dockerfile
# 基础镜像
FROM node:14

# 设置工作目录
WORKDIR /app

# 复制依赖文件
COPY package*.json ./

# 安装依赖
RUN npm install

# 复制源代码
COPY . .

# 暴露端口
EXPOSE 3000

# 启动命令
CMD ["npm", "start"]
```

### 常用指令

- **FROM**：指定基础镜像
- **WORKDIR**：设置工作目录
- **COPY/ADD**：复制文件
- **RUN**：执行命令
- **ENV**：设置环境变量
- **EXPOSE**：声明端口
- **CMD/ENTRYPOINT**：指定启动命令

## Docker Compose

Docker Compose 用于定义和运行多容器 Docker 应用程序。

### 安装

```bash
# Linux
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### docker-compose.yml 示例

```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - db
  db:
    image: mongo:latest
    volumes:
      - mongodb_data:/data/db

volumes:
  mongodb_data:
```

### 基本命令

```bash
# 启动服务
docker-compose up -d

# 停止服务
docker-compose down

# 查看日志
docker-compose logs

# 查看服务状态
docker-compose ps
```

## Docker 网络

### 网络类型

1. **bridge**：默认网络，容器间可通过 IP 通信
2. **host**：容器使用主机网络
3. **none**：容器没有网络连接
4. **overlay**：跨主机容器网络

### 网络命令

```bash
# 创建网络
docker network create my-network

# 列出网络
docker network ls

# 连接容器到网络
docker network connect my-network container-name

# 断开网络连接
docker network disconnect my-network container-name
```

## 数据管理

### 数据卷（Volumes）

```bash
# 创建数据卷
docker volume create my-volume

# 使用数据卷运行容器
docker run -v my-volume:/data nginx
```

### 绑定挂载（Bind Mounts）

```bash
# 将主机目录挂载到容器
docker run -v /host/path:/container/path nginx
```

## 最佳实践

### 镜像构建

1. **使用多阶段构建**
```dockerfile
# 构建阶段
FROM node:14 AS builder
WORKDIR /app
COPY . .
RUN npm install && npm run build

# 运行阶段
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
```

2. **优化镜像大小**
- 使用适当的基础镜像
- 合并 RUN 指令
- 清理不必要的文件

### 容器安全

1. **以非 root 用户运行**
```dockerfile
USER node
```

2. **限制资源使用**
```bash
docker run --memory="512m" --cpus="1.5" nginx
```

## 实战示例

### 部署 Web 应用

1. **创建 Dockerfile**
```dockerfile
FROM node:14-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000
CMD ["npm", "start"]
```

2. **创建 docker-compose.yml**
```yaml
version: '3'
services:
  web:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
    restart: always
```

3. **部署命令**
```bash
# 构建并启动
docker-compose up -d --build

# 查看日志
docker-compose logs -f
```

## 故障排查

### 常见命令

```bash
# 查看容器日志
docker logs container-name

# 进入容器
docker exec -it container-name sh

# 查看容器详细信息
docker inspect container-name

# 查看容器资源使用
docker stats
```

### 常见问题

1. **容器无法启动**
- 检查日志
- 验证端口映射
- 确认资源限制

2. **网络连接问题**
- 检查网络配置
- 验证防火墙规则
- 确认 DNS 设置

## 总结

Docker 通过容器化技术简化了应用的部署和管理流程。掌握 Docker 的核心概念和使用方法，可以显著提高开发和运维效率。

## 参考资料

- [Docker 官方文档](https://docs.docker.com/)
- [Docker Hub](https://hub.docker.com/)
- [Docker Compose 文档](https://docs.docker.com/compose/)
