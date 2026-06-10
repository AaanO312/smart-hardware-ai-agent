# 邵杰铧

**求职意向：AI Agent / AI 应用开发**  
178-7580-0652 | jiehuashao@qq.com | github.com/AaanO312  
持续关注大模型领域动态，有实际对比主流模型能力的经验，对 AI Agent 方向有强烈兴趣  
肇庆学院 · 物联网工程（本科）2023.09 - 2027.06 | 每周 5 天，可长期

---

## 技术能力

- **AI Agent**：LangChain Agent + Tool Calling、LangGraph（状态图编排 / 条件路由 / 人工介入）、RAG 全链路、Prompt 分层与动态切换、中间件开发
- **LLM & 模型**：通义千问（DashScope）、deepseek-v4 pro；熟悉 API 调用、参数调优与流式输出
- **向量库 & 检索**：Chroma、DashScope Embedding、PDF/TXT 文档解析（PyPDF）、文本切分与 Top-K 语义检索
- **工程 & 工具**：Python、Streamlit、Git；具备异常处理与全链路排查能力

---

## 项目经历

### 智能硬件售后 AI Agent 问答系统 | 2026.04 - 2026.05
LangChain · Chroma · Streamlit · 通义千问 | [github.com/AaanO312/smart-hardware-ai-agent](https://github.com/AaanO312/smart-hardware-ai-agent)

- 独立完成从架构设计到上线的全流程，面向扫地机器人售后场景，覆盖故障排查、维护保养、使用建议等 10+ 类问题
- 基于 RAG 架构搭建 Chroma 本地向量库，完成 PDF/TXT 文档解析、文本切分、DashScope Embedding 向量化、Top-K 相似度检索全链路，导入 3 个扫地机器人专业知识库文件
- 基于 LangChain 开发 ReAct Agent，注册 7 个工具（知识库检索、天气、用户定位、外部数据查询等），Agent 自主决策工具调用顺序
- 开发 Agent 中间件管道：工具调用全程监控、基于上下文的动态 Prompt 切换——Agent 在工具调用过程中自动识别报告生成意图并切换系统提示词，无需用户手动切换模式
- 使用 Streamlit 构建对话界面，支持流式输出，完整闭环可用

### 简历分析 Agent（LangGraph + Claude code） | 2026.06
LangGraph · Streamlit · 通义千问 · PyPDF | [github.com/AaanO312/resume_agent](https://github.com/AaanO312/resume_agent)

- 全程 AI 辅助开发（claude code），我主导状态图架构设计与节点逻辑校验，AI 生成代码，快速交付可运行产品
- 基于 LangGraph 构建 6 节点 Agent 工作流：简历解析 → JD 匹配打分 → LLM 自主路由决策 →（深度分析 / 人工补充）→ 优化建议 + 改后简历生成
- 核心亮点：路由不由代码硬编码，由 LLM 自主判断匹配度后选择最优路径（直接生成 / 深入拆解 JD / 请求用户补充），体现 Agent 自主决策能力
- 使用 StateGraph + 条件路由 + interrupt + MemorySaver 实现有状态多步骤推理与人工介入
