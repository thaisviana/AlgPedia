DELIMITER $$

DROP PROCEDURE IF EXISTS calculate_user_evaluation_contribution_support$$

CREATE PROCEDURE calculate_user_evaluation_contribution_support(IN implementation_id INT(11), IN user_id INT(11), OUT ct INT(11), OUT pt INT(11))
BEGIN

	DECLARE impl_id INT(11);
	DECLARE u_id INT(11);

	SET impl_id = implementation_id;
	SET u_id = user_id;

	SELECT cic + ccc + cclp + IF(cp IS NULL, 0, cp) + IF(cai IS NULL, 0, cai) ct,
	qpt + 11 _div
	INTO ct, pt
	FROM (
		SELECT u.id user_id, impl.id impl_id,
		IF((SELECT 1
				FROM algorithm_interest i
				WHERE i.user_id = u.id AND a.classification_id = impl.id
		) IS NULL, 0, 3) cic, # Contribuicao do interesse do usuario na classificacao da implementacao/algoritmo
		IF((SELECT 1
				FROM algorithm_proeficiencyscale ps
				INNER JOIN algorithm_classificationproeficiencyscale cps ON ps.id = cps.proeficiencyscale_ptr_id
				WHERE cps.classification_id = a.classification_id
		) IS NULL, 0, 5) ccc, # Contribuicao do conhecimento do usuario na classificacao da implementacao/algoritmo
		IF((SELECT 1
				FROM algorithm_proeficiencyscale ps
				INNER JOIN algorithm_programminglanguageproeficiencyscale plps ON ps.id = plps.proeficiencyscale_ptr_id
				WHERE plps.programming_language_id = impl.programming_language_id
		) IS NULL, 0, 3) cclp, # Contribuicao do conhecimento do usuario na linguagem de programacao da implementacao
		(SELECT SUM(qa.value)
			FROM algorithm_userquestionanswer uqa
			INNER JOIN algorithm_question q ON q.id = uqa.user_question_id
			INNER JOIN algorithm_userquestion uq ON uq.question_ptr_id = q.id
			INNER JOIN algorithm_questionanswer qa ON qa.id = uqa.question_answer_id
			WHERE uqa.user_id = u.id
		) cp, # Total da contribuicao do perfil do usuario
		(SELECT SUM(qa.value)
			FROM algorithm_implementationquestionanswer iqa
			INNER JOIN algorithm_question q ON q.id = iqa.implementation_question_id
			INNER JOIN algorithm_implementationquestion iq ON iq.question_ptr_id = q.id
			INNER JOIN algorithm_questionanswer qa ON qa.id = iqa.question_answer_id
			WHERE iqa.user_id = u.id AND iqa.implementation_id = impl.id
		) cai, # Contribuicao da avaliacao da implementacao pelo usuario
		(SELECT SUM(q.priority)
			FROM algorithm_question q
		) qpt # Soma de todas os pesos de todas as perguntas
		FROM auth_user u, algorithm_implementation impl
		INNER JOIN algorithm_algorithm a ON a.id = impl.algorithm_id
		WHERE u.id = u_id AND impl.id = impl_id
	) a;
END$$

DROP PROCEDURE IF EXISTS calculate_implementation_reputation$$

CREATE PROCEDURE calculate_implementation_reputation(implementation_id INT(11))
BEGIN
	DECLARE sum DOUBLE;
	DECLARE impl_id INT(11);
	DECLARE alg_id INT(11);

	SET impl_id = implementation_id;

	SELECT sum(val)/count(1) INTO sum FROM algorithm_usercontribution WHERE implementation_id = impl_id;
	SELECT algorithm_id INTO alg_id FROM algorithm_implementation where id = impl_id;

	UPDATE algorithm_implementation SET reputation = sum WHERE id = impl_id;

	SELECT SUM(reputation) INTO sum FROM algorithm_implementation WHERE algorithm_id = alg_id;

	UPDATE algorithm_algorithm SET reputation = sum WHERE id = alg_id;
END$$

DROP PROCEDURE IF EXISTS calculate_user_evaluation_contribution$$

CREATE PROCEDURE calculate_user_evaluation_contribution(IN implementation_id INT(11), IN user_id INT(11)) proc_label:
BEGIN
	DECLARE impl_id INT(11);
	DECLARE u_id INT(11);
	DECLARE ct INT(11); # Contribuicao total
	DECLARE pt INT(11); # Peso total
	DECLARE contribution_id INT(11);
	DECLARE last_op VARCHAR(32);

	IF NOT EXISTS(select 1 from algorithm_implementation i where i.id = implementation_id) THEN
		SELECT 'No Implementation';
		LEAVE proc_label;
	END IF;

	IF NOT EXISTS(select 1 from auth_user u where u.id = user_id) THEN
		SELECT 'No User';
		LEAVE proc_label;
	END IF;

	SET impl_id = implementation_id;
	SET u_id = user_id;

	CREATE TABLE IF NOT EXISTS algorithm_usercontribution (
		id INT(11) PRIMARY KEY AUTO_INCREMENT,
		user_id INT(11),
		implementation_id INT(11),
		val DOUBLE,
		FOREIGN KEY (user_id) references auth_user(id),
		FOREIGN KEY (implementation_id) references algorithm_implementation(id)
	);
	
	CALL calculate_user_evaluation_contribution_support(impl_id, u_id, ct, pt);

	IF ct IS NULL OR pt IS NULL THEN
		SELECT 'No CT or PT';
		LEAVE proc_label;
	END IF;

	SELECT id INTO contribution_id
	FROM algorithm_usercontribution uc
	WHERE uc.user_id = u_id AND uc.implementation_id = impl_id;
	
	IF contribution_id IS NULL THEN
		INSERT INTO algorithm_usercontribution (user_id, implementation_id)
		VALUES(u_id, impl_id);
		
		SET contribution_id = LAST_INSERT_ID();
	END IF;

	UPDATE algorithm_usercontribution SET val=(ct/pt) WHERE id = contribution_id;

	CALL calculate_implementation_reputation(impl_id);

	SELECT 'Done';
END$$

DELIMITER ;