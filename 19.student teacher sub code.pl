% Teacher teaching a subject
teaches_subject(teacher1, math).
teaches_subject(teacher2, english).
teaches_subject(teacher3, science).
teaches_subject(teacher4, history).

% Student enrolled in subjects
enrolled_student(student1, math).
enrolled_student(student1, science).
enrolled_student(student1, history).

enrolled_student(student2, english).
enrolled_student(student2, science).

enrolled_student(student3, math).
enrolled_student(student3, history).

% Subject codes
subject_code(math, m101).
subject_code(english, e202).
subject_code(science, s303).
subject_code(history, h404).

% Define relationships between teacher, subject, and subject codes
teacher_code(Teacher, Subject, Code) :-
    teaches_subject(Teacher, Subject),
    subject_code(Subject, Code).

student_code(Student, Subject, Code) :-
    enrolled_student(Student, Subject),
    subject_code(Subject, Code).
