names = ['emmet', 'julia', 'bethany', 'alex', 'david', 'noah', 'sydney']
#caps = [name.upper() for name in names if len(name) < 6]
#print(caps)
import random
grade_dict = {name:random.randrange(1,100) for name in names}
print(grade_dict)
#good_grade_dict = {name:grade for (name, grade) in grade_dict.items() if grade >= 60}
good_grade_dict = {x:y for (x, y) in grade_dict.items() if y >= 60}
print(good_grade_dict)