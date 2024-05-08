import { createClient } from 'redis';
import { promisify } from 'util'

const client = createClient()

const getAsync = promisify(client.get).bind(client);

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


async function displaySchoolValue(schoolName) {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (error) {
        console.error(error);
    }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
