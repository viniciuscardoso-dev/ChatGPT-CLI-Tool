import openai
import os
openai.api_key = os.environ['API_KEY']

def perguntar_gpt(prompt):
    response = openai.Completion.create(
          engine="text-davinci-003",
                prompt=prompt,
                      max_tokens=1024,
                            n=1,
                                  stop=None,
                                        temperature=0.7,
                                            )
    answer = response.choices[0].text
    return answer.strip()

# perguntar ao usuário qual a pergunta a ser feita ao chat GPT
pergunta = input("Digite sua pergunta: ")

# chamar a função perguntar_gpt com a pergunta do usuário
resposta = perguntar_gpt(pergunta)
# imprimir a resposta
print(resposta)
