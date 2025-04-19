import json

with open('my_words//my_nouns.txt') as f:
	my_nouns = json.load(f)

with open('my_words//my_verbs.txt') as f:
	my_verbs = json.load(f)

with open('my_words//my_adjectives.txt') as f:
	my_adjectives = json.load(f)	

import random	

def merge_dicts(x, y, z):
	w = x.copy()
	w.update(y)
	w.update(z)
	return w
	
my_dict = merge_dicts(my_nouns, my_verbs, my_adjectives)
	
word_list = list(my_dict)

while len(word_list) != 0:
	m = random.choice(word_list)
	if m in my_nouns:
		temp_list = list(my_nouns)
		answer_choices_list = [my_dict[m]]
		while len(answer_choices_list) < 5:
			answer_choices_list.append(my_dict[random.choice(temp_list)])
			answer_choices_list = list(set(answer_choices_list))
	elif m in my_verbs:
		temp_list = list(my_verbs)
		answer_choices_list = [my_dict[m]]
		while len(answer_choices_list) < 5:
			answer_choices_list.append(my_dict[random.choice(temp_list)])
			answer_choices_list = list(set(answer_choices_list))
	else:
		temp_list = list(my_adjectives)
		answer_choices_list = [my_dict[m]]
		while len(answer_choices_list) < 5:
			answer_choices_list.append(my_dict[random.choice(temp_list)])
			answer_choices_list = list(set(answer_choices_list))
	print (m[:1].upper() + m[1:])
	answer_choices = {}
	q = 1
	for q in range(1,6):
		t_answer_choices_list = answer_choices_list
		answer_index_list = ['A','B','C','D','E']
		answer_choices[answer_index_list[q-1]] = random.choice(t_answer_choices_list)
		t_answer_choices_list.remove(answer_choices[answer_index_list[q-1]])
		q += 1
	if answer_choices[input('\n'.join("{}: {}".format(k, v) for k, v in answer_choices.items()) + '\n').upper()] == my_dict[m]:
		word_list.remove(m)
		if len(word_list) > 1:
			print ('Correct! \n' + str(len(word_list)) + ' to go! \n')
		elif len(word_list) == 1:
			print ('Correct! \nLast one!... hopefully \n')
		else:
			print('Congratulations! You are done!')
	else:
		print ('Wrong! \n')
		print (m[:1].upper() + m[1:] + ": " + my_dict[m])
		

			
		
	
	

	
