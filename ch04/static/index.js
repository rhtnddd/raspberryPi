document.getElementById('submitBtn').addEventListener('click', ()=>{
    const value = document.querySelector('input').value;
    console.log(value);

    if(value>=0 && value<=180){
        fetch('http://localhost:5000/rotate',{
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                angle: parseInt(value)
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            if(data.status === 'ok'){
                console.log(data.angle);
            }else{
                alert(`에러: ${data.msg}`);
            }
        })
        .catch(error => {
            console.error('Error:', error);
            alert('서버 연결 실패');
        });
    }else{
        alert("잘못된 입력 입니다");
    }
});