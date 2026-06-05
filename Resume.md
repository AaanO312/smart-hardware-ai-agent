# 邵杰铧

**求职意向：AI Agent / AI 应用开发**  
178-7580-0652 | jiehuashao@qq.com | github.com/AaanO312  
肇庆学院 · 物联网工程（本科）2023.09 - 2027.06 | 每周 5 天，可长期

## 技术能力

- **AI Agent**：LangChain Agent + Tool Calling、LangGraph（StateGraph / 条件路由 / interrupt / MemorySaver）、RAG 全链路、Prompt 分层与动态切换、中间件开发
- **工程**：Python、Streamlit、YAML 配置管理、日志系统、异常处理与全链路排查；AI 辅助开发（Vibe Coding）

## 项目经历

### 智扫通 — 智能硬件售后 AI Agent 问答系统 | 2026.04 - 至今
LangChain · Chroma · Streamlit · 通义千问 | [github.com/AaanO312/agent](https://github.com/AaanO312/agent)

- 独立完成从架构设计到上线的全流程，面向扫地机器人售后场景，覆盖故障排查、维护保养、使用建议等 10+ 类问题
- 自建 Chroma 本地向量库，导入 3 个专业知识库文件，实现文档自动解析、分块、向量化和语义检索
- 基于 LangChain 开发 ReAct Agent，注册 7 个工具（知识库检索、天气、用户定位、外部数据查询等），Agent 自主决策工具调用顺序
- 开发 3 层中间件管道：工具调用监控、模型调用日志、基于上下文的动态 Prompt 切换（问答/报告双模式自动路由）
- 设计 YAML 分层配置 + 日志双输出（控制台 & 按天归档），支持模型/参数/Prompt 热切换，无需改代码
- 使用 Streamlit 构建对话界面，支持流式输出，完整闭环可用

### 简历分析 Agent（LangGraph + Vibe Coding） | 2026.06
LangGraph · Streamlit · 通义千问 · PyPDF | [github.com/AaanO312/resume_agent](https://github.com/AaanO312/resume_agent)

- 全程 AI 辅助开发（Vibe Coding），我主导状态图架构设计与节点逻辑校验，AI 生成代码，快速交付可运行产品
- 基于 LangGraph 构建 6 节点 Agent 工作流：简历解析 → JD 匹配打分 → LLM 自主路由决策 →（深度分析 / 人工补充）→ 优化建议 + 改后简历生成
- 核心亮点：路由不由代码硬编码，由 LLM 自主判断匹配度后选择最优路径（直接生成 / 深入拆解 JD / 请求用户补充），体现 Agent 自主决策能力
- 使用 StateGraph + 条件路由 + interrupt + MemorySaver 实现有状态多步骤推理与人工介入
