const BASE_URL = "http://172.16.30.243:8000";

async function save() {
  const barcode = document.getElementById('barcode').value;
  const res = await fetch(`${BASE_URL}/save`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({barcode: barcode, name: "Part", quantity: 1})
  });
  document.getElementById('output').textContent = await res.text();
}

async function check() {
  const barcode = document.getElementById('barcode').value;
  const res = await fetch(`${BASE_URL}/check/${barcode}`);
  document.getElementById('output').textContent = await res.text();
}

async function update() {
  const barcode = document.getElementById('barcode').value;
  const res = await fetch(`${BASE_URL}/update/${barcode}`, { method: "POST" });
  document.getElementById('output').textContent = await res.text();
}

async function del() {
  const barcode = document.getElementById('barcode').value;
  const res = await fetch(`${BASE_URL}/delete/${barcode}`, { method: "DELETE" });
  document.getElementById('output').textContent = await res.text();
}
