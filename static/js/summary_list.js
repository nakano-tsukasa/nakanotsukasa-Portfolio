document.addEventListener('DOMContentLoaded', function(){
    let currentIndex = 0;

    const summaryDisplay = document.getElementById('summaryDisplay');
    const summaryDisplay2 = document.getElementById('summaryDisplay2');
    const prevBtn = document.getElementById('prev-btn');
    const nextBtn = document.getElementById('next-btn');
    const title1 = document.getElementById('title1')

    function updateSummary(index){
        if(index < 0){
            summaryDisplay2.textContent = summaries2[0];
            summaryDisplay.textContent = summaries[0];
            title1.textContent = 'First Summary'
        }else if(index == 0){
            summaryDisplay2.textContent = summaries2[index];
            summaryDisplay.textContent = summaries[index];
            title1.textContent = 'First Summary'
        }else if (index > 0 && index < summaries2.length - 1){
            summaryDisplay2.textContent = summaries2[index];
            summaryDisplay.textContent = summaries[index];
            title1.textContent = 'Derived Summary'
        }else if(index == summaries2.length - 1){
            summaryDisplay2.textContent = summaries2[index];
            summaryDisplay.innerHTML = "";
            title1.textContent = 'Derived Summary'
        }else{
            return
        }
    }

    prevBtn.addEventListener('click', function(){
        if(currentIndex > 0){
            updateSummary(currentIndex - 1);
            currentIndex -= 1
        }else{
            return
        }
    });

    nextBtn.addEventListener('click', function(){
        if(currentIndex <= summaries.length - 1){
            updateSummary(currentIndex + 1)
            currentIndex += 1
        }else{
            return
        }
    });

    updateSummary(currentIndex)
});

