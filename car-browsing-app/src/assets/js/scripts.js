// This file contains JavaScript code for interactivity on the website, such as fetching car data, handling user interactions, and updating the UI dynamically.

document.addEventListener('DOMContentLoaded', () => {
    const carList = document.getElementById('car-list');
    const carDetails = document.getElementById('car-details');

    // Sample car data
    const cars = [
        { id: 1, name: 'Toyota Camry', specs: 'Engine: 2.5L, Horsepower: 203hp, MPG: 28 city / 39 highway' },
        { id: 2, name: 'Honda Accord', specs: 'Engine: 1.5L Turbo, Horsepower: 192hp, MPG: 30 city / 38 highway' },
        { id: 3, name: 'Ford Mustang', specs: 'Engine: 2.3L EcoBoost, Horsepower: 310hp, MPG: 21 city / 32 highway' },
    ];

    // Function to display car list
    function displayCarList() {
        cars.forEach(car => {
            const listItem = document.createElement('li');
            listItem.textContent = car.name;
            listItem.addEventListener('click', () => displayCarDetails(car));
            carList.appendChild(listItem);
        });
    }

    // Function to display car details
    function displayCarDetails(car) {
        carDetails.innerHTML = `<h2>${car.name}</h2><p>${car.specs}</p>`;
    }

    // Function to filter cars
    function filterCars() {
        const selectedBrand = document.getElementById('brand-dropdown').value.toLowerCase();
        const cars = document.querySelectorAll('.car');

        cars.forEach(car => {
            const brand = car.getAttribute('data-brand').toLowerCase();
            if (selectedBrand === "" || brand === selectedBrand) {
                car.style.display = 'block';
            } else {
                car.style.display = 'none';
            }
        });
    }

    // Initialize the car list on page load
    displayCarList();
});