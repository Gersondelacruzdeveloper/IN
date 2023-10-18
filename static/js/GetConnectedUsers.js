// Replace 'your-api-endpoint' with the actual endpoint URL
const apiUrl = 'http://127.0.0.1:8000/api/get_connected_users/'

// Function to handle the API response
function handleResponse(response) {
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
}

// Function to handle errors in the API call
function handleError(error) {
  console.error('API call failed:', error);
  // Handle the error gracefully, e.g., show a message to the user
}

// Make the API call
fetch(apiUrl, {
  method: 'GET',
  headers: {
    // Add any necessary headers here, such as authorization token, etc.
    'Content-Type': 'application/json',
  },
})
  .then(handleResponse)
  .then((data) => {
    // 'data' will contain the response from the API
    // Handle the data here, e.g., display it on the webpage
    console.log(data); // or update your UI with the data
  })
  .catch(handleError);
