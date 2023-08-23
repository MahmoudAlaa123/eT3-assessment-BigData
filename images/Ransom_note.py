ransomNote = "aaaabb"
magazine = "abaa"


from collections import Counter


ransomNote_counts = Counter(ransomNote)
magazine_counts = Counter(magazine)

print(ransomNote_counts & magazine_counts)

