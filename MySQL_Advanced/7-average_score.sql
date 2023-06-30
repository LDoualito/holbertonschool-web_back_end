-- SCRIPT THAT CREATES A STORED PROCEDURE THAT COMPUTES AND STORE THE AVERAGE SCORE FOR A STUDENT
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	DECLARE user_score FLOAT;
	SELECT AVG(score) INTO user_score FROM corrections AS c WHERE c.user_id = user_id;
	UPDATE users SET average_score = user_score WHERE id = user_id;
END; //
DELIMITER ;