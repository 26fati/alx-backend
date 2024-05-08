import { createQueue } from 'kue'
const queue = createQueue();

const jobData = {
    phoneNumber: "1234567890", // Example phone number
    message: "Hello, this is a test message." // Example message
};
const job = queue.create('push_notification_code', jobData).save(function(err) {
    if (!err) console.log('Notification job created: ', job.id);
});

job.on('complete', () => {
    console.log('Notification job completed');
}).on('failed', () => {
    console.log('Notification job failed');
});