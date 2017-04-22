import nltk
import Image2Vec
# import enchant

# spellChecker = enchant.Dict("en_US")

x_value=[140, 396, 680, 940]
y_value=[402, 680, 946, 1197]

# print x_value[0],y_value[0]

dictionary = set(line.strip() for line in open('words.txt'))

def is_english_word(word):
    if word.lower() in dictionary:
      return True
    return False


matrix = Image2Vec.vector_gen("1.png")
print matrix
# matrix = [["p","a","h","d"],["s", "t", "e", "c"],["r", "n", "h", "l"],["i", "t", "i", "d"]]
print matrix
visit = [
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]
         ]

x_axis = [1,-1,0,0,1,1,-1,-1]
y_axis = [0,0,1,-1,1,-1,1,-1]

outputVector = []
outputVector_string = []

def checkValidity(x,y):
    if (x>=0 and x<4 and y>=0 and y<4):
        return True
    else:
        return False


def findWords(x,y,str,list):
    if len(str)== 10:
        return
    visit[x][y] = 1;
    checkValidWord(str,list);
    for i in range(0,8):
        if(checkValidity(x+x_axis[i],y+y_axis[i]) and visit[x+x_axis[i]][y+y_axis[i]]==0):
            str += matrix[x+x_axis[i]][y+y_axis[i]]
            list.append((x_value[y+y_axis[i]],y_value[x+x_axis[i]]))
            findWords(x+x_axis[i],y+y_axis[i],str,list)
            # print list
            str = str[:-1]
            list.pop()
    visit[x][y] = 0;


def checkValidWord(str,list):
    if (len(str) >= 3 and is_english_word(str)):
        outputVector.append(list[:])
        outputVector_string.append(str)
        # print outputVector
    # if (len(str) >= 3 and spellChecker.check(str.lower())):
    #     outputVector2.append(str)
    return

# for i in range(0,4):
# 	for j in range(0,4):
# 		matrix[i][j] = raw_input()
def syed_afshan():
    s = ""
    l = []
    for i in xrange(0,4):
        for j in xrange(0,4):
            s = matrix[i][j];
            l = [(x_value[j],y_value[i])]
            findWords(i,j,s,l);
    return outputVector, outputVector_string


# outputVector = list(set(outputVector))
# print syed_afshan()
# print len(outputVector)