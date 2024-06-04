from flask import Flask,render_template,jsonify,request
from src.helper import download_hugging_face_embedding
from langchain.chains import RetrievalQA
from langchain_pinecone import PineconeVectorStore
from src.prompt import *
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)

embeddings=download_hugging_face_embedding()

index_name="medical-chatbot"

docsearch=PineconeVectorStore.from_existing_index(index_name,embeddings)

PROMPT=PromptTemplate(template=prompt_template,input_variables=["context","question"])

chain_type_kwargs={"prompt":PROMPT}

llm=CTransformers(model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
                  model_type="llama",
                  config={'max_new_tokens':512,'temperature':0.8}
                  )

qa=RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get',methods=['GET','POST'])
def chat():
    msg=request.form["msg"]
    user_message=msg
    print(user_message)
    result=qa.invoke({"query": user_message})
    print("Response : ",result["result"])
    return str(result["result"])

if __name__=='__main__' :
    app.run(debug=True)