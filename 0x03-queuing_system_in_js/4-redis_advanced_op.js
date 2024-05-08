import { createClient, print } from 'redis';

const client = createClient()

client.on('connect', function() {
    console.log('Redis client connected to the server');
}).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
}).connect();

client.hSet('HolbertonSchools', 'Portland', '50', print);
client.hSet('HolbertonSchools', 'Seattle', '80', print);
client.hSet('HolbertonSchools', 'New York', '20', print);
client.hSet('HolbertonSchools', 'Bogota', '20', print);
client.hSet('HolbertonSchools', 'Cali', '40', print);
client.hSet('HolbertonSchools', 'Paris', '2', print);

client.hGetAll('HolbertonSchools', function(error, result) {
    if (error) {
        console.error('Error:', error);
    } else {
        console.log(result);
    }
});