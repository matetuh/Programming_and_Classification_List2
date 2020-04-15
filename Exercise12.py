#defining the cesarCiper function
#which takes tekst to encrypt and the d parameter to move the letters in alphabet
def cesarCiper(text,d):
    #alphabet array
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    #out alphabet ( shifted letters )
    out = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    
    result = ""
    
    #here i shift the letters in alphabet
    for i in range (len(alphabet)):
        if i > len(alphabet)-d-1 :
            out[i] = alphabet[i-(len(alphabet)-d)]
        if i <= len(alphabet)-d-1 :
            out[i] = alphabet[i+d]
    
    #then i makes form alphabet and out arrrays strings
    alp = ""
    ou = ""
    
    for x in alphabet:
        alp = alp + x
    for x in out:
        ou = ou + x
        
    # and here i use the maketrans method to shift letters
    trantab = str.maketrans(alp, ou)
    # and here i encrypt the text
    result = text.translate(trantab)
    #then return result (encrypted text)
    return result

#calling a cesarCiper
print(cesarCiper('mateusz',2))

