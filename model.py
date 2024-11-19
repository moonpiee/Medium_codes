from IPython.display import Markdown
model=genai.GenerativeModel(model_name="gemini-1.5-flash")
response=model.generate_content("What is a black hole?") #generate content
Markdown(response.text) #or use print(response.text) for simple layout
