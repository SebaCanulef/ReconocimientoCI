const video = document.getElementById('video');
const captureButton = document.getElementById('capture');
const canvas = document.getElementById('canvas');
const capturedImage = document.getElementById('captured-image');
const imgDataInput = document.getElementById('img_data');

const constraints = { video: true };

// Inicializa la cámara al cargar la página
async function initCamera() {
    try {
        const stream = await navigator.mediaDevices.getUserMedia(constraints);
        video.srcObject = stream; 
    } catch (err) {
        console.error('Error accessing the camera:', err);
    }
}

// Captura la imagen cuando se presiona el botón "Tomar Foto"
captureButton.addEventListener('click', () => {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    capturedImage.src = canvas.toDataURL('image/png'); 
    imgDataInput.value = capturedImage.src; 
    capturedImage.style.display = 'block'; 
    canvas.style.display = 'none'; 
    video.style.display = 'none'; 
    captureButton.style.display = 'none'; 

    // Muestra el botón "Procesar Imagen"
    document.getElementById('image-form').style.display = 'block';
});

initCamera(); // Inicializa la cámara al cargar la página
