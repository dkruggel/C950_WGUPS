from package import Package

class HashTable:
    # This hash table is of the chaining variety
    # which requires all buckets to be lists
    def __init__(self, initial_capacity=10):
        # Initialization involves creating empty buckets
        # Buckets are initialized as empty lists
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Insert function
    def insert(self, item):
        # Use hash function to return bucket index for insertion
        bucket = hash(item.id) % len(self.table)

        # Get the list at the bucket index
        bucket_list = self.table[bucket]

        # Append bucket list with new item
        bucket_list.append(item)
         
    # Lookup function
    def search(self, key):
        # Use hash function to return bucket index for initial lookup
        bucket = hash(key) % len(self.table)

        # Get the list at the bucket index
        bucket_list = self.table[bucket]

        # If the id exists in the bucket list, let's get the whole item
        for item in bucket_list:
            if item.id == key:
                # Find the index of the item in the bucket list
                item_index = bucket_list.index(item)

                # Return that item!
                return bucket_list[item_index]

        # Sad times, the item was not found
        return None
                

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        if key in bucket_list:
            bucket_list.remove(key)