const fs = require('fs');
const http = require('http');

const boundary = '----WebKitFormBoundary7MA4YWxkTrZu0gW';
let postData = '';

const addField = (name, value) => {
    postData += `--${boundary}\r\nContent-Disposition: form-data; name="${name}"\r\n\r\n${value}\r\n`;
};

addField('date', '2026-06-29');
addField('titleEn', 'Highway 13 South Ribbon Cutting');
addField('descEn', 'Official ribbon cutting ceremony and handover for the road construction project.');
addField('titleLa', 'ພິທີມອບ-ຮັບໂຄງການ');
addField('descLa', 'ໂຄງການກໍ່ສ້າງທາງເບຕົງ ແຕ່ສາມແຍກທາງ 13 ໃຕ້...');
postData += `--${boundary}--\r\n`;

const options = {
    hostname: 'localhost',
    port: 3000,
    path: '/api/activities',
    method: 'POST',
    headers: {
        'Content-Type': `multipart/form-data; boundary=${boundary}`,
        'Content-Length': Buffer.byteLength(postData)
    }
};

const req = http.request(options, (res) => {
    let data = '';
    res.on('data', chunk => data += chunk);
    res.on('end', () => console.log('Response:', data));
});

req.on('error', (e) => console.error(e));
req.write(postData);
req.end();
