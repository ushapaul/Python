name1=input("what is her name?")
name2=input("what is his name?")
combine_string= name1 + name2
lower_case_string= combine_string.lower()
t=lower_case_string.count('t')
r=lower_case_string.count('r')
u=lower_case_string.count('u')
e=lower_case_string.count('e')
true= t + u + u + e
l=lower_case_string.count('l')
o=lower_case_string.count('o')
v=lower_case_string.count('v')
e=lower_case_string.count('e')
love= l + o + v + e
love_score=int(str(true) + str(love))
if love_score<10 or love_score>90:
    print(f"your score is{love_score} and u go together like coke and mentos")
elif love_score>=40 and love_score<=50:
    print(f"your love is {love_score} and you are alright together")
else:
    print(f"your love score is {love_score}")
