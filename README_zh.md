[English](./README.md) | **中文**

# HitCC

> Claude Code CLI Node.js版本 v2.1.84 逆向重建知识库

HitCC 不是源码仓库，而是一套面向学习、分析与重写的文档库。  
项目目标不是复刻原始文件树，而是尽可能还原 Claude Code CLI 的核心运行逻辑、模块边界、配置系统和外围生态，从而为“可运行替代品”或“高相似版本重写”提供稳定参考。

本项目与 Anthropic PBC 无任何关系。仓库中不包含 Claude Code 原始源码，不包含破解内容，也不包含绕过产品策略或权限机制的实现。

## 说明

获取本仓库研究的 Claude Code CLI：
```sh
npm pack @anthropic-ai/claude-code@2.1.84
```

`recovery_tools/`下面的Pthton脚本可以对混淆加密后的源代码初步优化

本仓库仅基于上述方法获得的 Claude Code CLI v2.1.84 的静态分析，未进行运行时动态分析，也没有使用 Anthropic PBC 提供的任何包括 LLM 推理服务在内的网络服务。

本仓库文档内容可能偏多，目前统计的 `docs/`（下列数据可能不会及时更新）：
```
TOTAL
  Files: 81
  Lines: 27170
  Chars: 698707
  Bytes: 953399
```

## 这个仓库提供什么

- Claude Code CLI 主执行链的结构化逆向文档
- 从启动入口到 Agent Loop、Tool Use、Prompt 组装、Session 持久化的分主题分析
- MCP、Plugin、Skill、TUI、Remote Persistence、Bridge 等外围系统的拆分说明
- 面向重写工程的候选架构、已知边界和未决项整理

## 这个仓库不提供什么

- 原始源码文件结构还原
- 私有服务端实现细节
- 1:1 行为复刻保证
- 可直接运行的 CLI、SDK 或安装脚本

## 文档覆盖范围

当前知识库不是按原始源码文件树组织，而是按“可稳定还原的运行时主题”组织。  
截至目前，`docs/` 已覆盖的范围可以按目录理解为：

- `00-overview`
  - 范围边界、证据来源、置信度口径、文档结构与维护约定
- `01-runtime`
  - CLI 入口、命令树、运行模式分流
  - Session / Transcript 持久化与恢复
  - 输入编译链、主 Agent Loop、compact 分支
  - Model adapter、provider 选择、auth、stream 处理与 remote transport
  - `web-search`、`web-fetch` 两类内建网络工具
  - telemetry、control plane、非 LLM 网络链路
  - settings source、路径、合并、缓存、写回与关键消费面
- `02-execution`
  - Tool execution core、并发执行、Hook runtime、Permission / Sandbox / Approval
  - instruction discovery、rules、prompt assembly、context layering
  - 非主线程 prompt 路径、attachment 生命周期、context modifier 与 tool-use context
- `03-ecosystem`
  - Resume、Fork、Sidechain、Subagent、agent team
  - Remote persistence、bridge、Plan system
  - MCP、Skill、Plugin、TUI 及其运行时交互边界
- `04-rewrite`
  - 面向重写工程的候选分层、目录骨架、未决项与阻塞判断
- `05-appendix`
  - glossary、evidence map 等统一术语和证据索引

## 当前结论

基于当前证据边界，这套文档已经足以支持：

- 可运行替代品的重建
- 高相似版本的模块化重写

但仍不足以承诺：

- 原版工程目录的准确还原
- 私有服务端黑箱逻辑的完整还原
- 原版所有边角行为的 1:1 复现

更具体的判断见：

- [范围、证据与结论](./docs/00-overview/01-scope-and-evidence.md)
- [重写判断、阻塞级未决项与后续补证](./docs/04-rewrite/02-open-questions-and-judgment.md)


## 建议阅读顺序

1. 先读 [docs/00-overview/01-scope-and-evidence.md](./docs/00-overview/01-scope-and-evidence.md)，确认这套文档已经知道什么、还不知道什么。
2. 再读 [docs/01-runtime/01-product-cli-and-modes.md](./docs/01-runtime/01-product-cli-and-modes.md) 到 `01-runtime` 相关页面，建立产品形态与主运行链认识。
3. 继续阅读 `02-execution`，把 prompt、tool use、hook、permission、attachment 等执行路径串起来。
4. 再进入 `03-ecosystem`，补齐 MCP、Plugin、Skill、TUI、Remote、Plan 等外围系统。
5. 最后阅读 `04-rewrite`，把当前知识边界和工程落地策略连接起来。

如果你只想快速进入主题，请直接从 [docs/00-overview/00-index.md](./docs/00-overview/00-index.md) 开始。

## 维护原则

本仓库当前采用“知识库”而不是“长篇单文档”维护方式，核心原则如下：

- `00-overview/00-index.md` 只做全局入口，不重复正文
- 父页只做导航与边界说明，不承载长篇机制分析
- 子页负责正文、证据落点、反证与未决项
- 未知点统一收口到范围页与重写判断页，避免在多个目录页重复维护
- 新增证据时，优先更新对应主题页，再回补 glossary 或 evidence map

详细约定见：

- [docs/00-overview/02-document-style-and-structure-conventions.md](./docs/00-overview/02-document-style-and-structure-conventions.md)

## 适用场景

这个仓库更适合以下用途：

- 研究 Claude Code CLI 的系统结构与职责边界
- 为自研 agentic coding shell 提供架构参考
- 为高相似版本重写整理稳定知识边界
- 交叉校验某个功能点在运行时主链中的位置

不适合以下用途：

- 寻找原始源码
- 期待直接运行的替代实现
- 追求服务端私有逻辑的完整还原

## 授权声明

Copyright (c) 2026 Hitmux contributors

本项目采用 [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) 许可协议。

这意味着你可以：

- 复制与传播本项目内容
- 修改、改编并再发布
- 在商业或非商业场景中使用

但你必须：

- 保留原作者或来源署名
- 附上许可证链接
- 说明是否做过修改

正式许可证文本见仓库根目录的 [LICENSE](./LICENSE)。

## 致谢
感谢[Linux Do](https://linux.do)社区的支持

## 免责条款

请仅将本项目用于学习、研究、教学或正当工程分析用途。  
任何将本项目用于侵犯 Anthropic PBC 合法权益或规避产品政策的行为，均与本项目无关，风险自负。

作者不对文档内容的准确性、完整性或因使用该文档导致的任何直接或间接损失（包括但不限于法律风险、技术故障、数据丢失）承担法律责任。
