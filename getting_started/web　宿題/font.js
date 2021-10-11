const colors = ['#7FFFD4','#ADFF2F','#EE82EE'];
var blobs = document.querySelectorAll("#background path");

blobs.forEach(blob => {
    blob.style.fill = colors[Math.floor(Math.random() * colors.length)];
});