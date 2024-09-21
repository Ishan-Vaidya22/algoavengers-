document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Example validation
    const dob = document.getElementById('dob').value;
    const rollNo = document.getElementById('rollNo').value;
    const mobile = document.getElementById('mobile').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    
    if (!dob || !rollNo || !mobile || !email || !password) {
        alert('All fields are required!');
        return;
    }
    
    // Proceed with form submission or AJAX call
    console.log('Form Submitted');
});
