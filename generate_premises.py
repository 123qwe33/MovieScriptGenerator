import openai


with open('openaiapikey.txt', 'r') as infile:
    openai.api_key = infile.read()



def gpt3_completion(prompt, engine='text-curie-001', temp=0.7, top_p=1.0, tokens=250, freq_pen=0.0, pres_pen=0.0, stop=['User:','RAVEN:']):
    max_retry = 5
    retry = 0
    while True:
        try:
            response = openai.Completion.create(
                engine=engine,         # use this for standard models
                #model=engine,           # use this for finetuned model
                prompt=prompt,
                temperature=temp,
                max_tokens=tokens,
                top_p=top_p,
                frequency_penalty=freq_pen,
                presence_penalty=pres_pen,
                stop=stop)
            text = response['choices'][0]['text'].strip()
            text = re.sub('\s+', ' ', text)
            save_gpt3_log(prompt, text)
            return text
        except Exception as oops:
            retry += 1
            if retry >= max_retry:
                return None
            print('Error communicating with OpenAI:', oops)
            sleep(1)