# Docker Images Pusher

使用 Github Action 将国外的 Docker 镜像转存到阿里云私有仓库，供国内服务器使用，免费易用。

- 每天 00:00(UTC) 触发任务；
- 支持同步单个镜像的多个版本；
- 支持自动同步前天有更新的镜像。

## 使用方式

### 配置环境变量

进入 Settings->Secret and variables->Actions->New Repository secret，配置以下环境变量：

`ALIYUN_REGISTRY`：阿里云仓库地址

`ALIYUN_NAME_SPACE`：阿里云仓库命名空间

`ALIYUN_REGISTRY_USER`：阿里云仓库用户名

`ALIYUN_REGISTRY_PASSWORD`：阿里云仓库密码

### 添加镜像

在 [images.txt](images.txt) 中添加镜像地址，一行一个镜像。

- 支持别名，格式为`镜像 --alias 名称`：
  ```txt
  vaultwarden/server --alias vaultwarden
  ```
