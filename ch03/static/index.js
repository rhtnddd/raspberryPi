let userSequence = [];
let isGameActive = false;

function start(){
    userSequence = [];
    isGameActive = true;
    document.getElementById('status').innerHTML = '색깔 버튼을 눌러보세요!';

    document.getElementById('main').innerHTML=`
    <button style=" width: 100px;
    height: 100px; background-color: red;
    border: none; cursor: pointer;"
    onmouseover="this.style.filter='brightness(80%)'"
    onmouseout="this.style.filter='brightness(100%)'" 
    onclick="buttonClick('red')"
    id="red"
    ></button>
    <button style=" width: 100px;
    height: 100px; background-color: yellow;
    border: none; cursor: pointer;"
    onmouseover="this.style.filter='brightness(80%)'"
    onmouseout="this.style.filter='brightness(100%)'"
    onclick="buttonClick('yellow')"
    id="yellow"
    ></button>
    <button style=" width: 100px;
    height: 100px; background-color: green;
    border: none; cursor: pointer;" 
    onmouseover="this.style.filter='brightness(80%)'"
    onmouseout="this.style.filter='brightness(100%)'"
    onclick="buttonClick('green')"
    id="green"
    ></button>
    `;
}

function buttonClick(color) {
    if (!isGameActive) return;

    userSequence.push(color);

    const button = document.getElementById(color);
    button.style.transform = 'scale(0.95)';
    setTimeout(() => {
        button.style.transform = 'scale(1)';
    }, 150);

    document.getElementById('status').innerHTML =
        `입력된 순서: ${userSequence.join(' → ')} (${userSequence.length}개)`;

    if (userSequence.length === 3) {
        setTimeout(() => {
            submitSequence();
        }, 300);
    }
}

function submitSequence() {
    if (userSequence.length === 0) {
        alert('먼저 색깔 버튼을 눌러주세요!');
        return;
    }

    isGameActive = false;

    const gameData = {
        sequence: userSequence,
        timestamp: new Date().toISOString(),
        length: userSequence.length
    };

    fetch('/submit_sequence', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(gameData)
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('status').innerHTML =
            `순서: ${userSequence.join(' → ')} (서버 응답: ${data.message})`;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('status').innerHTML =
            `전송 실패: ${userSequence.join(' → ')}`;
    });

    console.log('전송할 데이터:', gameData);
}