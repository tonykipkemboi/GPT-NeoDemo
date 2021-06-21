# dependencies
from transformers import pipeline

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

# prompt user to enter starter text
user_input = input('Enter starter sentence: ')

# compute
result = generator(user_input, max_length=500, do_sample=True, temperature=0.9)


def main():

    print(result)

    prom = input('Do you want to download the results? [Y/N] ')

    if prom is None:
        print(prom)

    elif prom == 'Y' or prom == 'y':
        with open('result.txt', 'w') as f:
            f.writelines(result[0]['generated_text'])

    else:
        if prom == 'N' or prom == 'n':
            print('Hope you enjoyed!')


if __name__ == '__main__':
    main()
