class Courses:
    """Models the idea of a UNC course."""
    name: str
    level: int
    prerequisites: list[str]
    
    def __init__(self, name: str, level: int, prerequisites: list[str]) -> None:
        self.name = name
        self.level = level
        self.prerequisites = prerequisites
        pass
    
    def is_valid_course(self, prereq: str) -> bool:
        """Returns whether a course is 400+ and has the given prereq."""
        if (self.level >= 400 and prereq in self.prerequisites):
            return True
        else:
            return False

def find_courses(list_of_courses: list[Courses], prereq: str) -> list[str]:
    """"""
    names: list[str] = []
    for course in list_of_courses:
        if (prereq in course.prerequisites and course.level >= 400):
            names.append(course.name)
    return names
    

