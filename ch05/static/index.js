document.getElementById('now').addEventListener('click', async ()=>{
    try{
        const response = await axios.get('/api/now');
        const data = response.data;
        document.getElementById('tbody').innerHTML=`
            <tr>
                <td>-</td>
                <td>현재</td>
                <td>${data.temp}°C</td>
                <td>${data.hum}%</td>
            </tr>
        `;
    }catch(error){
        console.log('api 연결 중 에러발생:', error);
        alert('데이터를 불러오는데 실패했습니다.');
    }
});

document.getElementById('record').addEventListener('click', async ()=>{
    try{
        const response = await axios.get('/api/record');
        const data = response.data;
        document.getElementById('tbody').innerHTML = data.map(i=>
            `
            <tr>
                <td>${i.id}</td>
                <td>${i.created_at || i.create_at}</td>
                <td>${i.temperature}°C</td>
                <td>${i.humidity}%</td>
            </tr>
            `
        ).join('');
    }catch(error){
        console.log('api 연결 중 에러발생:', error);
        alert('데이터를 불러오는데 실패했습니다.');
    }
});