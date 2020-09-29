class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        # self.bucket_array = [None for i in range(capacity)]
        self.table = [None] * capacity
        self.items = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity
        


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # items = 0
        # for i in range(self.capacity):
        #     if self.table[i] is not None:
        #         items += 1
        return self.items / len(self.table)
                    


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here
        hval = 0x811c9dc5
        fnv_32_prime = 0x01000193
        uint32_max = 2 ** 32
        for s in key:
            hval = hval ^ ord(s)
            hval = (hval * fnv_32_prime) % uint32_max
        return hval


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # hash = 5381
        # for x in key:
        #     hash = (( hash << 5) + hash) + ord(x)
        # return hash & 0xFFFFFFFF
        # Your code here
        hash = 5381
        byte_array = key.encode('utf-8')

        for byte in byte_array:
            hash = ((hash * 33) ^ byte) % 0x100000000
        return hash


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        value = self.djb2(key)
        # value = self.fnv1(key)

        return value % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        if self.table[index]:
            new_entry = HashTableEntry(key, value)
            new_entry.next = self.table[index]
            self.table[index] = new_entry
            self.items += 1
            # print(self.table)
            # if self.get_load_factor() > 0.7:
            #     self.resize(self.capacity * 2)
        else:
            self.table[index] = HashTableEntry(key, value)




    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        cur = self.table[index]
        while cur:
            if cur.key == key:
                cur.value = None
                cur.next = None
                self.items -= 1
                return
            if cur.next and cur.next.key == key:
                cur.next = cur.next.next
            cur = cur.next
        


        # if self.table[index]:  // day 1
        #     self.table[index].value = None
        else:
            print("Key not found") 

        


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current = self.table[index]
        # if self.table[index]:     //day 1
        #     hash_entry = self.table[index]
        #     return hash_entry.value
        #     else:
        while current:
            if current.key == key:
                return current.value
            else:
                current = self.table[index].next
        return None;

        # else:
        #     return None    //day 1


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_table = self.table
        self.capacity = new_capacity
        self.table = [None] * new_capacity
        # for i in range(len(old_table)):
        #     cur = old_table[i]
        for i in old_table:
            cur = i
            while cur:
                self.put(cur.key, cur.value)
                cur = cur.next


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
