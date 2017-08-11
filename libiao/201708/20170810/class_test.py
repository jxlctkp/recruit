#!/usr/bin/python

class Student:
  stu_id=0
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
    Student.stu_id+=1
  def displayCount(self):
    print "Total student %d",Student.stu_id
  def displayStudent(self):
    print "Name: ",self.name,"Salay: ",self.salary
student1=Student("libiao",100)
student2=Student("luck",102)
student1.displayStudent()
student2.displayStudent()
Student.stu_id

