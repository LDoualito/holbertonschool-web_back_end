const fs = require('fs');
const express = require('express');

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
      const all = {};
      all.numberStudents = `Number of students: ${lines.length - 1}\n`;
      all.listStudents = [];
      field.forEach((f) => {
        const students = lines.filter((line) => line.split(',')[3] === f);
        all.listStudents.push(`Number of students in ${f}: ${students.length}. List: ${students.map((student) => student.split(',')[0]).join(', ')}`);
      });
      return resolve(all);
    });
  });
}

const app = express();
const port = 1245;

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  res.write('This is the list of our students\n');
  countStudents(process.argv[2])
    .then((data) => {
      res.write(data.numberStudents);
      res.end(data.listStudents.join('\n'));
    })
    .catch((err) => {
      res.end(err.message);
    });
});

app.listen(port);

module.exports = app;
