

import redis from 'redis';

const client = redis.createClient();

client.on('connect', async () => {
    console.log('Redis client connected to the server');
    // Now that the client is connected, execute commands
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');

    // Close the connection when done
    client.quit();
});

client.on('error', err => console.log(`Redis client error: ${err}`));

async function setNewSchool(schoolName, value) {
    await client.set(schoolName, value, (err, value) => {
        if (value) {
            redis.print(`reply: ${value}`)
        }
    });
}

async function displaySchoolValue(schoolName) {
    const value = await client.GET(schoolName, (value, err) => {
        if (value) {
            console.log(value)
        }
        else {
            console.log(err)
        }
    })
}