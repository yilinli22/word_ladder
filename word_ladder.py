#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    stack = []
    if(start_word == end_word):
        stack.append(start_word)
        return stack
    word_set = set(line.strip() for line in open(dictionary_file))
    word_dict = {}
    for ele in word_set:
        word_dict[ele] = 0
    stack.append(start_word)
    queue = []
    queue.append(stack)
    while(len(queue) != 0):
        curr_stack = queue.pop(0)
        for key, value in word_dict.items():
            if(_adjacent(key, curr_stack[len(curr_stack) - 1]) & (value == 0)):
                if(key == end_word):
                    curr_stack.append(end_word)
                    return curr_stack
                new_stack = curr_stack.copy()
                new_stack.append(key)
                queue.append(new_stack)
                word_dict[key] += 1
    return None


def verify_word_ladder(ladder):
    test = 0
    if len(ladder) == 1:
        return True
    if len(ladder) == 0:
        return False
    else:
        for i in range(len(ladder) - 1):
            if _adjacent(ladder[i], ladder[i+1]) is True:
                test += 1
            else:
                return False
        return test == len(ladder) - 1


def _adjacent(word1, word2):
    differ = 0
    if len(word1) == len(word2):
        for i in range(0, len(word1)):
            if word1[i] != word2[i]:
                differ += 1
        if differ == 1:
            return True
        else:
            return False
    else:
        return False
