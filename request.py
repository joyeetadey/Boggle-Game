# import readline
# from functools import reduce
# class Trie(object):
   
#     def __init__(self):
#         self.children = {}
#         self.flag = False
       
#     def add(self, char):
#         self.children[char] = Trie()

#     def insert(self, word):
#         node = self
#         for char in word:
#             if char not in node.children:
#                 node.add(char)
#             node = node.children[char]
#         node.flag = True

#     def contains(self, word):
#         node = self
#         for char in word:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return node.flag

#     def all_suffixes(self, prefix):
#         results = set()
#         if self.flag:
#             results.add(prefix)
#         if not self.children: return results
#         return reduce(lambda a, b: a | b, [node.all_suffixes(prefix + char) for (char, node) in self.children.items()]) | results

#     def autocomplete(self, prefix):
#         node = self
#         for char in prefix:
#             if char not in node.children:
#                 return set()
#             node = node.children[char]
#         return list(node.all_suffixes(prefix))

#     def one_autocomplete(self,prefix):
#         node = self
#         for char in prefix:
#             if char not in node.children:
#                 return False
#             node = node.children[char]
#         return True

# dictionary = Trie()
# with open('allWords.txt','r') as file:
#     for i in file.read().split():
#         dictionary.insert(i)

# board = []
# with open('board.txt','r') as file:
#     for line in file.readlines():
#         board.append([])
#         for char in line.split():
#             board[-1].append(char.upper())

# def print_board(board):
#     for y in board:
#         for x in y:
#             if len(x) == 2:
#                 print(x, end=' ')
#             else:
#                 print(x, end='  ')
#         print()

# def adjacent(val1,val2,lst):
#     try:
#         return (lst.index(val1) - lst.index(val2) in [-1,1])
#     except ValueError:
#         return False
#     return False

# def solve_board(board):
#     def turtle(board, x, y, curr_path, letters=''):
       
#         crossing, min_num_lett = False, 3
       
#         curr_path.append((x,y))
#         letters += str(board[x][y])
       
       
#         if dictionary.contains(letters) and len(letters) >= min_num_lett:
#             all_words.append(letters)
       
     
#         elif not dictionary.one_autocomplete(letters):
#             return 0

#         if (x+1,y) not in curr_path:
#             turtle(board,x+1,y, list(curr_path), str(letters))

#         if (x-1,y) not in curr_path:
#             turtle(board,x-1,y, list(curr_path), str(letters))

#         if (x,y-1) not in curr_path:
#             turtle(board,x,y-1, list(curr_path), str(letters))

#         if (x,y+1) not in curr_path:
#             turtle(board,x,y+1, list(curr_path), str(letters))

#         if not crossing:
#             if (x-1,y+1) not in curr_path and not adjacent((x-1,y),(x,y+1), curr_path):
#                 turtle(board,x-1,y+1,list(curr_path), str(letters))

#             if (x+1,y+1) not in curr_path and not adjacent((x+1,y), (x,y+1), curr_path):
#                 turtle(board,x+1,y+1,list(curr_path), str(letters))
           
#             if (x-1,y-1) not in curr_path and not adjacent((x-1,y), (x,y-1), curr_path):
#                 turtle(board,x-1,y-1,list(curr_path), str(letters))
           
#             if (x+1,y-1) not in curr_path and not adjacent((x+1,y), (x,y-1), curr_path):
#                 turtle(board,x+1,y-1,list(curr_path), str(letters))
#         else:
           
#             if (x+1,y+1) not in curr_path:
#                 turtle(board,x+1,y+1, list(curr_path), str(letters))

#             if (x+1,y-1) not in curr_path:
#                 turtle(board,x+1,y-1, list(curr_path), str(letters))

#             if (x-1,y-1) not in curr_path:
#                 turtle(board,x-1,y-1, list(curr_path), str(letters))

#             if (x-1,y+1) not in curr_path:
#                 turtle(board,x-1,y+1, list(curr_path), str(letters))
   
#     all_words = []
#     for x, y_l in enumerate(board):
#         for y, x_l in enumerate(y_l):
#             curr_path = [(-1,-1)] + [(-1,i) for i in range(len(board)+1)] + [(len(board), i) for i in range(len(board)+1)] + [(i,-1) for i in range(len(board)+1)] + [(i,len(board)) for i in range(len(board)+1)] + ['|||']
#             turtle(board,x,y,[i for i in curr_path])
#     final=list(dict.fromkeys(all_words))
#     return final

# def score_calc(words):
#     solution = solve_board(board)
#     val_table = {0:0,1:0,2:0,3:1,4:1,5:2,6:3,7:5,8:11}
#     total = 0

#     for item in words:
#         if len(item) not in val_table:
#             total += 11
#         else:
#             total += val_table[len(item)]
#     return total


# def check_ans(l,answer):
#     answer=addword()
    
#     solution = solve_board(board)
#     flag=0
#     for word in l:
#         if(answer==word):
#             flag=1
#             break
#         else:
#             flag=0
#     if(flag==1):
#         return True
#     else:
#         return False
           
# def word_return(lists,answer):
#     solution = solve_board(board)
#     if(check_ans(lists,answer)):
#         rightans={answer:'+1'}
#         for x,y in rightans.items():
#             return x,y
#     else:
#         wrongans={answer:'-1'}
#         for x,y in wrongans.items():
#             return x,y
       
# #print_board(board)
# #solution = solve_board(board)
# #print(solution)


# #print(check_ans(solution,ans))

# #max_score=score_calc(solution)
# #print("maximum score is:",max_score)


# def print_res():
#     #final function
#     scoreans=word_return(solution,ans)
#     print(scoreans)
# print_res()