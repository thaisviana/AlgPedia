
-- Insert das perguntas relativas aos usuários
insert into AlgPedia.algorithm_question(text, priority) values('What is your profile', 2);

insert into AlgPedia.algorithm_userquestion(question_ptr_id) values(1);

insert into AlgPedia.algorithm_questionanswer(question_id, text, value) values(1, 'Professor, UFRJ, IT', 10);
insert into AlgPedia.algorithm_questionanswer(question_id, text, value) values(1, 'Professional, UFRJ, IT', 8);
insert into AlgPedia.algorithm_questionanswer(question_id, text, value) values(1, 'Student, UFRJ, IT', 6);
insert into AlgPedia.algorithm_questionanswer(question_id, text, value) values(1, 'Professor, non-UFRJ, IT', 4);
insert into AlgPedia.algorithm_questionanswer(question_id, text, value) values(1, 'Professional, non-UFRJ, IT', 2);
insert into AlgPedia.algorithm_questionanswer(question_id, text, value) values(1, 'Student, non-UFRJ, IT', 1);
insert into AlgPedia.algorithm_questionanswer(question_id, text, value) values(1, 'non-IT', 0);

-- Insert das perguntas relativas às implementações
insert into AlgPedia.algorithm_question(text, priority) values('How much readable is this code', 4);
insert into AlgPedia.algorithm_question(text, priority) values('This code compiles', 3);
insert into AlgPedia.algorithm_question(text, priority) values('How is this code\'s performance scalability', 5);

insert into AlgPedia.algorithm_implementationquestion(question_ptr_id) values(1);
insert into AlgPedia.algorithm_implementationquestion(question_ptr_id) values(2);
insert into AlgPedia.algorithm_implementationquestion(question_ptr_id) values(3);