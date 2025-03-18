document.addEventListener('DOMContentLoaded', function() {
    const uploadForm = document.getElementById('uploadForm');
    const audioFile = document.getElementById('audioFile');
    const uploadBtn = document.getElementById('uploadBtn');
    const spinner = uploadBtn.querySelector('.spinner-border');
    const alertArea = document.getElementById('alertArea');
    const resultArea = document.getElementById('resultArea');
    const transcriptionText = document.getElementById('transcriptionText');
    const downloadBtn = document.getElementById('downloadBtn');

    function showAlert(message, type = 'danger') {
        alertArea.innerHTML = `
            <div class="alert alert-${type} alert-dismissible fade show" role="alert">
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        `;
    }

    function setLoading(loading) {
        uploadBtn.disabled = loading;
        spinner.classList.toggle('d-none', !loading);
        uploadBtn.textContent = loading ? 'Processing...' : 'Convert to Text';
        if (loading) {
            uploadBtn.prepend(spinner);
        }
    }

    uploadForm.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const file = audioFile.files[0];
        if (!file) {
            showAlert('Please select an audio file.');
            return;
        }

        if (file.size > 16 * 1024 * 1024) {
            showAlert('File size must be less than 16MB.');
            return;
        }

        const formData = new FormData();
        formData.append('audio', file);

        setLoading(true);
        alertArea.innerHTML = '';
        resultArea.classList.add('d-none');

        try {
            const response = await fetch('/upload', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.error || 'Failed to process audio file');
            }

            transcriptionText.value = data.text;
            resultArea.classList.remove('d-none');
            showAlert('Audio successfully transcribed!', 'success');

        } catch (error) {
            showAlert(error.message);
        } finally {
            setLoading(false);
        }
    });

    downloadBtn.addEventListener('click', function() {
        const text = transcriptionText.value;
        if (!text) return;

        const blob = new Blob([text], { type: 'text/plain' });
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = 'transcription.txt';
        a.click();
        window.URL.revokeObjectURL(url);
    });
});
