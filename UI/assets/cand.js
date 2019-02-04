let collapsibleBox = document.querySelector('header.front .bottom-header .box');
let mobileMenu = document.querySelector('header.front .bottom-header ul');

collapsibleBox.addEventListener('click', () => {
  mobileMenu.classList.toggle('show');
});

// function to add show class to the sign up modal
let showSignUpModal = () => signUpModal.classList.add('show');

// function to add show class to the login modal
let showlogInModal = () => logInModal.classList.add('show');

// function to add show class to the sign up modal
let showsignUpModal = () => logInModal.classList.add('show');

// function to remove modal from login and sign up modal
let closeModal = () => {
  signUpModal.classList.remove('show');
  logInModal.classList.remove('show');
};

// attach event listener to the log in links and add show class on click
logInLink.addEventListener('click', showlogInModal, );
signUpLink.addEventListener('click', showsignUpModal);


closeBtn.addEventListener("click", closeModal);


// sign up and login redirects to profile page
let logInButton = document.getElementById("login-button")
logInButton.addEventListener('click', (e) => {
  e.preventDefault();
  window.location.href = 'dashboard/profile.html'
})
let signUpButton = document.getElementById("signup-button")
logInButton.addEventListener('click', (e) => {
  e.preventDefault();
  window.location.href = 'dashboard/profile.html'
})

$('.form').find('input, textarea').on('keyup blur focus', function(e) {

  var $this = $(this),
    label = $this.prev('label');

  if (e.type === 'keyup') {
    if ($this.val() === '') {
      label.removeClass('active highlight');
    } else {
      label.addClass('active highlight');
    }
  } else if (e.type === 'blur') {
    if ($this.val() === '') {
      label.removeClass('active highlight');
    } else {
      label.removeClass('highlight');
    }
  } else if (e.type === 'focus') {

    if ($this.val() === '') {
      label.removeClass('highlight');
    } else if ($this.val() !== '') {
      label.addClass('highlight');
    }
  }

});

$('.tab a').on('click', function(e) {

  e.preventDefault();

  $(this).parent().addClass('active');
  $(this).parent().siblings().removeClass('active');

  target = $(this).attr('href');

  $('.tab-content > div').not(target).hide();

  $(target).fadeIn(600);

});

var isActive = false;

$('.js-menu').on('click', function() {
	if (isActive) {
		$(this).removeClass('active');
		$('body').removeClass('menu-open');
	} else {
		$(this).addClass('active');
		$('body').addClass('menu-open');
	}

	isActive = !isActive;
});

function myFunction() {
  var x = document.getElementById("myInput");
  if (x.type === "password") {
    x.type = "text";
  } else {
    x.type = "password";
  }
}
