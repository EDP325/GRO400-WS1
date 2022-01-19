#!/usr/bin/env python

full_text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Proin porttitor, orci nec nonummy molestie, enim est eleifend mi, non fermentum diam nisl sit amet erat. Duis semper. Duis arcu massa, scelerisque vitae, consequat in, pretium a, enim. Pellentesque congue. Ut in risus volutpat libero pharetra tempor. Cras vestibulum bibendum augue. Praesent egestas leo in pede. Praesent blandit odio eu enim. Pellentesque sed dui ut augue blandit sodales. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Aliquam nibh. Mauris ac mauris sed pede pellentesque fermentum. Maecenas adipiscing ante non diam sodales hendrerit.
"""

def is_vowel(letter):
    assert(len(letter) == 1)
    return letter.lower() in ['a', 'e', 'i', 'o', 'u', 'y']

def vowel_anayze(list):
    num_of_vowel = 0
    for word in list:
        if word[0] in ['a', 'e', 'i', 'o', 'u', 'y']:
            num_of_vowel += 1

    return num_of_vowel

    

if __name__ == "__main__":

    words = full_text.split()
    num_of_words = len(words)
    num_of_vowel = vowel_anayze(words)

    print("Num of words: %d /t Num of vowels: %d",num_of_words,num_of_vowel)



