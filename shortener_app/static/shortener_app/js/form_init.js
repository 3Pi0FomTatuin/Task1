function inputHandler() {
    this.parentElement.classList.add('form-field_focused');
}

function blurHandler() {
    if (!this.value && this.parentElement.classList.contains('form-field_focused')) {
        this.parentElement.classList.remove('form-field_focused');
    }
}

for (let input of document.querySelectorAll('.form-field input')) {
    input.oninput = input.onfocus = inputHandler;
    input.onblur = blurHandler;
}
