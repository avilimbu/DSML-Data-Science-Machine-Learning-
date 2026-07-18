
def idenVowel(sen):
    vowels = "aeiouAEIOU"
    count = 0
    for i in sen:
        if i in vowels:
            count+=1;
    return count


sen = input("Enter the words/ sentence to find out how many vowels will appear: ")
print(f"No of vowels present in you sentence/word = {idenVowel(sen)}")