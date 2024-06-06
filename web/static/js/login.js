/*
 * Anurag.n
* 2024/06/06 
*/


$(document).ready(() => {



    $('#register-link').on('click', (e) => {
        $('#sign-in-div').hide()
        $('#register-div').show();
    })
    $('#login-link').on('click', (e) => {
        $('#sign-in-div').show()
        $('#register-div').hide();
    })


    function RegisterUser(postPrms) {
        $.ajax({
            url: '/api/register',
            data: JSON.stringify(postPrms),
            contentType: 'application/json',
            method: 'POST',
            success: (data) => {

                if (data.status == 200) {
                    alert('Successfully Registered , please login')
                    $('#sign-in-div').show()
                    $('#register-div').hide();
                } else {
                    alert('Something went wrong')
                }

            },
            err: (error) => {
                console.log(error);
            }
        })
    }

    function Authentication(postPrms) {
        $.ajax({
            url: '/api/login',
            data: JSON.stringify(postPrms),
            contentType: 'application/json',
            method: 'POST',
            success: (data) => {

                if (data.status == 200) {
                   alert('Welcome to main screen')
                   window.location = 'main'
                } else {
                    alert(data.message)
                }

            },
            err: (error) => {
                console.log(error);
            }
        })
    }



    //Handle Register

    $('#register-btn').on('click', (e) => {

        e.preventDefault();

        // Get the data from frontend
        var postPrms = {};
        var name = $('#name').val().trim();
        var email = $('#emailIid').val().trim();
        var mobile = $('#mobile').val().trim();
        var password = $('#pass').val().trim();

        if (!name || !email || !mobile || !password) {
            alert("All fields are required!");
            return;
        }

        postPrms['name'] = name;
        postPrms['email'] = email;
        postPrms['mobile'] = mobile;
        postPrms['password'] = password;

        RegisterUser(postPrms);
    });


    //handle login
    $('#SignIn').on('click', (e) => {

        e.preventDefault();

        // Get the data from frontend
        var postPrms = {};
        var email = $('#email-id').val().trim();
        var password = $('#password').val().trim();

        if (!email || !password) {
            alert("All fields are required!");
            return;
        }

        postPrms['email'] = email;
        postPrms['password'] = password;

        Authentication(postPrms);
    });



})
