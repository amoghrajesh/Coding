import re
import inflect
from collections import Counter
from nltk.corpus import words
allwords=set(words.words())
inflect=inflect.engine()
def viterbi_segment(text):
    probs, lasts = [1.0], [0]
    for i in range(1, len(text) + 1):
        prob_k, k = max((probs[j] * word_prob(text[j:i]), j)
                        for j in range(max(0, i - max_word_length), i))
        probs.append(prob_k)
        lasts.append(k)
    words = []
    i = len(text)
    while 0 < i:
        words.append(text[lasts[i]:i])
        i = lasts[i]
    words.reverse()
    return words, probs[-1]

def word_prob(word):
    return my_dictionary[word] / total

def words(text):
    return re.findall('[a-z]+', text.lower())

my_dictionary = Counter(words(open('big.txt').read()))
max_word_length = max(map(len, my_dictionary))
total = float(sum(my_dictionary.values()))

'''alpha=viterbi_segment('itthe')
alpha=alpha[0]
alpha=' '.join(alpha)
print(alpha)'''

s="this photo is taken inside of an office is standing in front of white walls has white hairthe girl has brown white clouds that is crossing from the back of white people are sitting on top of the white itemsthe building is large white "
s3=" is white in a is the one box on the above is a that black waste basket on the ground to the is a"
s2="a brown haired man with a small soul patch is wearing a blue shirtabove hanging on the wall a skull mask covered glitterthere are yellow flowers around the skull and long big feathers all around the flowersthere are brown feathers blue and red feathers"
s1="small wooden table has plates on itthe table is made of light brown woodthere are two plates that are white and one plate that is white with a black are forks and two knives on the table as well"
s=s.split()
ans=[]
ans.append(s[0].capitalize())
for i in range(1,len(s)):
    if s[i] not in allwords and inflect.singular_noun(s[i]) is False:
        alpha=viterbi_segment(s[i])
        print("viterbi segment",alpha)
        alpha=alpha[0]
		
        if len(alpha)==2:
            a,b=alpha
            ans.append(a)
            ans.append('.')
            ans.append(b.capitalize())
        else:
            #alpha=strmap(str
            ans.append(alpha[0])

    elif s[i] not in allwords and inflect.singular_noun(s[i]) is True:
        ans.append(s[i])   
            
        '''a,b=alpha
        ans.append(a)
        ans.append('.')
        ans.append(b.capitalize())'''
    else:
        ans.append(s[i])
ans.append('.')
print(' '.join(ans))
        
    
    
