let click = document.getElementById("click");
let junsong = document.getElementById("junsong");
let num1 = document.getElementById("num1");
let num2 = 0;
num1.textContent = num2;
click.addEventListener('click', () => {
    num2 += 1;
    num1.textContent = num2;
});
junsong.addEventListener('click',async () => {
    let res = await fetch("/junsong",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify({value:num2})
    })
    // location.href="http://127.0.0.1:5001/junsong/"+num2;
    num2 =0;
    num1.textContent = 0;
});
