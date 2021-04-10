
from flask import Flask, render_template, request
# from transformers import T5ForConditionalGeneration, T5Tokenizer
import requests
# # initialize the model architecture and weights
# model = T5ForConditionalGeneration.from_pretrained("t5-base")
# # initialize the model tokenizer
# tokenizer = T5Tokenizer.from_pretrained("t5-base")

app = Flask(__name__,template_folder='template')

url ="https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"

headers = {
  'x-rapidapi-host': "aylien-text.p.rapidapi.com",
  'x-rapidapi-key': "e83a081f21msh7b1bc6b3ccc6f18p1302c9jsnaab174d2dcce",
  
  }
# GET /recipes/mealplans/generate?timeFrame=day&targetCalories=2000&diet=vegetarian&exclude=shellfish%2C%20olives HTTP/1.1
# X-Rapidapi-Key: e83a081f21msh7b1bc6b3ccc6f18p1302c9jsnaab174d2dcce
# X-Rapidapi-Host: spoonacular-recipe-food-nutrition-v1.p.rapidapi.com
# Host: spoonacular-recipe-food-nutrition-v1.p.rapidapi.com

random_joke = "food/jokes/random"
find = "recipes/findByIngredients"
randomFind = "recipes/random"
desiredRecipie="/recipes/search"
summarizer="/summarize"
label='/classify'


import pyttsx3 
import PyPDF2 as pd

 
def pdf_to_summarized_text(pdf_name):
  book = open(pdf_name, 'rb')
  pdfReader = pd.PdfFileReader(book)
  pages = pdfReader.numPages
  print(pages)
  writer = pd.PdfFileWriter()
  pdf_pages = []
 
  for page in range(0,pages):
      text = pdfReader.getPage(page)
      text = text.extractText()
      pdf_pages.append(text)
  return pdf_pages

  

@app.route('/')
def get_summary():
    print("hello")
    # give title and text
    title="TITLE"
    pages=pdf_to_summarized_text("test_sv.pdf")
    text=""
    print("request sent 1")
    response=[]
    for page in pages:
        querystring = {"title":title,"text":page}
        rsp = requests.request("GET", url + summarizer, headers=headers, params=querystring).json()
        response.append(rsp)
    
    final_summary=''
    for summary in response:
        para=''
        for sentence in summary['sentences']:
            lines=sentence.split('\n')
            for each_line in lines:
                para=para + each_line
        final_summary=final_summary+para+'\n'
    # abstractive summarization if more than 4 pages
    # if len(response)>4:
    #     inputs = tokenizer.encode("summarize: " + final_summary, return_tensors="pt", max_length=512, truncation=True)
    #     outputs = model.generate(
    #     inputs, 
    #     max_length=400, 
    #     min_length=100, 
    #     length_penalty=2.0, 
    #     num_beams=4, 
    #     early_stopping=True)
    
    #     abstractive_summary=tokenizer.decode(outputs[0])
    # else:
    #   print("extractive")
    abstractive_summary=final_summary
    
    # response1 = requests.request("GET", url + label, headers=headers, params=querystring).json()
    print("Response received")
    # print("Label:",response1['label'])
    # print(response)
    # 
    return render_template('showcase.html', summary_extract=abstractive_summary)
 
	
# from flask import Flask
# from flask import render_template
# from flask import make_response
# import pdfkit

from flask_ngrok import run_with_ngrok

run_with_ngrok(app)   

 
app.run()
# if __name__ == '__main__':
#   app.run(debug=True, host='0.0.0.0',threaded=True)
  