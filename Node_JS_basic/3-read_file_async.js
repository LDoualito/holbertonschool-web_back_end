const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) return reject(Error('Cannot load the database'));
      // Split data in lines
      const dataLines = data.split('\n');
      // Filter empty lines
      const lines = dataLines.filter((line) => line.length !== 0);
      // Declare a set for fields because set's elements can't be duplicate
      const field = new Set();
      // Add to the set the student's field
      lines.forEach((line) => {
        const fieldStudent = line.split(',')[3];
        if (fieldStudent !== 'field') field.add(fieldStudent);
      });
      console.log(`Number of students: ${lines.length - 1}`);
      field.forEach((f) => {
        const students = lines.filter((line) => line.split(',')[3] === f);
        console.log(`Number of students in ${f}: ${students.length}. List: ${students.map((student) => student.split(',')[0]).join(', ')}`);
      });
      return resolve();
    });
  });
}

module.exports = countStudents;
