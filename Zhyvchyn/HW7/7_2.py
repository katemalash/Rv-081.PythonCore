string1 = 'Lorem ipsuM dOlOr 456 sit amet, 78  consectetur Adipiscing elit'
string2 = 'Maecenas  mAecenas 654 teMpus 123 ruTrum 111 ferMenTum'
set1 = set(string1)
set2 = set(string2)

both = set1.intersection(set2)
print(sorted(both))
print(sorted(set1))
print(sorted(set2))