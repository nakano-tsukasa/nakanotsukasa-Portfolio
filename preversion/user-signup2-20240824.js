
(function() {
    'use strict';
    window.addEventListener('load', function() {
        const forms = document.getElementsByClassName('needs-validation');
        const password = document.getElementById('InputPassword');
        const confirmPassword = document.getElementById('InputConfirmPassword');

        Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                    password.value = '';
                    confirmPassword.value = '';
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
})();

(function(){
    `use strict`;
    window.addEventListener('load', function(){
        const form = document.querySelector('.needs-validation');
        const password = document.getElementById('InputPassword');
        const confirmPassword = document.getElementById('InputConfirmPassword');

        form.addEventListener('submit',function(event){
            if(password.value !== confirmPassword.value || confirmPassword.value === ''){
                event.preventDefault();
                event.stopPropagation();
                confirmPassword.classList.remove('is-valid');
                confirmPassword.classList.add('is-invalid');
            }else{
                confirmPassword.classList.remove('is-invalid');
                confirmPassword.classList.add('is-valid');
            }
        },false)
    },false)
})();
