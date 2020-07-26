# https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    stuart_count = 0
    kevin_count = 0

    vowels = {"A", "E", "I", "O", "U"}

    length = len(string)
    for i, letter in enumerate(string):
        words = length - i 
        if letter in vowels:
            kevin_count += words
        else:
            stuart_count += words

    if kevin_count > stuart_count:
        print(f"Kevin {kevin_count}")
    elif kevin_count < stuart_count:
        print(f"Stuart {stuart_count}")
    else:
        print("Draw")

    

if __name__ == '__main__':
    string = "BANANA"
    minion_game(string)