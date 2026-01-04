def has_required_skill(person, skill):
    return all(skill in person['skills'] for skill in skill)

john = {
    'name': 'John Doe',
    'age': 30,
    'skills': ['Python', 'Javascript', 'C++']
}

jane = {
    'name': 'Jane Smith',
    'age': 25,
    'skills': ['Python', 'Java']
}

required_skills = ['Python', 'Javascript']

print(has_required_skill(john, required_skills))
print(has_required_skill(jane, required_skills))