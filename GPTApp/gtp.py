# dependencies
from transformers import pipeline

generator = pipeline('text-generation', model='EleutherAI/gpt-neo-2.7B')

# prompt user to enter starter text
user_input = input('Enter starter sentence: ')

# compute
result = generator(user_input, max_length=500, do_sample=True, temperature=0.9)


def main():
    print(result)


if __name__ == '__main__':
    main()
