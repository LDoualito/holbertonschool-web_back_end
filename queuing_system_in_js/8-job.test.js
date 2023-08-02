import createPushNotificationsJobs from './8-job';
const { expect } = require('chai');
const kue = require('kue');

const queue = kue.createQueue();
const jobs = [
  { phoneNumber: '1234', message: 'Message #1' },
  { phoneNumber: '4567', message: 'Message #2' }
];

before(() => {
  queue.testMode.enter(true);
});

afterEach(() => {
  queue.testMode.clear();
});

after(() => {
  queue.testMode.exit();
});

describe('Test queue', () => {
  it('Expect to throw error', () => {
    expect(() => createPushNotificationsJobs('', queue)).to.throw('Jobs is not an array');
    expect(() => createPushNotificationsJobs(123, queue)).to.throw('Jobs is not an array');
    expect(() => createPushNotificationsJobs(NaN, queue)).to.throw('Jobs is not an array');
  });

  it('Expect to create a notification', () => {
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.equal(2);
    expect(queue.testMode.jobs[0].type).to.equal('push_notification_code_3');
    expect(queue.testMode.jobs[0].data).to.eql({
      phoneNumber: '1234',
      message: 'Message #1'
    });
  });
});
