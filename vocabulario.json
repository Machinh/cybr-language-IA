import json

# Carregar o vocabulário a partir do arquivo JSON
with open('vocabulario.json', 'r', encoding='utf-8') as file:
    loaded_vocabulary = json.load(file)

# Função para pré-processar a palavra em mandarim
def preprocess_word(word):
    return word.lower().strip()

# Exemplo de uso do vocabulário carregado
input_word = input("Digite uma palavra em mandarim: ")
preprocessed_word = preprocess_word(input_word)

tag_and_translation = loaded_vocabulary.get(preprocessed_word, ("Desconhecida", "Desconhecida"))
tag = tag_and_translation[0]
translation = tag_and_translation[1]

print("Tag correspondente:", tag)
print("Tradução em português:", translation)
