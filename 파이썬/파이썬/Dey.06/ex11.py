eng_dict = {
    'sun'  : '태양',
    'moon' : '달'  ,
    'star' : '별'  ,
    'space': '우주'
}

for Word in eng_dict:
    print('{} 의 뜻 : {}'.format(Word, eng_dict.get(Word)) )

#딕서너리 .get(key) : key 에 해당하는 갑을 가저온다.