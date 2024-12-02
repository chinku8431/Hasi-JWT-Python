const response = await fetch("http://127.0.0.1:8000/compare-files/", {
    method: "POST",
    headers: {
        Authorization: `Bearer ${token}`,
    },
    body: formData,
});


// const response = await fetch("/compare-files/", {
//     method: "POST",
//     body: formData,
// });

