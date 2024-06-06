$(document).ready(() => {

    //this data suppose to come from users collection
    let users = [
        {
            id: '123',
            name: 'Anurag'
        },
        {
            id: '233',
            name: 'Jon Doe'
        }
    ];

    $.each(users, (index, user) => {
        $('#assgn-by').append('<option id="' + user.id + '">' + user.name + '</option>');
    });




    function render(data) {

        for (var vj = 0; vj < data.length; vj++) {
            $('#body').append(
                $('<tr>').append(
                    $('<td>').text(data[vj].task),
                    $('<td>').text(data[vj].date),
                    $('<td>').text(data[vj].time),
                    $('<td>').text(data[vj].assigned),
                    $('<td>').text(data[vj].status),
                )

            )
        }
    }


    function addTask(postPrm) {
        $.ajax({
            url: '/api/AddTasks',
            data: JSON.stringify(postPrm),
            contentType: 'application/json',
            method: 'POST',
            success: (data) => {

                if (data.status == 200) {
                    alert('Successfully added task')
                    ViewTask()

                } else {
                    alert('Something went wrong')
                }

            },
            err: (error) => {
                console.log(error);
            }
        })
    }

    function ViewTask() {
        var prms = {}
        $.ajax({
            url: '/api/ViewTasks',
            data: prms,
            contentType: 'application/json',
            method: 'POST',
            success: (data) => {

                render(data)

            },
            err: (error) => {
                console.log(error);
            }
        })
    }

    ViewTask()







    //Handle Modal Show /hide
    $('#addtask-btn').on('click', (e) => {
        $('#addtaskmodal').modal('show')
    })

    $('#btn_add').on('click', (e) => {
        var postPrm = {}
        var taskName = $('#taskName').val()
        var date = $('#date').val()
        var time = $('#time').val()
        var assigned = $('#assgn-by option:selected').text()
        var status = $('#status').val()

        postPrm['taskName'] = taskName
        postPrm['date'] = date
        postPrm['time'] = time
        postPrm['assignedBy'] = assigned
        postPrm['status'] = status

        addTask(postPrm)


    })




})