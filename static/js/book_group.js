$(document).ready(function(){
    
    $('bookGroupSelect').change(function(){
        const groupId = $(this).val();
        $('#groupInfo').html('');

        if(groupId){
            $.ajax({
                url: '/get_group_info/' + groupId,
                method: 'GET',
                success: function(response) {
                    const books = response.books;
                    const content = '';

                    books.forEach(function(book) {
                        const safeBookName = DOMPurify.sanitize(book.book_name);// XSS対策に、サニタイズを行う
                        content += `
                            <div class="col md-4">
                                <a href="{{url_for('main.summarizer', book_id=${book.book_id}, book_name=${safeBookName})}}">
                                    <div class="card">
                                        <img src="/static/img/dog.jpg" alt="Book Cover" class="card-img-top">
                                        <div class="card-body">
                                            <h5 class="card-title">${safeBookName}</h5>
                                        </div>
                                    </div>
                                </a>
                            </div>
                        `;
                    });

                    $('#groupInfo').html(content);
                },
                error: function(){
                    $('#groupInfo').html('<p>Error loading group information.</p>');
                }
            });
        }
    });
});