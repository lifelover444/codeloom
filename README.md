# Codeloom 织言

Codeloom 织言是一个运行在终端里的本地 AI 编程助手。

它面向日常代码开发场景，提供项目理解、代码修改、提交辅助、测试命令调用和文件级上下文管理能力。

## 快速开始

在项目根目录安装本地开发版本：

```bash
python -m pip install -e .
```

确认命令可用：

```bash
codeloom --version
codeloom --help
```

启动交互式编程环境：

```bash
codeloom
```

如果已经配置了用户级环境变量和配置文件，可以在任意目录直接运行 `codeloom`。

## 配置步骤

Codeloom 织言可以连接不同厂商的大模型。使用前需要先准备对应模型服务商的 API key，并把密钥写入本机环境变量。

1. 选择模型服务商和模型

   例如：

   ```bash
   codeloom --model deepseek/deepseek-v4-pro
   ```
   
2. 配置对应的 API key

   Windows PowerShell 示例：

   ```powershell
   setx DEEPSEEK_API_KEY "你的 DeepSeek 密钥"
   setx OPENAI_API_KEY "你的 OpenAI 密钥"
   setx ANTHROPIC_API_KEY "你的 Anthropic 密钥"
   ```

   只需要配置你实际使用的服务商。执行 `setx` 后，请重新打开终端让环境变量生效。

3. 写入可选的用户级默认配置

   如果希望每次直接输入 `codeloom` 就使用固定模型，可以在用户目录创建 `~/.codeloom.conf.yml`：

   ```yaml
   model: deepseek/deepseek-v4-pro
   analytics-disable: true
   check-update: false
   ```

   这里的 DeepSeek 只是示例。你可以把 `model` 改成自己要使用的模型。

4. 检查配置是否生效

   ```bash
   codeloom --exit --no-git --no-show-release-notes --no-show-model-warnings
   ```

   输出中会显示当前使用的模型。

## 常用命令

查看版本：

```bash
codeloom --version
```

在不进入交互模式的情况下检查启动：

```bash
codeloom --exit --no-git --no-show-release-notes --no-show-model-warnings
```

指定模型运行：

```bash
codeloom --model deepseek/deepseek-v4-pro
```

查看可用参数：

```bash
codeloom --help
```

## 项目结构

```text
codeloom/
├── codeloom/      # 核心源码包
├── tests/         # 测试用例
├── scripts/       # 工具脚本
├── docker/        # 容器相关文件
├── docs/          # 项目维护文档
└── README.md      # 中文使用说明
```

## 验收检查

修改命令、配置、文案或打包逻辑后，建议运行：

```bash
python scripts/check_codeloom_acceptance.py
```

该脚本会检查命令入口、包结构、运行产物命名、帮助文本和用户可见文案。

也可以运行当前聚焦的基础测试：

```bash
python -m pytest tests/basic/test_acceptance_script.py tests/basic/test_user_visible_branding.py tests/basic/test_cli_metadata.py tests/basic/test_project_structure.py tests/basic/test_branding.py tests/basic/test_runtime_paths.py -q
```

## 说明

Codeloom 织言的目标是提供一个独立、清晰、可演示的终端 AI 编程产品体验。普通用户路径中不应出现旧命令名、旧配置名或旧运行产物名。
