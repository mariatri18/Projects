alphabet = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"

def encrypt(myText):
    cypherText = ""
	    for char in myText:
            if char in alphabet:
                newPosition = (alphabet.find(char) + 13) % 24
        	    cypherText += alphabet[newPosition]
    	    else:
                cypherText += char
    return cypherText

text = input("Δώσε τη φράση: ")
print(encrypt(text))
