const input = document.getElementById("input");
const send = document.getElementById("send");

send.addEventListener("click", async () => {
  const response = await fetch(`/send`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(input.value),
  });
});