-- PROCEDURE
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
	DECLARE weight_avg_score FLOAT;
	SET weight_avg_score = (SELECT SUM(score * weight) / SUM(weight)
							FROM users
							JOIN corrections AS c ON users.id=c.user_id
							JOIN projects AS p ON c.project_id=p.id
							WHERE users.id=user_id);
	UPDATE users SET average_score = weight_avg_score WHERE id = user_id;
END; //
DELIMITER ;