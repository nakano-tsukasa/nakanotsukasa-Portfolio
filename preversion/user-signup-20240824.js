//=====================variables=====================

const inputs = Array.from(document.querySelectorAll('.input-area input')).slice(0,-1);
const warnings = document.querySelectorAll('.warning');
const notmatch = document.querySelector('#notmatch');
const pass01 = document.querySelector('#pass01');
const pass02 = document.querySelector('#pass02');
const form = document.querySelector('#form');
const submiterror = document.querySelector('#submiterror');
const submit = document.querySelector('.submit');

//=====================functions=====================
// +-------+--------------+-------------------------+
// | number| functionName | functionPrescription    |
// +-------+--------------+-------------------------+
// | f1    | checkBlank   | check prior blank       |
// +-------+--------------+-------------------------+
// | f2    | checkPass    | make sure pass the same |
// +-------+--------------+-------------------------+
// | f3    | checkAll     | confirm before submit   |
// +-------+--------------+-------------------------+
// | f4    | submitInfo   | submit user information |
// +-------+--------------+-------------------------+

//--------------------f0:IIFE--------------------

(function(){
    checkblank();
    checkpass();
    checkAll();
    submitInfo();
})();



//--------------------f1:checkblank--------------------

function checkblank(){
    inputs.forEach((input,index) => {
        input.addEventListener('blur',function(){
            if(input.value === ''){
                warnings[index].style.display = 'inline';
            }else{
                warnings[index].style.display = 'none';
            }
        })
    });
};

//--------------------f2:checkpass--------------------

function checkpass(){
    pass02.addEventListener('blur',function(){
        if(pass01.value !== pass02.value){
            notmatch.style.display = 'inline';
        }else{
            notmatch.style.display = 'none';
        }
    });
};

//--------------------f3:checkAll--------------------

function checkAll(){
    form.addEventListener('submit',function(event){
        pass02.blur();
        const checkform = inputs[0].value !== '' &&
        inputs[1].value !== '' &&
        inputs[2].value !== '' &&
        pass01.value === pass02.value;
    
        if(!checkform){
            submiterror.style.display = 'inline';
            event.preventDefault();
        }else{
            submiterror.style.display = 'none';
            event.preventDefault();
            submitInfo();
        }
    });
};

//--------------------f4:submitInfo()--------------------


function submitInfo(){
    const formData = {
        name: inputs[0].value,
        mail: inputs[1].value,
        pass01: pass01.value,
        pass02: pass02.value
    };

    fetch('http://localhost:5500/user-post',{
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
    })
    .then(response => {
        if(!response.ok){
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Success:',data);
    })
    .catch(error => {
        console.error('Error',error);
    });
};