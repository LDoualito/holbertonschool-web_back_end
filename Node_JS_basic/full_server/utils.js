const fs = require('fs');

export default function readDatabase(path) {
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
      const fieldSort = Array.from(field).sort();
      fieldSort.forEach((f) => {
        const students = lines.filter((line) => line.split(',')[3] === f);
        all[f] = {
          students: `List: ${students.map((student) => student.split(',')[0]).join(', ')}`,
          count: students.length,
        };
      });
      return resolve(all);
    });
  });
}
