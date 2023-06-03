#!/usr/bin/env python

from user import User

class Student(User):
    knowledge = None

    def learn(self, lesson):
        if self.knowledge == None:
            self.knowledge = []
        
        self.knowledge.append(lesson)