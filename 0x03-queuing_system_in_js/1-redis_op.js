import { createClient } from 'redis';

const client = createClient()

client.on('connect', function() {
    console.log('Redis client connected to the server');
}).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
}).connect();

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, function(err, reply) {
        if (err) {
            console.error('Error:', err);
        } else {
            console.log('Reply:', reply);
        }
        });
}


function displaySchoolValue(schoolName) {
    client.get(schoolName, function(error, result) {
        if (error) {
          console.log(error);
        }
        console.log(result);
      });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
