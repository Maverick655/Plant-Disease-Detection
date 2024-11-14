document.getElementById("upload-form").onsubmit = async function(event) {
    event.preventDefault();

    const formData = new FormData();
    const fileInput = document.querySelector("input[type='file']");
    formData.append("file", fileInput.files[0]);

    const response = await fetch("/predict", {
        method: "POST",
        body: formData,
    });

    const result = await response.json();
    document.getElementById("result").textContent = result.prediction;
    if (result.img_path) {
        document.getElementById("display-image").innerHTML = `<img src="/${result.img_path}" alt="Uploaded Image" width="300px">`;
    }
};
