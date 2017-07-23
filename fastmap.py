from random import choice, seed
from unittest import TestCase


class FastMap:
    """
    Implementation of a map with 4 methods: get(key), put(key, value), remove(key), random()

    My first pass on the white board used a dict / hashmap as the underlying store and kept expanding to deal
    with keeping the time complexity of all methods to O(1). This got messy until I realized that I could turn
    things around and use the hashmap to map a key to the index in a list of the values. This way it's easy
    to implement the random() method on the list of values and addresses some of the book-keeping introduced
    by my first approach. There is still the issue of fragmentation to deal with that is introduced by the
    remove() method. To deal with this we keep track of indices into the values list that have been vacated and
    place them on a list used as a queue. When we put a key, value into the map we first check if there are
    any available positions in the queue. If so, we pop an index off the queue and place the value in the list
    at the location pointed to by the index, and then place the key in the dict with a value of the popped index. If
    no index is available on the queue then the new value is appended to the list and the index placed with the
    key in the map.

    The only internet resources used in developing this code is the Python Time Complexity table to validate the
    time complexity of the operations.

    """
    def __init__(self):
        # for key, index pairs
        self.key_map = {}
        # for the values of the key, value pairs
        self.values = []
        # the list used to track vacated positions in the values list
        self.empty_pos = []

    def get(self, key):
        index = self.key_map.get(key)
        if index is not None:
            return self.values[index]

    def put(self, key, value):
        if key not in self.key_map:
            if len(self.empty_pos) > 0:
                new_pos = self.empty_pos.pop()
                self.values[new_pos] = value
            else:
                new_pos = len(self.values)
                self.values.append(value)
            self.key_map[key] = new_pos
        else:
            self.values[self.key_map[key]] = value

    def remove(self, key):
        if key in self.key_map:
            value = self.values[self.key_map[key]]
            self.values[self.key_map[key]] = None
            self.empty_pos.append(self.key_map[key])
            self.key_map.pop(key)
            return value

    def random(self):
        return choice(self.values)


class TestFastMap(TestCase):
    def setUp(self):
        self.fastmap = FastMap()

    def test_put_get(self):
        self.fastmap.put('key1', 'value1')
        self.fastmap.put('key2', 'value2')
        self.fastmap.put('key1', 'value3')

        self.assertEqual('value3', self.fastmap.get('key1'))
        self.assertEqual('value2', self.fastmap.get('key2'))

    def test_remove(self):
        for i in xrange(10):
            self.fastmap.put('key' + str(i), 'value' + str(i))

        self.assertEqual('value7', self.fastmap.remove('key7'))
        self.assertIsNone(self.fastmap.remove('key7'))
        self.assertEqual(1, len(self.fastmap.empty_pos))

        self.fastmap.put('key20', 'value20')
        self.assertEqual(0, len(self.fastmap.empty_pos))

    def test_random(self):
        seed(1234)
        for i in xrange(100):
            self.fastmap.put('key' + str(i), 'value' + str(i))

        self.assertEqual('value96', self.fastmap.random())
        self.assertEqual('value44', self.fastmap.random())
        self.assertEqual('value0', self.fastmap.random())
