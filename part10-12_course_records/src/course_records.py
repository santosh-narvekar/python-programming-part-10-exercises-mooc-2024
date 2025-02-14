# tee ratkaisusi tänne

# APPLICATION LOGIC
class Course:
  def __init__(self,name:str,grade:int,credits:int):
    self.__name = name
    self.__grade = grade
    self.__credits = credits
  
  def grade(self):
    return self.__grade
  
  def credits(self):
    return self.__credits
  
  def __str__(self):
    return f"{self.__name} ({self.__credits} cr) grade {self.__grade}"
  
class MyCourses:
  def __init__(self):
    self.__courses = {}

  def get_course(self,name):
    if name in self.__courses:
      return self.__courses[name]
    else:
      return None
  
  def add_course(self,name:str,grade:int,credits:int):
      if name in self.__courses:
         if self.__courses[name].grade() < grade:
            self.__courses[name] = Course(name,grade,credits)    
      else:
        self.__courses[name] = Course(name,grade,credits)    
  
  def print_statistics(self,credits,grades,courses_done):
    
    print(f"{courses_done} completed courses, a total of {credits} credits")
    print(f"mean {(sum(grades) / len(grades)):.1f}")
    print("grade distribution")

    for grade in range(5,0,-1):
      print(f"{grade}: { "x" * grades.count(grade)}")
      
  def get_statistics(self):
   
    grades = [] 
    courses_done = 0 
    credits = 0
    
    for course in self.__courses.values():
      credits += course.credits()
      grades.append(course.grade())
      courses_done += 1
      
    self.print_statistics(credits,grades,courses_done)

# UI LOGIC
class CourseApplication:
  def __init__(self):
    self.__myCourses = MyCourses()

  def help_commands():
    print("1 add course")
    print("2 get course data")
    print("3 statistics")
    print("0 exit")
 
  help_commands()

  def add_course(self):
    name = input("course: ")
    grade = int(input("grade: "))
    credits = int(input("credits: "))

    self.__myCourses.add_course(name,grade,credits)
  
  def get_course(self):
    name =  input("course: ")

    course_exists = self.__myCourses.get_course(name)  
    if course_exists:
      print(course_exists)
    else:
      print("no entry for this course")
 
  def get_statistics(self):
    self.__myCourses.get_statistics()

  def execute(self):
    while True:
      print()
      command = int(input("command: "))

      if command == 0:
        break

      if command == 1:
        self.add_course()

      if command == 2:
        self.get_course()

      if command == 3:
         self.get_statistics()
    
courseUi = CourseApplication()
courseUi.execute()