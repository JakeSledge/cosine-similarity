import numpy as np


def create_words_array(documents):
    words = []
    for doc in documents:
        with open(doc, 'r') as f:
            text = f.read()

        # Turn the text into a list of non repeated words
        text = text.split()
        for word in text:
            w = list(word)
            word = ""
            if ";" in w:
                if ";" not in words:
                    words.append(";")
                w.remove(";")
            for let in w:
                word += let
            if word not in words:
                words.append(word)
    return words


def text_to_vec(doc, words):
    """This funtion creates a vector that represents how frequently words are used in a piece of text"""
    # Create the list of number of times each word appears
    with open(doc, 'r') as f:
        text = f.read()
        text = text.split()
        text_vec = []
        for word in words:
            count = 0
            while word in text:
                count += 1
                text.remove(word)
            text_vec.append(count)
        return text_vec


def vec_angle(vec_one, vec_two):
    """This function uses definition of dot product to find the angle between two vectors"""
    dot = np.dot(vec_one, vec_two)
    mag_one = np.sqrt(np.dot(vec_one, vec_one))
    mag_two = np.sqrt(np.dot(vec_two, vec_two))
    cos_val = dot/mag_one/mag_two
    angle = np.degrees(np.arccos(cos_val))
    return angle


def get_angle_list(docs, vecs):
    angles = {}
    for i in range(len(vecs)-1):
        for j in range(i+1, len(vecs)):
            angles["{} and {}".format(docs[i], docs[j])] = vec_angle(vecs[i], vecs[j])
    return angles


def neat_print(angle_dict):
    i = 0
    for key in angle_dict.keys():
        i += 1
        print(i)
        print("The angle between {} is {}".format(key, angle_dict[key]))


def run(docs):
    words = create_words_array(docs)
    vectors = []
    for doc in docs:
        vectors.append(text_to_vec(doc, words))
    angle_dict = get_angle_list(docs, vectors)
    neat_print(angle_dict)
