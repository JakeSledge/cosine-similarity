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
    """This creates a list of angles between all documents"""
    angles = {}
    for i in range(len(vecs)-1):
        for j in range(i+1, len(vecs)):
            angles["{} and {}".format(docs[i], docs[j])] = vec_angle(vecs[i], vecs[j])
    return angles


def neat_print(angle_dict):
    """This nicely prints all of the angles between documents"""
    for key in angle_dict.keys():
        print("The angle between {} is {}".format(key, angle_dict[key]))


def run(docs):
    """This is a testing function designed to print out all possible angles in docs"""
    words = create_words_array(docs)
    vectors = []
    for doc in docs:
        vectors.append(text_to_vec(doc, words))
    angle_dict = get_angle_list(docs, vectors)
    neat_print(angle_dict)


def get_average_word_vec(docs, words):
    """This creates an average word vector"""
    vectors = []
    for doc in docs:
        vectors.append(text_to_vec(doc, words))
    avg_vec = []
    for i in range(len(vectors[0])):
        total = 0
        for vec in vectors:
            total += vec[i]
        avg_vec.append(total/len(vectors))
    return avg_vec


def train_test_angles(avg_vecs, test_vecs):
    angles = {}
    for t_doc, t_vec in test_vecs.items():
        for a_doc, a_vec in avg_vecs.items():
            angles["{} and {}".format(a_doc, t_doc)] = vec_angle(a_vec, t_vec)
    return angles


def who_wrote_this(train_sets, test):
    """This function tells you who wrote each of the documents in the test list. The train_sets is a list of lists where
    each nested list contains docs all written by one person"""

    # This creates a list of all the documents and a word array from that. Then using that word array, creates average
    # vectors of each person in train_sets
    total = [test,]
    for person in train_sets:
        total = total + person
    words = create_words_array(total)
    avg_vecs = {}
    for person in train_sets:
        avg_vecs["{} avg".format(person[0])] = get_average_word_vec(person, words)

    # Now create vectors of the test documents
    test_vecs = {}
    test_vecs[test] = text_to_vec(test, words)
    angles = train_test_angles(avg_vecs, test_vecs)
    angle_vals = angles.values()
    min_angle = min(angle_vals)
    for k, v in angles.items():
        if v == min_angle:
            print("{} were written by the same authors".format(k))
