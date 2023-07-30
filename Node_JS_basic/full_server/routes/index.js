import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

const router = require('express').Router();

router.get('/', (request, response) => AppController.getHomepage(request, response));
router.get('/students', (request, response) => StudentsController.getAllStudents(request, response, process.argv[2]));
router.get('/students/:major', (request, response) => StudentsController.getAllStudentsByMajor(request, response, process.argv[2]));

export default router;
