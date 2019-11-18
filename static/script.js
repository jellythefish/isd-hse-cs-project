$('#file').on('change', function () {
    var fileName = $(this).val().replace(/C:\\fakepath\\/i, '');
    $(this).next('.custom-file-label').html(fileName);
})

$('#btn-file').on('click', function () {
    $('#file').click();
})

$('#submit-file').on('click', function () {
    $('#convert-message-result').remove();
    let responseLabel = $('<div>', {
        class: 'alert',
        id: 'convert-message-result'
    });
    $('#main').append(responseLabel);

    if ($('#file').val() === "") {
        responseLabel.text("You didn't choose a file!");
        responseLabel.addClass('alert-danger');
    } else {
        let formData = new FormData();
        formData.append('file', $('#file')[0].files[0]);

        fetch('/convert/' + $('#inputGroupSelect :selected').text(), {
            method: 'POST',
            body: formData
        }).then(resp => {
            if (resp.status === 200) {
                return resp.blob()
            } else {
                responseLabel.text("Bad request!");
                responseLabel.addClass('alert-warning');
            }
        }).then(blob => {
            if (blob == undefined) {
                return;
            }

            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = $('#file').val().replace(/C:\\fakepath\\/i, '');
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            responseLabel.text("Success!");
            responseLabel.addClass('alert-success');
        });
    }
})