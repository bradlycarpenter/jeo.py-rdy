async function myFunction() {
  try {
    const response = await fetch("http://127.0.0.1:5000");
    const text = await response.text();
    let x = document.getElementById("1");
    x.innerHTML = text;
  } catch (error) {
    console.log("Error fetching data:", error);
  }
}
