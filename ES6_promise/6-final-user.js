import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
    .then((res) => {
      for (const e of res) {
        if (e.status === 'rejected') {
          e.value = `Error: ${e.reason.message}`;
          delete e.reason;
        }
      }
      return res;
    });
}
