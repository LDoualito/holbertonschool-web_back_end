export default function updateStudentGradeByCity(students, city, newGrades) {
    return students
      .filter((student) => student.location === city)
      .map((x) => {
        const newGrade = newGrades.filter((newGrade) => newGrade.studentId === x.id);
        const student = x;
        if (newGrade.length === 1) student.grade = newGrade[0].grade;
        else student.grade = 'N/A';
        return student;
      });
  }
