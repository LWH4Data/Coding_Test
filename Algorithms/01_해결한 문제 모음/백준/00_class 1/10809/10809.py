import sys
sys.stdin = open('input_10809.txt')

word = input()
alpha = ['a', 'b', 'c', 'd', 'e', 'f' ,'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
         'u', 'v', 'w', 'x', 'y', 'z']
idx = []

for i in range(len(alpha)):
    try: 
        idx.append(word.index(alpha[i]))
    except:
        idx.append(-1)
    
print(' '.join(map(str, idx)))
