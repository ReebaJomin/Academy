from difflib import get_close_matches
dictionary={
    "ambigue":"An ambiguous expression or statement",
    "Blert":"A cowardly person,someone who is weak",
    "comp":"Providing products or services free of charge as a token of appreciation,a favor",
    "Eradicate":"To destroy something completely down to its roots"
}
def meaning(w,dictionary): 
	w = w.lower() 

	if w in dictionary.keys(): 
		return data[w] 
	elif len(get_close_matches(w, dictionary.keys())) > 0:			 
		yn = input("Did you mean % s ? if yes press y else press n: " % get_close_matches(w, dictionary.keys())[0]) 
		yn = yn.lower() 
		if yn == "y": 
			return dictionary[get_close_matches(w, dictionary.keys())[0]] 
		elif yn == "n": 
			return "The word doesn't exist. Please double check it."
		else: 
			return "We didn't understand your entry."
	else: 
		return "The word doesn't exist. Please double check it."
 
word = input("Enter the word to look up meaning:") 
output = meaning(word,dictionary) 
 
else: 
	print(f"The meaning of {word} is '{output}'")  
