import numpy as np 
import copy
import pickle
def source_text_to_int(source_filename):
    CODES = {'<PAD>': 0, '<EOS>': 1, '<UNK>': 2, '<GO>': 3 }
    source_vocab_to_int = copy.copy(CODES)
    counter = 4
    with open(source_filename, encoding='utf-8') as infile:
        for line in infile:
            line = line.lower()
            for word in line.split():
                if word in source_vocab_to_int:  
                    continue  
                else:   
                    source_vocab_to_int[word] = counter
                    counter += 1
    pickle.dump(source_vocab_to_int, open( "./data/Chinese/source_vocab_to_int.pkl", "wb" ) )
    source_vocab_to_int = pickle.load( open( "./data/Chinese/source_vocab_to_int.pkl", "rb" ) )
    source_int_text = []
    with open(source_filename, encoding='utf-8') as infile2:
        for line2 in infile2:
            line2 = line2.lower()
            new_list = []
            for word in line2.split():
                new_list.append(source_vocab_to_int[word])
            source_int_text.append(new_list)
    pickle.dump((source_int_text,source_vocab_to_int), open( "./data/Chinese/source_int_txt.pkl", "wb" ) )
    source_int_text, source_vocab_to_int = pickle.load(open("./data/Chinese/source_int_txt.pkl", "rb"))
    return source_int_text, source_vocab_to_int

def target_text_to_int(target_filename):
    CODES = {'<PAD>': 0, '<EOS>': 1, '<UNK>': 2, '<GO>': 3 }
    target_vocab_to_int = copy.copy(CODES)
    counter = 4
    with open(target_filename, encoding='utf-8') as infile:
        for line in infile:
            line = line.lower()
            for word in line.split():
                if word in target_vocab_to_int:  
                    continue  
                else:   
                    target_vocab_to_int[word] = counter
                    counter += 1
    pickle.dump(target_vocab_to_int, open( "./data/Chinese/target_vocab_to_int.pkl", "wb" ) )
    target_int_text =[]
    target_vocab_to_int = pickle.load( open( "./data/Chinese/target_vocab_to_int.pkl", "rb" ) )
    with open(target_filename, encoding='utf-8') as infile2:
        for line2 in infile2:
            line2 = line2.lower()
            new_list = [] 
            for word2 in line2.split():
                new_list.append(target_vocab_to_int[word])
            new_list[-1] = target_vocab_to_int['<EOS>']
            target_int_text.append(new_list)
    pickle.dump((target_int_text,target_vocab_to_int), open( "./data/Chinese/target_int_txt.pkl", "wb" ) )
    target_int_text, target_vocab_to_int = pickle.load(open("./data/Chinese/target_int_txt.pkl", "rb"))
    return target_int_text, target_vocab_to_int
