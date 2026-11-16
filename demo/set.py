# s={1,2,3,4,5,6,7,8,9,10}
# s.add(11)
# s.remove(5)
# print(s)
# s.discard(6)## this is better then remove because if the element is not present in the set then it will not give any error
# # print(s)


# s1={1,2,3,4,5}
# s2={4,5,6,7,8}
# print(s1.union(s2))###duplicates will be removed
# print(s1.intersection(s2))###common elements will be printed    
# print(s1.difference(s2))###elements of s1 which are not in s2 will be printed
# print(s1.symmetric_difference(s2))###elements which are not common in both sets will be printed
# print(s1.issubset(s2))###checks if s1 is subset of s2
# print(s1.issuperset(s2))###checks if s1 is superset of s2


s={1,2,3,4,5,6,7,8,9,10}
f=frozenset(s)###frozen set is immutable set
print(type(f))
print(f)