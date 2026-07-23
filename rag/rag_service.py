from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from rag.vector_store import VectorStoreService
from utils.prompt_loader import load_rag_prompts
from langchain_core.prompts import PromptTemplate
from model.factory import chat_model
from utils.logger_handler import logger

def print_prompt(prompt):
    print("="*20)
    print(prompt.to_string())
    print("="*20)
    return prompt

class RagSummarizeService(object):
    def __init__(self):
        self.vector_store = VectorStoreService()
        self.retriever = self.vector_store.get_retriever()
        self.prompt_text = load_rag_prompts()
        self.prompt_template = PromptTemplate.from_template(self.prompt_text)
        self.model = chat_model
        self.chain = self.__init__chain()

    def __init__chain(self):
        chain = self.prompt_template | print_prompt | self.model | StrOutputParser()
        return chain

    def retriever_docs(self,query: str) -> list[Document]:
        return self.retriever.invoke(query)

    def rag_summarize(self, query: str) -> str:
        context_docs = self.retriever_docs(query)
        context = ""
        counter = 0
        for doc in context_docs:
            counter += 1
            context += f"[参考资料{counter}]：参考资料：{doc.page_content} | 参考元数据：{doc.metadata}\n"
        
        try:
            return self.chain.invoke(
                {
                    "input": query,
                    "context": context,
                }
            )
        except KeyError as e:
            # DashScope 审核模块偶发拦截会导致响应结构缺少字段，降级返回检索原文
            logger.warning(f"[rag_summarize] LLM 调用 KeyError（可能是审核拦截）: {str(e)}，返回检索原文")
            if context_docs:
                fallback = "以下是根据知识库检索到的相关信息：\n\n"
                for i, doc in enumerate(context_docs, 1):
                    fallback += f"{i}. {doc.page_content}\n"
                return fallback
            return "知识库中暂无足够信息回答此问题，建议联系人工客服获取帮助。"
        except Exception as e:
            logger.error(f"[rag_summarize] LLM 调用失败: {str(e)}，返回检索原文")
            if context_docs:
                fallback = "以下是根据知识库检索到的相关信息：\n\n"
                for i, doc in enumerate(context_docs, 1):
                    fallback += f"{i}. {doc.page_content}\n"
                return fallback
            return "系统暂时无法处理此问题，请稍后重试或联系人工客服。"


if __name__ == '__main__':
    rag = RagSummarizeService()
    print(rag.rag_summarize("小户型适合哪种"))