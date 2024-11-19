import google.generativeai as genai
model = genai.GenerativeModel(
    'gemini-1.5-flash',
    generation_config=genai.GenerationConfig(
        temperature=1.0,
        top_p=1,
        top_k=45,
        max_output_tokens=5,
    ))
