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


docs = ['anna.txt', 'jake.txt', 'anna_two.txt', 'jake_two.txt']
word_arr = create_words_array(docs)
vectors = {}
for doc in docs:
    vectors[doc] = text_to_vec(doc, word_arr)

angles = [
    vec_angle(vectors[docs[0]], vectors[docs[1]]),vec_angle(vectors[docs[0]], vectors[docs[2]]),
    vec_angle(vectors[docs[0]], vectors[docs[3]]), vec_angle(vectors[docs[1]], vectors[docs[2]]),
    vec_angle(vectors[docs[1]], vectors[docs[3]]), vec_angle(vectors[docs[2]], vectors[docs[3]])
]
print("The difference between {} and {} is {}".format(docs[0], docs[1], angles[0]))
print("The difference between {} and {} is {}".format(docs[0], docs[2], angles[1]))
print("The difference between {} and {} is {}".format(docs[0], docs[3], angles[2]))
print("The difference between {} and {} is {}".format(docs[1], docs[2], angles[3]))
print("The difference between {} and {} is {}".format(docs[1], docs[3], angles[4]))
print("The difference between {} and {} is {}".format(docs[2], docs[3], angles[5]))

print("The minimum angle is {}".format(min(angles)))