from key import cohere_api_key

# Cohere Model
from langchain_community.chat_models import ChatCohere

class CustomChatCohere(ChatCohere):
    def _get_generation_info(self, response):
        # Custom handling of generation info
        generation_info = {}
        if hasattr(response, 'token_count'):
            generation_info["token_count"] = response.token_count
        # Add other attributes if needed
        return generation_info

llm = CustomChatCohere(cohere_api_key=cohere_api_key)

from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence

def generateRestuarantNameMenu(cuisine):
    # Chain 1: Restaurant name
    template1 = 'I want to open a restaurant for {cuisine} food. Suggest only one fancy name for this restaurant'
    prompt1 = ChatPromptTemplate.from_template(template1)
    restaurant_name = prompt1 | llm

    # Chain 2: Restaurant manu Items
    template2 = 'List possible Menus for {cuisine} Restaurant'
    prompt2 = ChatPromptTemplate.from_template(template2)
    menus = prompt2 | llm

    # Sequential Runnable
    recommendation = RunnableSequence(restaurant_name, menus)
    response = recommendation.invoke(cuisine)

    return response.content

