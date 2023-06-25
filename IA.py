import json

# Carregar o vocabulário a partir do arquivo JSON
def load_vocabulary():
    with open('vocabulario.json', 'r', encoding='utf-8') as file:
        return json.load(file)

# Salvar o vocabulário em um arquivo JSON
def save_vocabulary(vocabulary):
    with open('vocabulario.json', 'w', encoding='utf-8') as file:
        json.dump(vocabulary, file, ensure_ascii=False, indent=4)

# Função para pré-processar a palavra em mandarim
def preprocess_word(word):
    return word.lower().strip()

# Exemplo de uso do vocabulário carregado
def main():
    vocabulary = load_vocabulary()

    while True:
        input_word = input("Digite uma palavra em mandarim: ")
        preprocessed_word = preprocess_word(input_word)

        if preprocessed_word in vocabulary:
            tag = vocabulary[preprocessed_word]["tag"]
            translation = vocabulary[preprocessed_word]["traducao"]

            print("Tag correspondente:", tag)
            print("Tradução em português:", translation)
        else:
            print("Palavra desconhecida.")
            tag = input("Digite a tag correspondente: ")
            translation = input("Digite a tradução em português: ")

            vocabulary[preprocessed_word] = {
                "tag": tag,
                "traducao": translation
            }

            save_vocabulary(vocabulary)
            print("Vocabulário atualizado.")

        choice = input("Deseja continuar conversando? (S/N): ")
        if choice.lower() != "s":
            break

    print("Conversa encerrada.")

if __name__ == "__main__":
    main()
