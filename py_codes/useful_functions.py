# Some useful functions
# Function to detect palindromes
def is_palindrome(text):
    text = text.lower()
    return text[::-1] == text

print(is_palindrome('mom'))

# Counting repating characters in string
def count_characters(strings):
    count_dict = {}
    for c in strings:
        if c in count_dict:
            count_dict[c] += 1
        else:
            count_dict[c] = 1
    print(count_dict)

count_characters("hello")


movies = ["Interstellar", "Inception", "The Prestige", "The Dark Knight", "Batman Begins"]
ratings = [1, 10, 10, 8, 6]

#Combining two lists
def comb_two_lists(l1, l2):
    new_list = []
    for tree in zip(l1, l2):
        new_list.append(tree)
    print(new_list)

comb_two_lists(movies, ratings)

# Anagram Detection
def is_anagram(s1,s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ', '').lower()
    return 'Yes' if len(s2) == len(s1) and sorted(s2) == sorted(s1) else 'No'

print(is_anagram('cinema','iceman'))

# Recursion example
def bottles_of_beer(bob):
    if bob < 1:
        print("""No more bottles of beer on the wall. No more bootles of beer.""")
        return
    tmp = bob
    bob -= 1
    print("""{} bottles of  beer on the wall. {} bootles of beer. Take one down, pass it around,
             {} bottles of beer on the wall.""".format(tmp, tmp, bob))
    bottles_of_beer(bob)

bottles_of_beer(10)

def print_to_zero(n):
    if n < 0:
        return
    print(n)
    print_to_zero(n-1)

print_to_zero(10)


# Binary Search (sorted list)
def binary_search(the_list, item):
    first = 0
    last = len(the_list)-1
    found = False
    while first<=last and not found:
        mid = (first + last)//2
        if the_list[mid] == item:
            found = True
        else:
            if item < the_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return print(found)

l = [10, 12, 13, 14, 17, 19, 22, 27]
item = 22

binary_search(l, item)

# Find duplicates
def find_duplicate(a_list):
    dups = []
    a_set = set()
    for item in a_list:
        length_one = len(a_set)
        a_set.add(item)
        length_two = len(a_set)
        if length_one == length_two:
            dups.append(item)
    return dups

a_list = ['Susan Collins', 'Carol Flora', 'Jeniffer Lawrence', 'Susan Collins']
print(find_duplicate(a_list))

# Nested loops
i_string = "Buy 1 get 2 free"
new_list = [c for c in i_string if c.isdigit()][-1] #produce the last digit on the string
print(new_list)

# Detect repeating values in two lists
def intersection(l1, l2):
    l3 = [value for value in l1 if value in l2]
    return l3

l1 = [2, 43, 48, 62, 64, 28, 3]
l2 = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]
print(intersection(l1,l2))

# Detect repeating values in two lists METHOD 2
def intersection_m2(l1, l2):
    set1 = set(l1)
    set2 = set(l2)
    new_list = list(set1.intersection(set2))
    return new_list

print(intersection_m2(l1,l2))

# Linked List
# Creating Linked Lists
import random

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def print_node(self):
        print(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        if not self.head:
            self.head = Node(data)
            return
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.data, end = " ")
            node = node.next
        print("\n")

    def search(self, target):
        current = self.head
        while current != None:
            if current.data == target:
                print("Found it!")
                return True
            else:
                current = current.next
        print("Not found.")
        return False

the_list = LinkedList()

for j in range(0, 20):
    j = random.randint(1, 30)
    the_list.append_node(j)
the_list.print_list()
the_list.search(10)