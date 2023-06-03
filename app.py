from __future__ import annotations
import os, openai
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from typing import Any
from langchain.base_language import BaseLanguageModel
from langchain.chains.llm import LLMChain
import gradio as gr

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
prompt_file = "prompt_template.txt"


class ProductDescGen(LLMChain):
    """LLM Chain specifically for generating multi paragraph rich text product description using emojis."""

    @classmethod
    def from_llm(
        cls, llm: BaseLanguageModel, prompt: str, **kwargs: Any
    ) -> ProductDescGen:
        """Load ProductDescGen Chain from LLM."""
        return cls(llm=llm, prompt=prompt, **kwargs)


def product_desc_generator(product_name, keywords):
    with open(prompt_file, "r") as file:
        prompt_template = file.read()

    PROMPT = PromptTemplate(
        input_variables=["product_name", "keywords"], template=prompt_template
    )
    llm = ChatOpenAI(
        model_name="gpt-3.5-turbo",
        temperature=0.7,
        openai_api_key=OPENAI_API_KEY,
    )

    ProductDescGen_chain = ProductDescGen.from_llm(llm=llm, prompt=PROMPT)
    ProductDescGen_query = ProductDescGen_chain.apply_and_parse(
        [{"product_name": product_name, "keywords": keywords}]
    )
    return ProductDescGen_query[0]["text"]


with gr.Blocks() as demo:
    gr.HTML("""<h1>Welcome to Product Description Generator</h1>""")
    gr.Markdown(
        "Generate Product Description for your products instantly!<br>"
        "Provide product name and keywords related to that product. Click on 'Generate Description' button and multi-paragraph rich text product description will be genrated instantly.<br>"
        "Note: Generated product description is SEO compliant and can be used to populate product information."
    )

    with gr.Tab("Generate Product Description!"):
        product_name = gr.Textbox(
            label="Product Name",
            placeholder="Nike Shoes",
        )
        keywords = gr.Textbox(
            label="Keywords (separated by commas)",
            placeholder="black shoes, leather shoes for men, water resistant",
        )
        product_description = gr.Textbox(label="Product Description")
        click_button = gr.Button(value="Generate Description!")
        click_button.click(
            product_desc_generator, [product_name, keywords], product_description
        )

demo.launch()
