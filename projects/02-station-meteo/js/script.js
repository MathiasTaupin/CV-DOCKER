// Script pour la Station Météo
document.addEventListener('DOMContentLoaded', function() {
    const cityInput = document.getElementById('cityInput');
    const searchBtn = document.getElementById('searchBtn');
    const weatherInfo = document.getElementById('weatherInfo');

    // Remplacer par votre clé API OpenWeatherMap
    const apiKey = 'YOUR_API_KEY_HERE';

    searchBtn.addEventListener('click', function() {
        const city = cityInput.value.trim();
        if (city) {
            getWeather(city);
        } else {
            alert('Veuillez entrer le nom d\'une ville.');
        }
    });

    cityInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            searchBtn.click();
        }
    });

    async function getWeather(city) {
        try {
            weatherInfo.innerHTML = '<p>Chargement...</p>';

            // Simulation de données météo (remplacer par l'appel API réel)
            // const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}&units=metric&lang=fr`);
            // const data = await response.json();

            // Données simulées pour démonstration
            const mockData = {
                name: city,
                main: {
                    temp: Math.floor(Math.random() * 30) + 5,
                    humidity: Math.floor(Math.random() * 100),
                    pressure: Math.floor(Math.random() * 200) + 1000
                },
                weather: [{
                    description: 'ensoleillé',
                    icon: '01d'
                }],
                wind: {
                    speed: Math.floor(Math.random() * 20)
                }
            };

            displayWeather(mockData);
        } catch (error) {
            weatherInfo.innerHTML = '<p>Erreur lors de la récupération des données météo.</p>';
            console.error('Erreur:', error);
        }
    }

    function displayWeather(data) {
        const html = `
            <h3>${data.name}</h3>
            <div class="temp">${data.main.temp}°C</div>
            <div class="description">${data.weather[0].description}</div>
            <div class="weather-details">
                <div class="weather-detail">
                    <div class="label">Humidité</div>
                    <div class="value">${data.main.humidity}%</div>
                </div>
                <div class="weather-detail">
                    <div class="label">Pression</div>
                    <div class="value">${data.main.pressure} hPa</div>
                </div>
                <div class="weather-detail">
                    <div class="label">Vent</div>
                    <div class="value">${data.wind.speed} m/s</div>
                </div>
            </div>
        `;
        weatherInfo.innerHTML = html;
    }

    // Charger la météo de Paris par défaut
    getWeather('Paris');
});