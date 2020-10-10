#english to pig latin 
print("Enter the englidh  message to translate into pig latin:")
message=input()
vowels = ("a","e","i","o","u","y")
pig_latin=[]
for word in message.split():
	
	prefixNonLetters=" "
	while len(word)>0 and not word[0].isalpha():
		prefixNonLetters += word[0]
		word = word[1:]
	if len(word)==0:
		pigLatin.append(prefixNonLetters)
		continue
		
	suffixNonLetter=" "
	while not word[-1].isalpha():
		 suffixNonLetter += word[-1]
		 word = word[:-1]
		
	#Rqmember if the word was in uppercase or title case.
	wasUpper = word.isupper()
	wasTitle = word.istitle()
	word = word.lower()#make the word lowercase for translation
	
	#separaratw tjw consonants at thw start of this word :
		prefixConsonants = " "
		while len(word) > 0 and not word[0] in vowels :
			prefixConstants += word[0]
			word = word[1:]
		#add the pig latin ending of the word
		if prefixConstants != " ":
			word += prefixConstants + "ay"
		else:
			word += "yay"
		#Set the word back to uppercase or title case
		if wasUpper:
			word = word.upper()
		if wasTitle:
			word = word.title()
			
		#add the non-letters back to the start or end  of the word.
		pigLatin.append(prefixNonLetters+word+suffixNonLetter)
#Join all the   back together into a single string.
print (" ".join(pigLatin))
		
		
		 
		 
	
		
	