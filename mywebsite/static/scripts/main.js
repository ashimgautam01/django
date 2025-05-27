
document.getElementById('contactForm').addEventListener('submit', function(e) {
  e.preventDefault();
  
  const submitBtn = document.getElementById('submitBtn');
  const btnText = document.getElementById('btnText');
  const successMessage = document.getElementById('successMessage');
  
  btnText.textContent = 'Sending...';
  submitBtn.disabled = true;
  submitBtn.classList.add('opacity-75');
  
  setTimeout(() => {
    btnText.textContent = 'Send Message';
    submitBtn.disabled = false;
    submitBtn.classList.remove('opacity-75');
    
    successMessage.classList.remove('hidden');
    
    this.reset();
    setTimeout(() => {
      successMessage.classList.add('hidden');
    }, 5000);
  }, 2000);
});

const inputs = document.querySelectorAll('input, textarea');
inputs.forEach(input => {
  input.addEventListener('focus', function() {
    this.parentElement.classList.add('scale-105');
  });
  
  input.addEventListener('blur', function() {
    this.parentElement.classList.remove('scale-105');
  });
});