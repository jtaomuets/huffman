# Asks for user input and stores in the variable 'data'
data = input("Please input your data for Huffman encoding: ")
# Prints user's input
print("Your selected input is: ", data)

# Class creation for a node tree
class Tree:
    # Initiating definitions
    def __init__(self, left, right):
        # Defines a node left of the current node
        self.left = left
        # Defines a node right of the current node
        self.right = right
    # Defines root nodes
    def rootNode(self):
        return (self.left, self.right)
    # Defines child nodes
    def childNode(self):
        return (self.left, self.right)

# Function definition for Huffman coding
def huffmanCode(node, left = True, binary = ''):
    # If the data in the node is a string, the following converts it to binary
    if type(node) is str:
        return {node: binary}
    (Left, Right) = node.childNode()
    # Creates a dictionary/associative array
    dictionary = dict()
    binary_0 = binary + '0'
    binary_1 = binary + '1'
    # Updating dictionary for left nodes
    dictionary.update(huffmanCode(Left, True, binary_0))
    # Updating dictionary for right nodes
    dictionary.update(huffmanCode(Right, False, binary_1))
    return dictionary

# Frequency determination
frequency = {}
for i in data:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1

# Anonymous function utilisation
a = lambda x: x[1]
frequency = sorted(frequency.items(), key = a, reverse = True)

huffman_nodes = frequency

# Sorts nodes in ascending order, based upon their frequency
while len(huffman_nodes) > 1:
    (a1, b1) = huffman_nodes[-1]
    (a2, b2) = huffman_nodes[-2]
    huffman_nodes = huffman_nodes[:-2]
    node = Tree(a1, a2)
    # Two smallest nodes are combined to form their parent node
    b3 = b1 + b2
    huffman_nodes.append((node, b3))
    
    huffman_nodes = sorted(huffman_nodes, key = a, reverse = True)

huffman_code = huffmanCode(huffman_nodes [0] [0])

#Huffman coded user input is outputted 
print("Your Huffman code is:")
for (character, frequency) in frequency:
    print(' %-4r |%12s' % (character, huffman_code[character]))
