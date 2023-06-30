-- SCRIPT THAT CREATES A PROCEDURE AddBonus THAT ADDS A NEW CORRECTION FOR A STUDENT
DELIMITER //
DROP PROCEDURE IF EXISTS AddBonus;
CREATE PROCEDURE AddBonus (IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	INSERT INTO projects (name) SELECT project_name WHERE NOT EXISTS (SELECT 1 FROM projects where name = project_name);
	INSERT INTO corrections (user_id, project_id, score)
	VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END; 
//
DELIMITER ;