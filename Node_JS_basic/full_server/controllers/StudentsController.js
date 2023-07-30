import readDatabase from '../utils';

export default class StudentsController {
  static getAllStudents(request, response, database) {
    readDatabase(database)
      .then((data) => {
        let line = 'This is the list of our students';
        for (const field in data) {
          if (Object.hasOwn(data, field)) {
            const e = data[field];
            line += `\nNumber of students in ${field}: ${e.count}. ${e.students}`;
          }
        }
        response.end(line);
      })
      .catch((err) => response.status(500).end(err.message));
  }

  static getAllStudentsByMajor(request, response, database) {
    const { major } = request.params;
    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).end('Major parameter must be CS or SWE');
    } else {
      readDatabase(database)
        .then((data) => {
          response.status(200).end(data[request.params.major].students);
        })
        .catch((err) => response.status(500).end(err.message));
    }
  }
}