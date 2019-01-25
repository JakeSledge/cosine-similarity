# cosine-similarity
The texts with the most similarity have an angle of closest to zero
more can be read about cosine similarity [here](https://stackoverflow.com/questions/1746501/can-someone-give-an-example-of-cosine-similarity-in-a-very-simple-graphical-wa)

Example:

```python
# List of docs to test
docs = ['one.txt', 'two.txt', 'three.txt', 'four.txt']

# Creates array of available words
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
```
