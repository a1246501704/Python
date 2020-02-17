#_*_coding:utf-8_*_

import os

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(BASE_DIR)
ADMIN_DB=os.path.join(BASE_DIR,'db','admin')
SCHOOL_DB=os.path.join(BASE_DIR,'db','school')
TEACHER_DB=os.path.join(BASE_DIR,'db','teacher')
COURSE_DB=os.path.join(BASE_DIR,'db','course')
COURSE_TO_TEACHER_DB=os.path.join(BASE_DIR,'db','course_to_teacher')
CLASSES_DB=os.path.join(BASE_DIR,'db','classes')
STUDENT_DB=os.path.join(BASE_DIR,'db','student')

# if __name__ == '__main__':
#     print(ADMIN_DB)
#     print(SCHOOL_DB)
#     print(TEACHER_DB)
#     print(COURSE_DB)
#     print(COURSE_TO_TEACHER_DB)
#     print(CLASSES_DB)
#     print(STUDENT_DB)

