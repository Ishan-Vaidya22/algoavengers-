document.addEventListener("DOMContentLoaded", () => {
    const currentMonthYear = document.getElementById('month-year');
    const calendar = document.querySelector('.calendar');
    const scheduleModal = document.getElementById('schedule-modal');
    const closeBtn = document.querySelector('.close');
    const interviewDateInput = document.getElementById('interview-date');
    const prevButton = document.querySelector('.prev-button');
    const nextButton = document.querySelector('.next-button');

    let currentDate = new Date();

    // Function to populate the calendar
    function populateCalendar(date) {
        calendar.innerHTML = `
            <div class="day-header">Sun</div>
            <div class="day-header">Mon</div>
            <div class="day-header">Tue</div>
            <div class="day-header">Wed</div>
            <div class="day-header">Thu</div>
            <div class="day-header">Fri</div>
            <div class="day-header">Sat</div>
        `;

        const month = date.getMonth();
        const year = date.getFullYear();
        const firstDay = new Date(year, month, 1).getDay();
        const daysInMonth = new Date(year, month + 1, 0).getDate();

        currentMonthYear.innerText = `${date.toLocaleString('default', { month: 'long' })} ${year}`;

        // Add empty divs before the first day
        for (let i = 0; i < firstDay; i++) {
            const emptyDiv = document.createElement('div');
            emptyDiv.classList.add('day');
            calendar.appendChild(emptyDiv);
        }

        // Add days of the month
        for (let i = 1; i <= daysInMonth; i++) {
            const dayDiv = document.createElement('div');
            dayDiv.classList.add('day');
            dayDiv.innerText = i;
            dayDiv.addEventListener('click', () => openModal(`${i}-${month + 1}-${year}`));
            calendar.appendChild(dayDiv);
        }
    }

    // Function to go to the previous month
    function prevMonth() {
        currentDate.setMonth(currentDate.getMonth() - 1);
        populateCalendar(currentDate);
    }

    // Function to go to the next month
    function nextMonth() {
        currentDate.setMonth(currentDate.getMonth() + 1);
        populateCalendar(currentDate);
    }

    // Function to open the modal
    function openModal(date) {
        interviewDateInput.value = date;
        scheduleModal.style.display = 'block';
    }

    // Function to close the modal
    function closeModal() {
        scheduleModal.style.display = 'none';
    }

    // Event listener to close the modal when clicking the close button
    closeBtn.addEventListener('click', closeModal);

    // Event listeners for navigating months
    prevButton.addEventListener('click', prevMonth);
    nextButton.addEventListener('click', nextMonth);

    // Populate the calendar with the current date
    populateCalendar(currentDate);
});
