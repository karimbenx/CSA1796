% Facts about symptoms and conditions
symptom(john, fever).
symptom(john, cough).
symptom(jane, headache).
symptom(jane, sore_throat).

condition(fever, flu).
condition(cough, cold).
condition(headache, stress).
condition(sore_throat, flu).

% Rule to diagnose a patient based on symptoms
diagnose_patient(Patient, Condition) :-
    symptom(Patient, Symptom),
    condition(Symptom, Condition).

% Example queries
% ?- diagnose_patient(john, Condition).
% ?- diagnose_patient(jane, Condition).
