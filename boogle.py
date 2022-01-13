from string import ascii_uppercase #The 26 ascii uppercase characters A to Z
from random import choice
import time

def make_grid(width, height):
   
    #return {(row, col): choice(ascii_uppercase) for row in range(height)
    #    for col in range(width)
    #}

    q=open("input.txt","rt")
    list1=[]
    line=q.readline()
    alp=line.split()
    list1.append(alp)
    
    line=q.readline()
    alp=line.split()
    list1.append(alp)
    
    line=q.readline()
    alp=line.split()
    list1.append(alp)
    #print(list1)
    
    #list1=[['M','A','N'], ['B','A','N'], ['C','A','N']]
    return {(row,col):list1[row][col] for row in range(3)
            for col in range(3)}

#Now we create a new function
def neighbours_of_position(coords):
    row = coords[0] 
    col = coords[1]
    
    top_left = (row - 1, col - 1)
    top_center = (row - 1, col)
    top_right = (row - 1, col + 1)
    
    left = (row, col - 1)
    right = (row, col + 1)
    
    bottom_left = (row + 1, col - 1)
    bottom_center = (row + 1, col)
    bottom_right = (row + 1, col + 1)
    
    return [top_left, top_center, top_right,
            left, right,
            bottom_left, bottom_center, bottom_right]

def all_grid_neighbours(grid):
    neighbours = {}
    for position in grid:
        position_neighbours = neighbours_of_position(position)
        neighbours[position] = [p for p in position_neighbours if p in grid]
    return neighbours
    
def path_to_word(grid, path):
    return "".join([grid[p] for p in path])


# def word_in_dictionary(word, dict):
#     return word in dict

def search(grid, dictionary):
    neighbours = all_grid_neighbours(grid)
    paths = []

    full_words, stems = dictionary
    
    def do_search(path):
        word = path_to_word(grid, path)

        if word in full_words:
            paths.append(path)

        if word not in stems:
            return

        for next_pos in neighbours[path[- 1]]:
            if next_pos not in path:
                do_search(path + [next_pos])
        
    for position in grid:
        do_search([position])
        
    words = []
    
    for path in paths:
        words.append(path_to_word(grid, path))
    return set(words)
    
def get_dictionary(dictionary_file):
    full_words, stems = set(), set()
    
    with open(dictionary_file) as f:
        for word in f:
            word = word.strip().upper()
            full_words.add(word)
            for i in range(1, len(word)):
                stems.add(word[:i])
    return full_words, stems
        
def display_words(words):
    print("Found %s words" % len(words))
    for word in words:
        print(word)
    print("==============")
    
def main():
    a=time.time()
    grid = make_grid(3, 3)
    #print(grid)
    dictionary = get_dictionary("words.txt")
    userin=input().split(' ');
    c=0

    words = search(grid, dictionary)
    display_words(words)
    for x in userin:
        if x in words:
            print(x,"can be made from matrix")
            c=c+1

    print(c*10)
    b=time.time()
    print((b-a)*1000)
    
if __name__ == "__main__":
    main()
