p1, p2 = 'Python', 'python'

p1 == p2
#* False
p1.lower() == p2.lower()
#* True

s1, s2, s3 = 'Σ', 'σ', 'ς' # Sigma

# Return a copy of the string converted to lowercase.
s1.lower() == s2.lower()
#* True
s1.lower() == s3.lower()
#* False

# Return a version of the string suitable for caseless comparisons.
s1.casefold() == s2.casefold()
#* True
s1.casefold() == s3.casefold()
#* True