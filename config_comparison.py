from google.api_core import retry
retry_policy={"retry":retry.Retry(predicate=retry.if_transient_error,initial=10,multiplier=1.5,timeout=300)}
top_k_lis=[10,50,80]
top_p_lis=[0.2,0.6,1.0]
temp_lis=[0.0,1.0,2.0]
models_lis={}
for k in top_k_lis:
    for p in top_p_lis:
        for t in temp_lis:
            name=f"model_k{k}_p{p*100}_t{t}"
            model=genai.GenerativeModel(
                        model_name='gemini-1.5-flash',
                        generation_config=genai.GenerationConfig(
                        temperature=t,
                        top_k=k,
                        top_p=p)
                        )
            models_lis[name]=model.generate_content("You are a creative writer. Craft a 1-line story on moon.",request_options=retry_policy).text
print(models_lis)
