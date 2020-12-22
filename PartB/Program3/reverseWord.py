class Sentence:
    def __init__(self, s):
        self.s = s
    
    def reverse(self):
        words = self.s.split(' ')

        words.reverse()
        self.rev = ""
        for i in words:
            self.rev += str(i) + " "

        return self.rev

    def calculateNoOfVowels(self):
        self.noOfVowels = 0
        for i in self.s:
            if i.lower() in "aeiou":
                self.noOfVowels += 1

        return self.noOfVowels

s = []

s.append(Sentence(input("Enter sentence 1: ")))
s.append(Sentence(input("Enter sentence 2: ")))
s.append(Sentence(input("Enter sentence 3: ")))

for i in s:
    i.reverse()

sortedSentences = sorted(s, key = lambda x: x.calculateNoOfVowels(), reverse = True)

print("Sorted on vowel count(descending): ")
for i in sortedSentences:
    print("Reverse: ", i.reverse())
    print("No of Vowels: ", i.noOfVowels)
