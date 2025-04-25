it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle',
'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies

print(len(it_companies))

# 2. Add 'Twitter' to it_companies

it_companies.add('Twitter')

# 3. Insert multiple IT companies at once to the set it_companies

it_companies.update(['Tiktok', 'Instagram', 'Snapchat'])

# 4. Remove one of the companies from the set it_companies

it_companies.remove('Snapchat')

# 5. What is the difference between remove and discard

# remove: remove an element from the set, if the element does not exist, it will raise an error
# discard: remove an element from the set, if the element does not exist, it will not raise an error

# 6. Join A and B

print(A.union(B))

# 7. Find A intersection B

print(A.intersection(B))

# 8. Is A subset of B

print(A.issubset(B))

# 9. Are A and B disjoint sets

print(A.isdisjoint(B))

# 10. Join A with B and B with A

print(A.union(B))

# 11. What is the symmetric difference between A and B

print(A.symmetric_difference(B))

# 12. Delete the sets completely

del A

# 13. Convert the ages to a set and compare the length of the list and the set, which one is bigger?

age_set = set(age)

print(len(age) > len(age_set))

      