document.getElementById('now').addEventListener('click', async ()=>{
    try{
        const response = await axios.get('/api/now');
        const data = response.data;
        document.getElementById('tbody').innerHTML=`
            <tr>
                <td>now</td>
                <td>now</td>
                <td>${data.temp}°C</td>
                <td>${data.hum}%</td>
            </tr>
        `;
    }catch(error){
        console.log('api 연결 중 에러발생:', error);
    }
})
document.getElementById('record').addEventListener('click', async ()=>{
    try{
        const response = await axios.get('/api/record');
        const data = response.data;
        document.getElementById('tbody').innerHTML = data.map(i=>
            `
            <tr>
                <td>${i.id}</td>
                <td>${i.create_at}</td>
                <td>${i.temp}°C</td>
                <td>${i.hum}%</td>
            </tr>
            `
        ).join('');
    }catch(error){
        console.log('api 연결 중 에러발생:', error);
    }
})