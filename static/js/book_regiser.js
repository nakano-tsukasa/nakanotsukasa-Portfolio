//=====================variables=====================


//=====================functions=====================
// +-------+------------------+-----------------------------+
// | number| functionName     | functionPrescription        |
// +-------+------------------+-----------------------------+
// | f1    | checkBlank       | check if input is blank     |
// +-------+------------------+-----------------------------+

//--------------------f0:IIFE--------------------

(function(){
    checkBlank();
})();

//--------------------f1:checkBlank--------------------
//check if input is blank
function checkBlank(){
    'use strict';
    window.addEventListener('load', function() {
        const forms = document.getElementsByClassName('needs-validation');
        const bookTitle = document.getElementById('bookTitle');

        Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
                if (form.checkValidity() === false) {
                    event.preventDefault();
                    event.stopPropagation();
                }
                form.classList.add('was-validated');
            }, false);
        });
    }, false);
};
