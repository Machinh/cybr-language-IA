import json
from unidecode import unidecode

def load_vocabulary():
    with open('vocabulario.json', 'r', encoding='utf-8') as file:
        return json.load(file)

def save_vocabulary(vocabulary):
    with open('vocabulario.json', 'w', encoding='utf-8') as file:
        json.dump(vocabulary, file, ensure_ascii=False, indent=4)

def preprocess_word(word):
    normalized_word = unidecode(word.lower().strip().replace(" ", ""))
    return normalized_word

def main():
    vocabulary = load_vocabulary()

    while True:
        input_word = input("Digite uma pergunta em mandarim: ")
        preprocessed_word = preprocess_word(input_word)

        matched_word = None
        for word in vocabulary:
            if preprocessed_word == preprocess_word(word):
                matched_word = word
                break

        if matched_word is not None:
            response = vocabulary[matched_word]["resposta"]
            print("Resposta:", response)
        else:
            print("Pergunta desconhecida.")
            response = input("Digite a resposta para essa pergunta: ")

            vocabulary[preprocessed_word] = {
                "resposta": response
            }

            save_vocabulary(vocabulary)
            print("Vocabulário atualizado.")

        choice = input("Deseja continuar conversando? (S/N): ")
        if choice.lower() != "s":
            break

    print("Conversa encerrada.")

if __name__ == "__main__":
    main()
