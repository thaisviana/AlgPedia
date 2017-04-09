alter table AlgPedia.algorithm_algorithm modify name varchar(80);
alter table algorithm_implementation add column date datetime default current_timestamp not null;
update algorithm_algorithm set name = replace(name, '\n', '');