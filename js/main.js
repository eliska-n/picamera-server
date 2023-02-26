function capture() {
	const url = '/capture'
	fetch(url, {
	  method: 'GET',
	})
	.then(response => {
	  if (!response.ok) {
		throw new Error('Network response was not ok');
	  }
	  return response.json();
	})
	.then(responseData => {
	  // handle the response data here
	  imageName = responseData.image_name
	  window.location.href = '/image/${imageName}';
	})
	.catch(error => {
	  console.error('There was a problem with the fetch operation:', error);
	});
}
