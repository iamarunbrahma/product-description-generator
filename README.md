# Product Description Generator
Generate SEO-compliant product descriptions using product titles and meta-keywords provided by the user.
Implemented custom LLMChain function from the Langchain and few-shot prompting technique to generate multi-paragraph rich text product description for each product name and its corresponding keywords. Built a gradio app as a frontend demo to showcase the process.

This project is hosted on HuggingFace Spaces: [Live Demo of Product Description Generator](https://huggingface.co/spaces/heliosbrahma/product-description-generator).

## Steps:-
- Provide the product name and keywords separated by commas
- Using the custom prompt template and ChatOpenAI model, call the custom LLM chain to generate a product description

## How to run it locally:-
To run this app locally, first clone this repo using `git clone`.<br><br>
Now, install all libraries by running the following command in the terminal:<br>
```python
pip install -r requirements.txt
```
<br><br>
Now, run the app from the terminal:<br>
```python
gradio app.py
```
