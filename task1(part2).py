from abc import ABC, abstractmethod
import os
import json


class ITeacher(ABC):
    @property
    @abstractmethod
    def name(self): pass

    @name.setter
    @abstractmethod
    def name(self, value): pass

    @property
    @abstractmethod
    def courses(self): pass

    @abstractmethod
    def __str__(self): pass


class ICourse(ABC):
    @property
    @abstractmethod
    def course_name(self): pass

    @course_name.setter
    @abstractmethod
    def course_name(self, value): pass

    @property
    @abstractmethod
    def teacher(self): pass

    @teacher.setter
    @abstractmethod
    def teacher(self, value): pass

    @property
    @abstractmethod
    def program(self): pass

    @program.setter
    @abstractmethod
    def program(self, value): pass

    @abstractmethod
    def __str__(self): pass


class ILocalCourse(ABC):
    @property
    @abstractmethod
    def auditory(self): pass

    @auditory.setter
    @abstractmethod
    def auditory(self, value): pass


class IOffsiteCourse(ABC):
    @property
    @abstractmethod
    def address(self): pass

    @address.setter
    @abstractmethod
    def address(self, value): pass


class ICourseFactory(ABC):
    @abstractmethod
    def get_object(self): pass


class Teacher(ITeacher):
    staff_members = []

    def __init__(self, value):
        self.name = value["name"]
        self.__courses = []
        Teacher.staff_members.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Teacher name must be type string")
        self.__name = value

    @property
    def courses(self):
        return self.__courses

    def add_course(self, value):
        self.__courses.append(value)

    def __str__(self):
        return f'Teacher {self.name}, is teaching these courses: {[elem.course_name for elem in self.courses]}'

    @classmethod
    def get_teacher(cls, value):
        for vals in cls.staff_members:
            if vals.name == value:
                return vals
        raise ValueError("Searched teacher doesn't exist")


class Course(ICourse):
    def __init__(self, data):
        self.course_name = data["name"]
        self.teacher = Teacher.get_teacher(data["teacher"])
        self.program = data["program"]
        self.teacher.add_course(self)

    @property
    def course_name(self):
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Course name should be a string")
        self._course_name = value

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, Teacher):
            raise TypeError("Teacher must be an instance of class Teacher")
        self._teacher = value

    @property
    def program(self):
        return self._program

    @program.setter
    def program(self, value):
        if not all(isinstance(vals, str) for vals in value):
            raise TypeError("Program must be a sequence of strings")
        self._program = value

    def __str__(self):
        return f'Course {self.course_name}. Teacher is {self.teacher.name}. The program is {self.program}'


class LocalCourse(ILocalCourse, Course):
    def __init__(self, value):
        super().__init__(value)
        self.auditory = value["auditory"]

    @property
    def auditory(self):
        return self._auditory

    @auditory.setter
    def auditory(self, value):
        if not isinstance(value, str):
            raise TypeError("Auditory must be a string")
        self._auditory = value

    def __str__(self):
        return super().__str__() + f' is taught in {self.auditory}'


class OffsiteCourse(IOffsiteCourse, Course):
    def __init__(self, value):
        super().__init__(value)
        self.address = value["address"]

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        if not isinstance(value, str):
            raise TypeError("Address should be a string")
        self._address = value

    def __str__(self):
        return super().__str__() + f' is located at {self.address}'


class CourseFactory(ICourseFactory):
    def __init__(self, file):
        if not os.path.isfile(file):
            raise ValueError("File does not exist")
        with open(file, "r") as finp:
            self.stash = json.load(finp)

    def get_object(self):
        data = self.stash[0]
        self.stash.pop(0)
        match data.get("type"):
            case "local":
                return LocalCourse(data)
            case "offsite":
                return OffsiteCourse(data)
            case "teacher":
                return Teacher(data)
            case _:
                raise ValueError("Invalid data in json")


def main():
    file = 'data.json'
    objs = CourseFactory(file)
    obj1 = objs.get_object()
    obj2 = objs.get_object()
    obj3 = objs.get_object()
    obj4 = objs.get_object()
    obj5 = objs.get_object()
    obj6 = objs.get_object()
    obj7 = objs.get_object()
    print(obj1)
    print(obj2)
    print(obj3)
    print(obj4)
    print(obj5)
    print(obj6)
    print(obj7)


if __name__ == '__main__':
    main()