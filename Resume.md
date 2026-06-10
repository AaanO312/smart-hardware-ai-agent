# 邵杰铧

**求职意向：AI Agent / AI 应用开发**  
178-7580-0652 | jiehuashao@qq.com | github.com/AaanO312  
肇庆学院 · 物联网工程（本科）2023.09 - 2027.06

---

## 技术能力

- **AI Agent**：LangChain Agent + Tool Calling、LangGraph（状态图编排 / Multi-Agent 协作 / 并行 Fan-out / 条件路由）、RAG 全链路、Prompt 分层与动态切换、中间件开发
- **LLM & 模型**：通义千问（DashScope / Ollama 本地部署）、DeepSeek-V4、Gemma 4；API 调用、流式输出、参数调优
- **向量库 & 检索**：Chroma、DashScope Embedding、PDF/TXT 文档解析（PyPDF）、文本切分、Top-K 语义检索
- **工程 & 工具**：Python、Streamlit、FastAPI、Git；Claude Code / Codex AI 辅助开发

---

## 项目经历

### 智能硬件售后 AI Agent 问答系统 | 2026.04 - 2026.05
LangChain · Chroma · Streamlit · 通义千问 | [GitHub](https://github.com/AaanO312/smart-hardware-ai-agent) | [在线Demo](https://jlasm5aioqgvmrh3dvqhwn.streamlit.app/)

- 基于 RAG 搭建 Chroma 向量库：PDF/TXT 解析 → 文本切分 → DashScope Embedding 向量化 → Top-K 检索，导入 3 个扫地机器人知识库
- LangChain ReAct Agent 注册 7 个工具（知识库检索、天气、用户定位、外部数据查询等），Agent 自主决策调用顺序
- 3 层中间件：工具调用监控 + 上下文驱动的动态 Prompt 切换（Agent 在工具调用中识别报告生成意图，自动切换系统提示词）
- FastAPI 封装 REST 接口，Streamlit 对话界面 + 流式输出，Streamlit Cloud 线上可访问

### 旅行规划 Multi-Agent 系统 | 2026.06
LangGraph · Streamlit · 通义千问 · Open-Meteo API | [GitHub](https://github.com/AaanO312/travel_agent) | [在线Demo](https://travelagent-2qjnxbankltdylfl6axvwv.streamlit.app/)

- 4 Agent 协作：天气查询（Open-Meteo 免费实时 API）→ 行程规划 ∥ 预算估算（LangGraph 并行 Fan-out）→ 协调 Agent 审核（6 项标准：天气冲突/预算超支/行程密度/时间逻辑/偏好匹配/完整度）
- 协调 Agent 审核不通过时自动驳回、生成修订指令、行程/预算 Agent 按指令重做，最多 3 轮循环直到方案自洽
- 表单收集需求 → 生成方案 → 对话式微调，用户反馈直接注入修订循环
- FastAPI 封装 REST 接口，Streamlit Cloud 线上可访问
