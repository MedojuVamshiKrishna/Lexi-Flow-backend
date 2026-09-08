from langchain_core.language_models import BaseChatModel
from langchain_core.embeddings import Embeddings
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

OPENAI_PROVIDER = "openai"

# returns the tenant's OpenAI chat model.
def get_chat_model(tenant) -> BaseChatModel:
    if tenant.llm_provider == OPENAI_PROVIDER:
        return ChatOpenAI(model=tenant.llm_model)
    
    raise ValueError(f"Unsupported LLM provider: {tenant.llm_provider}")

# returns the tenant's OpenAI embedding model.
def get_embedding_model(tenant) -> Embeddings:
    if tenant.embedding_provider == OPENAI_PROVIDER:
        return OpenAIEmbeddings(model=tenant.embedding_model)

    raise ValueError(
        f"Unsupported embedding provider: {tenant.embedding_provider}"
    )