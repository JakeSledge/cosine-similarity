# cosine-similarity
The texts with the most similarity have an angle of closest to zero
more can be read about cosine similarity [here](https://stackoverflow.com/questions/1746501/can-someone-give-an-example-of-cosine-similarity-in-a-very-simple-graphical-wa)

## Example:

```python
import sim

train_docs = [
    "current_events/anna/ac1.txt",
    "current_events/anna/ac2.txt",
    "current_events/anna/ac3.txt",
    "current_events/bosh/bc1.txt",
    "current_events/bosh/bc2.txt",
    "current_events/bosh/bc3.txt",
    "current_events/jake/jc1.txt",
    "current_events/jake/jc2.txt",
    "current_events/jake/jc3.txt",
]

test_docs = [
    "current_events/test/at1.txt",
    "current_events/test/bt1.txt",
    "current_events/test/jt1.txt",
]


train_sets = [train_docs[0:3], train_docs[3:6], train_docs[6:9]]
sim.who_wrote_this(train_sets, test_docs[0])
sim.who_wrote_this(train_sets, test_docs[1])
sim.who_wrote_this(train_sets, test_docs[2])
```
