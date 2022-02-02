marks_catCollection = {'id1':
                           {'mark_name': ['Ababagalamaga'],
                            'price': ['200$'],
                            'year': [1981]
                            },
                       'id2':
                           {'mark_name': ['Коти біля Диканьки'],
                            'price': ['300$'],
                            'year': [1945]
                            },
                       'id3':
                           {'mark_name': ['Ababagalamaga'],
                            'price': ['200$'],
                            'year': [1981]
                            },
                       }
result = {}
for key, value in marks_catCollection.items():
    if value not in result.values():
        result[key] = value

print(result)

marks_carCollection = {'id1':
                           {'mark_name': ['Ferrari'],
                            'price': ['200$'],
                            'year': [1921]
                            },
                       'id2':
                           {'mark_name': ['JesusCar'],
                            'price': ['300$'],
                            'year': [1945]
                            },
                       'id3':
                           {'mark_name': ['BentlyMark'],
                            'price': ['200$'],
                            'year': [1981]
                            },
                       }
print(marks_carCollection)

marks_elephantsCollection = {'id1':
                           {'mark_name': ['Маманьтоньок з СРСР'],
                            'price': ['200$'],
                            'year': [1982]
                            },
                       'id2':
                           {'mark_name': ['Elephant Жорік'],
                            'price': ['300$'],
                            'year': [1945]
                            },
                       'id3':
                           {'mark_name': ['Gosha228'],
                            'price': ['200$'],
                            'year': [1981]
                            },
                       }
print(marks_elephantsCollection)
