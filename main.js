/* User Page*/ 

$('.user-name-wrapper ul').hide();

$(document).click(function(e) {
	$('.user-name-wrapper ul').hide();
	$('body').removeClass('slide-fixed-open');
})

$('span.user-name').click(function(e) {
	e.stopPropagation();
	$(this).next('.user-name-wrapper ul').slideToggle(150);
});
$('.user-name-wrapper ul,.fixed-item-container').click(function(e) {
	e.stopPropagation();
});
$('.notification').click(function(e) {
	e.stopPropagation();
	$('body').toggleClass('slide-fixed-open');
});
$(window).mousemove(function(e) {
	var pointerPos = e.clientX;
	var winWidth = $(window).width();
	if (winWidth < pointerPos + 2) {
		$('body').addClass('slide-fixed-open');
	}
});
$('ul.list ul').each(function(){
$(this).addClass('child-list-wrapper');
$(this).children('li').addClass('child-item');
});

$('.child-list-wrapper').each(function(){
$(this).closest('li').addClass('wrapper-list-child-items');
});
$('.wrapper-list-child-items').prepend('<div class="child-trigger"></div>');
$('.child-trigger').click(function(){
$(this).siblings('.child-list-wrapper').slideToggle();
$(this).toggleClass('child-open');
	$(this).next('a').toggleClass('background');
});
$('.child-trigger').mouseenter(function(){
$(this).next('a').addClass('hover');
});
$('.child-trigger').mouseleave(function(){
$(this).next('a').removeClass('hover');
});

/* Login Sigin*/ 

//NAVIGATION BAR SCROLL EFFECT

jQuery(document).ready(function(){
    window.onscroll = function() {
        if (window.pageYOffset >= 650){
            jQuery('#nav-container').css({background:'white', 'box-shadow':'0px 14px 37px 1px rgba(0,0,0,0.1)'});
            jQuery('.nav-but').css({color:'#26282c'});
            jQuery('.login').css({border:'solid 1px #26282c'});
        }
        else {
            jQuery('#nav-container').css({background:'linear-gradient(135deg,#fdac75 0%,#f76039 100%)', 'box-shadow':'none'});
            jQuery('.nav-but').css({color:'white'});
            jQuery('.login').css({border:'solid 1px white'});
        }
    }
});

// login/sign up

let usernameField = document.getElementById('username'),
	emailField = document.getElementById('email'),
	passwordField = document.getElementById('password'),
	submitButton = document.getElementById('submit');

function isUsernameValid(username) {
	return username.length >= 5;
}

function isEmailValid(email) {
	return /[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,3}$/i.test(email);
}

function isPasswordValid(password) {
	/*
	Must contain at least one number and one uppercase and lowercase letter, and
	at least 8 or more characters.
	 */
	return /(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}/.test(password);
}

function validateUsernameField(event) {
	let value = usernameField.value;

	if (isUsernameValid(value)) {
		usernameField.classList.add('valid');
	} else {
		usernameField.classList.remove('valid');
	}
}

function validateEmailField(event) {
	let value = emailField.value;

	if (isEmailValid(value)) {
		emailField.classList.add('valid');
	} else {
		emailField.classList.remove('valid');
	}
}

function validatePasswordField(event) {
	let password = passwordField.value;

	if (isPasswordValid(password)) {
		passwordField.classList.add('valid');
	} else {
		passwordField.classList.remove('valid');
	}
}

usernameField.addEventListener('keyup', validateUsernameField);
emailField.addEventListener('keyup', validateEmailField);
passwordField.addEventListener('keyup', validatePasswordField);

submitButton.addEventListener('click', function(event) {
	event.preventDefault();
});

/* Self invoking function */
(function() {
	validateUsernameField();
	validateEmailField();
	validatePasswordField();
})();

//admin
var toggle = true;
$('.mobile-dropdown').on('click', function(){
  
  alert('oh yeahh');
  if(toggle===true){
    $(this).addClass('active-drop');
    toggle = false;
    alert('turned on');
  }else{
    $(this).removeClass('active-drop');
    toggle = true;
    alert('turned off');
  }
})

//petition
$(document).ready(function() {
  
});

//reg
var clientStatus = "NONE";

$(".searchbutton").click(searching);    // listner for the search button
//$("#authcheckbox").click(ManualAuth);   // wait for manual authentication

function searching() {
  $(body).css("backgound", gray);
  $(".header").css("display", "none").addClass("fade"); // remove the FreeSpeech header
  $(".login").css("display", "none").addClass("fade"); // remove the search box
  setTimeout(function() {
    //delay for 0.5 sec
  }, 500);
  $(".results").css("display", "").addClass("fadein"); // Display the results view

  if (clientStatus === "NONE") {
    $("#client-status").text("Not Enrolled");
    $(".checkbox").css("visibility", "visible");
    $("#enrolbutton").css("visibility", "visible");
    $("#checkbox-label").css("visibility", "visible");
  }
  
  if (clientStatus === "PARTIAL"){
    $("#client-status").text("Partially Enrolled");
    $(".checkbox").css("visibility", "visible");
    $("#enrolbutton").css("visibility", "visible");
    $("#checkbox-label").css("visibility", "visible");
  }
  
  if(clientStatus === "ENROLLED"){
    $("#client-status").text("Fully Enrolled");
    $("#verifybutton").css("visibility", "visible");
  }
  
  if(clientStatus === "OPTED-OUT"){
    $("#client-status").text("Fully Enrolled - Opted Out");
    $(".checkbox").css("visibility", "visible");
    $("#checkbox-label").css("visibility", "visible").text("Client wants to Opt back In");
    $("#verifybutton").css("visibility", "visible");
  }
  
  if(clientStatus === "LOCKED"){
    $("#client-status").text("Locked-Out");
    $("#status-results").css("visibility", "visible").text("Multiple Failed Attempts");
    $("#status-results").css("background", "orange");
  }
}


// login
function myFunction() {
    var x = document.getElementById("myInput");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
	}
	
	//aspirant reg
	$(function() {

		// We can attach the `fileselect` event to all file inputs on the page
		$(document).on('change', ':file', function() {
			var input = $(this),
					numFiles = input.get(0).files ? input.get(0).files.length : 1,
					label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
			input.trigger('fileselect', [numFiles, label]);
		});

		// We can watch for our custom `fileselect` event like this
		$(document).ready( function() {
				$(':file').on('fileselect', function(event, numFiles, label) {

						var input = $(this).parents('.input-group').find(':text'),
								log = numFiles > 1 ? numFiles + ' files selected' : label;

						if( input.length ) {
								input.val(log);
						} else {
								if( log ) alert(log);
						}

				});
		});
	});

	// Function for Specilization Input
	$( function() {
		var availableTags = [
			"Jubilee",
			"NASA",
			"Republican",
			"Maendeleo Chap chap",
			"Narc Kenya",
			"Chama Cha Mashinani",
		];
		$( "#tags" ).autocomplete({
			source: availableTags
		});
	} );

	// Function for Designation Input
	$( function() {
		var availableTags = [
			"President",
			"Governor",
			"Senator",
			"Member of Parliament",
			"Women Rep",
			"MCA",
		];
		$( "#designation" ).autocomplete({
			source: availableTags
		});
	} );

	$('form').submit(function(){
		$('.thanks').show();
		$('.thanks').delay(2000).fadeOut();
		window.setInterval(function() {
			 window.location.reload();
			 $('form input#name').focus();
		 }, 2500);
		event.preventDefault(); // Here triggering stops
	});

	// Autocomplete for Specialization
	$( "#tags" ).autocomplete({
		source:tags,
		//To select only from the autocomplete
			change: function (event, ui) {
				if (ui.item == null || ui.item == undefined) {
					$(this).val("");
					$(this).attr("disabled", false);
				}
			}
	 });

	// Autocomplete for Designation
	$( "#designation" ).autocomplete({
		source:tags,
		//To select only from the autocomplete
			change: function (event, ui) {
				if (ui.item == null || ui.item == undefined) {
					$(this).val("");
					$(this).attr("disabled", false);
				}
			}
	 });
