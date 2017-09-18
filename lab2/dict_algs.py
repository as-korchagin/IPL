def useful_func(emps):
    right_emps = set()
    for emp in emps:
        for child in emp.get("children"):
            if child.get("age") > 10:
                right_emps.add(emp.get("name"))
    return right_emps


ivan = {
    "name": "ivan",
    "age": 34,
    "children": [
        {
            "name": "vasia",
            "age": 12},
        {
            "name": "petia",
            "age": 10
        }]
}

darja = {
    "name": "darja",
    "age": 41,
    "children": [
        {
            "name": "kirill",
            "age": 21
        },
        {
            "name": "pavel",
            "age": 15
        }
    ]
}

emps = [ivan, darja]
print("\n".join(useful_func(emps)))
