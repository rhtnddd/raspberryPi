document.getElementById('submitBtn').addEventListener('click', ()=>{
    const value = parseInt(document.querySelector('input').value);
    if(!isNaN(value) && value >= 0 && value <= 180){
        fetch('/rotate', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ angle: value })
        })
        .then(res => res.json())
        .then(data => {
            if(data.status === 'ok'){
                console.log("회전 각도:", data.angle);
            }else{
                alert(`에러: ${data.msg}`);
            }
        })
        .catch(err => {
            console.error(err);
            alert('서버 연결 실패');
        });
    } else {
        alert("0~180 사이 숫자를 입력하세요");
    }
});